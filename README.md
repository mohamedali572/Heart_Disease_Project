# Heart Disease Project

Project description and setup instructions.

# Heart Disease Prediction Project

A comprehensive machine learning project for **heart disease prediction**, covering the full ML pipeline:
- Data preprocessing
- Feature engineering (encoding, scaling)
- Dimensionality reduction (PCA)
- Feature selection (RFE)
- Supervised and unsupervised models
- Hyperparameter tuning
- Web UI with Streamlit

---

## Dataset

The project uses the **Heart Disease Dataset** from the UCI Machine Learning Repository:  
[https://archive.ics.uci.edu/dataset/45/heart+disease](https://archive.ics.uci.edu/dataset/45/heart+disease)

---

## Features

- **Data Preprocessing:** Handle missing values, one-hot encoding, feature scaling.  
- **Dimensionality Reduction:** PCA to retain 95% variance.  
- **Feature Selection:** Recursive Feature Elimination (RFE) to choose top features.  
- **Supervised Learning Models:** Logistic Regression, Decision Tree, Random Forest, SVM.  
- **Unsupervised Learning:** KMeans clustering for exploratory insights.  
- **Hyperparameter Tuning:** GridSearchCV to optimize model performance.  
- **Web Interface:** Streamlit app for user-friendly predictions.  

---

## Project Structure


Heart_Disease_Project/
│── data/
│ └── heart_disease.csv # Dataset file
│── notebooks/
│ ├── 01_data_preprocessing.ipynb # Cleaning & preprocessing
│ ├── 02_pca_analysis.ipynb # PCA analysis
│ ├── 03_feature_selection.ipynb # Feature selection with RFE
│ ├── 04_supervised_learning.ipynb# Training supervised models
│ ├── 05_unsupervised_learning.ipynb # KMeans clustering
│ └── 06_hyperparameter_tuning.ipynb # GridSearchCV tuning
│── models/
│ └── final_model.pkl # Best trained model
│── ui/
│ └── app.py # Streamlit UI
│── deployment/
│ └── ngrok_setup.txt # Instructions for tunneling
│── results/
│ └── evaluation_metrics.txt # Model evaluation metrics
│── README.md
│── requirements.txt
│── .gitignore


