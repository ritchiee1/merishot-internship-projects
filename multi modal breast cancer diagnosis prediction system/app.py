import streamlit as st
import numpy as np
import joblib
from PIL import Image
from tensorflow.keras.models import load_model

# page config 
st.set_page_config(
    page_title="Breast Cancer Multimodal Diagnosis",
    layout="wide",
    page_icon="🧬"
)

# constants
IMG_SIZE = 224
MODEL_PATH = "breast_cancer_multimodal_model.h5"
SCALER_PATH = "clinical_scaler.pkl"

# load model + scaler
@st.cache_resource
def load_resources():
    model = load_model(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return model, scaler

model, scaler = load_resources()

# feature names
feature_names = [
"mean radius","mean texture","mean perimeter","mean area","mean smoothness",
"mean compactness","mean concavity","mean concave points","mean symmetry","mean fractal dimension",
"radius error","texture error","perimeter error","area error","smoothness error",
"compactness error","concavity error","concave points error","symmetry error","fractal dimension error",
"worst radius","worst texture","worst perimeter","worst area","worst smoothness",
"worst compactness","worst concavity","worst concave points","worst symmetry","worst fractal dimension"
]

# title
st.title("🧬 Breast Cancer Diagnosis System")
st.markdown("### Multimodal Prediction using Histopathology Images + Cell Nuclei Morphological Features")

st.markdown("---")

# layout
col1, col2 = st.columns([1,1])

# clinical features
with col1:

    st.subheader("Cell Nuclei Morphological Features")

    clinical_inputs = []

    for feature in feature_names:
        value = st.number_input(feature, value=0.0)
        clinical_inputs.append(value)

    clinical_array = np.array(clinical_inputs).reshape(1, -1)

# image upload
with col2:

    st.subheader("Histopathology Image")

    uploaded_file = st.file_uploader(
        "Upload Breast Tissue Image",
        type=["png","jpg","jpeg"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", width=300)

        image = image.resize((IMG_SIZE, IMG_SIZE))
        image_array = np.array(image)/255.0
        image_array = np.expand_dims(image_array, axis=0)

    else:
        image_array = None

# prediction button
st.markdown("---")

if st.button("Run Prediction"):

    try:

        clinical_scaled = scaler.transform(clinical_array)

        # combined prediction
        if image_array is not None:

            prediction = model.predict([image_array, clinical_scaled])[0][0]

        # clinical only
        
        else:

            dummy_image = np.zeros((1,224,224,3))
            prediction = model.predict([dummy_image, clinical_scaled])[0][0]

        # ------------------------
        # Result
        # ------------------------
        st.markdown("## Prediction Result")

        if prediction > 0.5:
            st.success("Diagnosis: **BENIGN**")
        else:
            st.error("Diagnosis: **MALIGNANT**")

        st.write(f"Prediction Probability: {prediction:.4f}")

    except Exception as e:

        st.error(f"Prediction failed: {e}")


# info section
st.markdown("---")

st.subheader("About This System")

st.markdown("""
This system is a multimodal breast cancer prediction tool that analyzes biopsy data to predict wheather a tumor is **benign** or **malignant** using **multimodal deep learning model**.
The system makes predictions in three ways:
            
- **Image Prediction:** analyzes histopathology images of breast tissue using deep learning.
- **Feature Prediction:** analyzes cell nuclei morphological features extracted from digitalized biopsy images using computer based image analysis.
- **Combined Prediction:** uses both the image and the extracted nuclear features for a comprehensive prediction.

The model outputs a **binary classification**:

- BENIGN
- MALIGNANT
""")
            