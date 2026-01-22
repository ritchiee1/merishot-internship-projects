# Loan Eligibility Classification Project

## Overview
This project focuses on building a **machine learning classification model** to predict loan eligibility based on applicant information.  
The goal is to analyze the data, perform preprocessing, train classification models, evaluate their performance, and extract meaningful insights.

---

## Dataset
The dataset contains applicant-level information such as:

- Gender  
- Marital Status  
- Education  
- Employment Status  
- Dependents  
- Applicant Income  
- Co-applicant Income  
- Loan Amount  
- Loan Term  
- Credit History  
- Property Area  

**Target Variable:**  
- `Loan_Status` (Approved / Not Approved)

---

## Data Preprocessing
The following preprocessing steps were applied:

- Handling missing values  
- Encoding categorical variables  
- Converting `Dependents = 3+` into a numerical format  
- Feature selection to retain the most relevant predictors  
- No feature scaling was applied since the problem is classification-based and tree models were used

---

## Exploratory Data Analysis (EDA)
Key visual analyses include:

- Distribution of numerical features  
- Loan approval rates across categorical variables  
- Relationship between income, loan amount, and approval status  

**Outliers:**  
- Outliers were identified but not capped to preserve real-world variability

---

## Modeling
Two classification models were trained:

- **Logistic Regression**
- **Random Forest Classifier**

### Hyperparameter Tuning
Hyperparameter tuning was performed using grid search to optimize model performance.

---

## Model Evaluation
The models were evaluated using:

- Accuracy  
- Precision  
- Recall  
- F1-score  
- Confusion Matrix  
- Classification Report  

The Random Forest model showed stronger performance due to its ability to capture non-linear relationships in the data.

---

## Key Insights
- Credit history is a strong predictor of loan approval  
- Applicant income and loan amount significantly influence outcomes  
- Tree-based models handle this dataset better than linear models  
- Feature selection improved model stability and interpretability  

---

## Conclusion
This project demonstrates a complete machine learning workflow for a classification task, including preprocessing, modeling, evaluation, and insights generation.  
The final model can assist financial institutions in making data-driven loan approval decisions.

---

## Tools & Libraries
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  

---

## Author
Jetevu Richard