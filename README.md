# 🏥 Insurance Price Prediction API & Web App

This project is an end-to-end machine learning application to predict medical insurance charges based on user demographic and lifestyle data. It includes a React-based frontend and a FastAPI backend, with the trained model served through an API.

---

## 🔗 Links

**Demo Vide Link**: [[Link]([https://insurance-price-prediction-ui.vercel.app/](https://drive.google.com/file/d/1nUCRhkPML6pR4DCiG-q3gOvvaB-8LbJb/view?usp=sharing)]  
**Live URL**: [[Link](https://insurance-price-prediction-ui.vercel.app/)]  

---

## Features

- Predict insurance charges using:
  - Age
  - Gender
  - BMI
  - Number of children
  - Smoker status
  - Region
- Clean and responsive frontend UI built with **React**
- Fast, efficient backend API using **FastAPI**
- Trained machine learning model using **scikit-learn**
- Hosted on **Render**

---

## Machine Learning Model

The backend uses a machine learning model trained on the popular [Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance) dataset. The model pipeline includes:

- **Preprocessing**:
  - One-hot encoding for categorical variables
  - Standard scaling for numerical variables
- **Model**:
  - `RandomForestRegressor` with hyperparameter tuning

The pipeline is serialized using `joblib` and loaded in the FastAPI server for real-time predictions.

---

## 📦 Tech Stack

| Layer        | Tech                      |
|--------------|---------------------------|
| Frontend     | React            |
| Backend      | FastAPI, Pydantic         |
| ML Model     | scikit-learn, pandas      |
| Deployment   | Render                    |

---

## How to Run Locally

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/insurance-price-predictor.git
cd insurance-price-predictor
