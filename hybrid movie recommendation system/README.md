# 🎬 Hybrid Movie Recommendation System

This project implements a **Hybrid Movie Recommendation System** using the MovieLens 1M dataset.

It combines:

- **Collaborative Filtering (Matrix Factorization)**
- **Content-Based Filtering (Cosine Similarity)**

The goal is to generate personalized movie recommendations while addressing issues like **data sparsity** and **cold-start problems**.

---

## 📌 Problem Statement

Streaming platforms such as Netflix and Amazon Prime host thousands of movies. Without intelligent recommendation systems, users may struggle to find relevant content, leading to poor user experience.

This project builds a hybrid recommendation model that:

- Learns user preferences from historical ratings  
- Uses movie genre similarity  
- Combines both approaches for improved personalization  

---

## 📂 Dataset Description

**Source:** MovieLens 1M (GroupLens)

- 👤 6,040 Users  
- 🎬 3,706 Movies  
- ⭐ 1,000,209 Ratings (1–5 scale)  

### Files Used

- `users.dat` – User demographics  
- `movies.dat` – Movie titles and genres  
- `ratings.dat` – User ratings  

The dataset is highly **sparse**, making it suitable for testing hybrid recommendation systems.

---

## ⚙️ Project Workflow

1. Data Loading  
2. Data Preprocessing  
3. Feature Engineering  
4. Model Architecture  
5. Model Training  
6. Model Evaluation  
7. Hybrid Recommendation  
8. Deployment  
9. Insights & Conclusion  

---

## 🧹 Data Loading and Preprocessing

- Loaded datasets using `pandas`
- Merged ratings with movie metadata
- Created a **User–Item interaction matrix**
- Filled missing ratings with 0 for matrix factorization

---

## 🧠 Feature Engineering

### Content-Based Features

- Split movie genres using `|`
- Encoded genres using `MultiLabelBinarizer`
- Computed **Cosine Similarity** between movies

### Collaborative Features

- Constructed rating matrix
- Applied **Matrix Factorization** using NumPy

---

## 🏗 Model Architecture

### 1️⃣ Collaborative Filtering (Matrix Factorization)

The rating matrix **R** is factorized into:

- `P` → User latent feature matrix  
- `Q` → Movie latent feature matrix  

Predicted rating:

R̂_ij = P_i · Q_j^T

Optimization is performed using **Gradient Descent with Regularization**.

---

## 🚀 Model Training

**Hyperparameters used:**

- Latent factors (k): 20  
- Iterations (steps): 50  
- Learning rate (alpha): 0.002  
- Regularization (beta): 0.02  

Training reduces prediction error over iterations.

Example loss output:

Step 0 → 1328145.3421  
Step 40 → 677275.4211  

---

## 📊 Model Evaluation

Evaluation metric: **Root Mean Squared Error (RMSE)**

Collaborative Filtering RMSE:

0.7429

Lower RMSE indicates better prediction accuracy.

---

## 🔀 Hybrid Recommendation

Final prediction combines collaborative and content-based scores:

final_score = α × collaborative_score + (1 - α) × content_score

Where:
- α controls balance between both models.

This improves personalization and helps handle cold-start cases.

---

## 💾 Model Deployment

Matrices are saved using `pickle`:

- `P_matrix.pkl`
- `Q_matrix.pkl`
- `genre_matrix.pkl`

This allows fast inference without retraining the model.

---

## 📌 Key Insights

- Matrix factorization works efficiently using NumPy.
- Content-based filtering improves cold-start recommendations.
- Hybrid systems balance user behavior and movie similarity.
- RMSE shows good predictive performance.
- Precomputed recommendations simulate production-ready deployment.

---

## 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Pickle
- Google Colab

---

## 📈 Future Improvements

- Implement Surprise library SVD for comparison
- Add implicit feedback handling
- Deploy as a web API (Flask/FastAPI)
- Add user interface for real-time recommendations

---

## 📜 License

This project uses the MovieLens dataset provided by GroupLens Research.
