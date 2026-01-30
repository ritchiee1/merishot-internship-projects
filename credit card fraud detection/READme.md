# Credit Card Fraud Detection

## 📌 Project Requirements

This project was completed as part of the **Meritshot Data Science Internship – Task 6 (Intermediate Level Project)**.

### Internship Task Objective
The objective of this task is to evaluate the intern’s ability to:
- Solve a real-world data science problem
- Handle imbalanced datasets
- Apply appropriate machine learning techniques
- Explain results clearly and professionally
- Document the entire workflow step-by-step

### Selected Project
**Credit Card Fraud Detection (Imbalanced Machine Learning)**

Only one project was selected and completed, as required.

### Mandatory Deliverables
- ✔ End-to-end machine learning project  
- ✔ Exploratory Data Analysis with insights  
- ✔ Handling class imbalance  
- ✔ Model training and evaluation  
- ✔ Detailed documentation (PDF)  
- ✔ GitHub repository with clean README  
- ✔ LinkedIn post showcasing the project  

### Evaluation Focus
- Clarity of explanation  
- Logical project flow  
- Correct methodology  
- Business understanding  
- Professional documentation  

---

## 📖 Project Overview

Credit card fraud is a major challenge in the financial sector, causing financial losses for banks and inconvenience for customers. Fraudulent transactions are rare, making them difficult to detect using traditional rule-based systems.

This project applies **machine learning classification techniques** to detect fraudulent credit card transactions using historical transaction data. The dataset is highly imbalanced, which makes the problem more realistic and challenging.

---

## 🎯 Problem Statement

The goal of this project is to build a **classification model** that can accurately identify fraudulent credit card transactions while minimizing false alarms.

This solution helps:
- Reduce financial losses
- Improve transaction security
- Detect fraud early in real-world banking systems

---

## 📂 Dataset Description

- **Source:** Kaggle – Credit Card Fraud Detection Dataset  
- **Total Rows:** 284,807  
- **Total Columns:** 30  
- **Target Variable:** `Class`

### Feature Explanation
- `Class`  
  - `0` → Legitimate transaction  
  - `1` → Fraudulent transaction  
- `V1` to `V28`  
  - PCA-transformed numerical features for privacy protection  
- `Time`  
  - Time elapsed (in seconds) since the first transaction  
- `Amount`  
  - Transaction amount  

⚠ The dataset is **highly imbalanced**, with fraud cases representing less than 1% of all transactions.

---

## 🔍 Exploratory Data Analysis (EDA)

### Key Observations
- The class distribution is extremely skewed toward legitimate transactions.
- Fraudulent transactions occur very rarely compared to non-fraud cases.
- Transaction amounts for fraud cases vary widely, including both small and large values.
- Time-based patterns alone are not strong predictors but can add value when combined with other features.

### Why EDA Matters
EDA helped identify:
- The need for imbalance handling techniques
- Why accuracy alone is not a reliable evaluation metric
- Which features require scaling

---

## ⚙️ Data Preprocessing

The following preprocessing steps were applied:

- Removal of duplicate rows
- Feature scaling using **StandardScaler** for:
  - `Time`
  - `Amount`
- Train-test split using **stratified sampling**
- Handling class imbalance using **SMOTE (Synthetic Minority Oversampling Technique)**

These steps ensured fair model training and improved fraud detection performance.

---

## 🧠 Feature Engineering

- Target variable (`Class`) separated from features
- PCA features were retained as provided
- Scaled numerical features to improve model convergence

No artificial features were created to preserve the original dataset integrity.

---

## 🤖 Model Building

### Algorithm Used
- **Logistic Regression**

### Why Logistic Regression?
- Works well for binary classification problems
- Interpretable and efficient
- Performs reliably when combined with proper preprocessing and resampling

The model was trained using SMOTE-resampled training data.

---

## 📊 Model Evaluation

### Evaluation Metrics Used
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix

### Key Takeaways
- Accuracy alone was misleading due to class imbalance
- Recall and F1-score provided better insight into fraud detection ability
- The model showed improved detection of fraudulent transactions after resampling

---

## 🔮 Prediction

The trained model was used to predict fraud on unseen test data. Sample predictions confirmed the model’s ability to classify transactions as either fraudulent or legitimate.

---

## ✅ Final Insights and Conclusion

- Credit card fraud detection is a challenging problem due to extreme class imbalance.
- Proper data preprocessing and imbalance handling are critical for model performance.
- Logistic Regression, when combined with SMOTE, can effectively detect fraud.
- Business-focused evaluation metrics are essential for real-world deployment.

This project demonstrates a complete **end-to-end data science workflow**, from raw data to actionable insights.

---

## 🛠 Tools & Technologies

- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- Imbalanced-learn (SMOTE)  
- Jupyter Notebook  

---

## 🔗 Project Links

- ([Github](https://github.com/ritchiee1/merishot-internship-projects/tree/main/credit%20card%20fraud%20detection))  
- ([LinkedIn](https://www.linkedin.com/posts/richard-jetevu-31a648331_datascience-machinelearning-python-activity-7422991671094611969-cSto?utm_source=share&utm_medium=member_ios&rcm=ACoAAFORE8YB5cZ04TS4VwgHvW4vSnumjXmeLvA))
---
## 👤 Author
**Jetevu Richard**  
Junior Data Scientist / ML Engineer  
---