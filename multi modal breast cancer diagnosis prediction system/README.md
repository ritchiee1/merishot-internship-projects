# 🧬 Multimodal Breast Cancer Diagnosis Prediction System

This project implements a **Multimodal Breast Cancer Diagnosis System** combining:

- 🖼 **Breast Cancer Histopathology  Images**
- 🧬 **Cell Nuclear Morphological Features (30 features)**

The system predicts **Benign** or **Malignant** breast cancer using either modality independently or both together.

---

## 📌 Problem Statement

Early detection of breast cancer is crucial. Traditional approaches often use either imaging or nuclear features separately, reducing diagnostic accuracy.  

This project builds a multimodal model that:

- Analyzes histopathology images  
- Uses nuclear morphological features  
- Combines both for improved accuracy  
- Supports image-only or feature-only predictions  

---

## 📂 Dataset Description

**Source:** BreakHis Dataset (40X magnification)  

- 🖼 **Images:** 1,995 histopathology images  
  - Benign: 1,011  
  - Malignant: 984  
- 🧬 **Morphological Features:** 30 nuclear measurements per sample  
- 👤 **Patients:** Unique patient IDs  

**Folder Structure:**
* image_binary/
* ├── benign
* └── malignant


**Feature Columns:** 30 nuclear morphology features, e.g., area, perimeter, circularity, eccentricity.

---

## ⚙️ Project Workflow

1. Data Loading  
2. Data Preprocessing  
3. Train/Validation Split  
4. Multimodal Model Architecture  
5. Model Training  
6. Model Evaluation  
7. Prediction on New Data  
8. Deployment via Streamlit  
9. Insights & Conclusion  

---

## 🧹 Data Loading & Preprocessing

- Images loaded via `tensorflow.keras.preprocessing.image`  
- Features loaded using `pandas` & scaled with `StandardScaler`  
- Patient-level split to avoid leakage  

Example shapes:
* Images: (1995, 224, 224, 3)
* Features: (1995, 30)
* Train Images: (1570, 224, 224, 3)
* Validation Images: (425, 224, 224, 3)

---

## 🏗 Model Architecture

### Image Branch (CNN)

- Conv2D + MaxPooling layers  
- GlobalAveragePooling2D  
- Dense layer (128 neurons, ReLU)

### Feature Branch (MLP)

- Dense layers (64 → 32 neurons, ReLU)

### Combined Branch

- Concatenate CNN & MLP outputs  
- Dense → Dropout → Dense → Sigmoid output  

**Compiled with:** Adam, Binary Crossentropy, Accuracy

---

## 🚀 Model Training

- Epochs: 10  
- Batch size: 16  
- Validation monitoring  

Example Training Output:
Uploaded Image: benign_test_image.png
Uploaded Features: CSV with 30 columns
Prediction: BENIGN



---

## 🌐 Streamlit Deployment

- File Upload: Image (.png/.jpg) and/or CSV with features  
- Mode selection: Image Only / Features Only / Combined  
- Columns for input/output  
- Styled with headers, colored metrics, and professional layout  


---

## 💾 Model & Scaler Persistence

- `breast_cancer_multimodal_model.h5`  
- `clinical_scaler.pkl`  

Fast inference without retraining.

---

## 📌 Key Insights

- CNN extracts visual patterns in nuclei  
- Morphological features improve interpretability  
- Multimodal predictions outperform single modality  
- Flexible input allows image-only or feature-only predictions  

---

## 🛠 Technologies Used

- Python  
- TensorFlow / Keras  
- NumPy & Pandas  
- Scikit-learn  
- OpenCV & PIL  
- Streamlit  
- Joblib  
- Google Colab

---

## 📈 Future Improvements

- Attention-based CNN for nuclei  
- Larger dataset integration  
- Docker/cloud-based Streamlit deployment  
- Feature importance visualization  
- Multi-class histopathology classification  

---

## 📜 License

The dataset is publicly available for research.  
This project uses MIT License for educational/research purposes.
