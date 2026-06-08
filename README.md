# 🍷 End-to-End Data Science Project: Wine Quality Prediction

## 📌 Project Overview

This project demonstrates a complete End-to-End Machine Learning pipeline for predicting wine quality using physicochemical properties of wine samples. The project follows industry-standard MLOps practices, including modular pipeline development, configuration management, experiment tracking, and model evaluation.

The machine learning model used in this project is **ElasticNet Regression**, which combines the strengths of both Lasso (L1) and Ridge (L2) regularization techniques.

---

## 🚀 Project Workflow

### Machine Learning Pipeline

The project consists of the following stages:

1. **Data Ingestion**

   * Load the dataset from source.
   * Store raw data locally for further processing.

2. **Data Validation**

   * Validate dataset schema.
   * Check missing values, data types, and column consistency.

3. **Data Transformation**

   * Feature engineering.
   * Data preprocessing.
   * Train-test split.
   * Data scaling and preparation.

4. **Model Training**

   * Train the ElasticNet Regression model.
   * Hyperparameter tuning using configurable parameters.

5. **Model Evaluation**

   * Evaluate model performance using regression metrics:

     * RMSE
     * MAE
     * R² Score
   * Track experiments using:

     * MLflow
     * DagsHub

---

## 📂 Project Structure

```bash
├── config
│   ├── config.yaml
│   ├── schema.yaml
│   └── params.yaml
│
├── src
│   ├── wine_quality
│   │   ├── components
│   │   ├── config
│   │   ├── constants
│   │   ├── entity
│   │   ├── pipeline
│   │   └── utils
│
├── artifacts
│
├── research
│
├── logs
│
├── main.py
├── app.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Workflow Implementation

The project development follows these steps:

1. Update `config.yaml`
2. Update `schema.yaml`
3. Update `params.yaml`
4. Update Entity Classes
5. Update Configuration Manager
6. Update Components
7. Update Pipeline
8. Update `main.py`

---

## 📊 Dataset Information

### Wine Quality Dataset

The dataset contains physicochemical properties of wine samples and their corresponding quality scores.

### Features

* Fixed Acidity
* Volatile Acidity
* Citric Acid
* Residual Sugar
* Chlorides
* Free Sulfur Dioxide
* Total Sulfur Dioxide
* Density
* pH
* Sulphates
* Alcohol

### Target Variable

* Quality Score

---

## 🤖 Model Used

### ElasticNet Regression

ElasticNet combines:

* **L1 Regularization (Lasso)** for feature selection.
* **L2 Regularization (Ridge)** for handling multicollinearity.

Advantages:

* Reduces overfitting.
* Performs automatic feature selection.
* Handles correlated features effectively.

---

## 📈 Evaluation Metrics

The following metrics are used to evaluate model performance:

### Mean Absolute Error (MAE)

Measures the average absolute difference between predicted and actual values.

### Root Mean Squared Error (RMSE)

Measures prediction error while giving higher weight to large errors.

### R² Score

Measures how well the model explains variance in the target variable.

---

## 🔍 Experiment Tracking

### MLflow

MLflow is used for:

* Parameter tracking
* Metric logging
* Model versioning
* Experiment comparison

### DagsHub

DagsHub is integrated with MLflow for:

* Remote experiment tracking
* Model management
* Collaboration and reproducibility

---

## 🛠️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/wine-quality-prediction.git
cd wine-quality-prediction
```

### Create Virtual Environment

```bash
conda create -n wine python=3.10 -y
conda activate wine
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Execute Training Pipeline

```bash
python main.py
```

### Run Application

```bash
python app.py
```

---

## 📋 Configuration Files

### config.yaml

Contains:

* Data source paths
* Artifact locations
* Pipeline configuration

### schema.yaml

Contains:

* Dataset schema
* Column definitions
* Validation rules

### params.yaml

Contains:

* ElasticNet hyperparameters
* Training parameters

---

## 📌 Key Features

✅ Modular project structure

✅ Reproducible ML pipeline

✅ Configuration-driven development

✅ Data validation framework

✅ Experiment tracking with MLflow

✅ DagsHub integration

✅ Scalable architecture for production deployment

---

## 🔮 Future Improvements

* Hyperparameter Optimization
* Docker Containerization
* CI/CD Pipeline Integration
* Model Deployment using Flask/FastAPI
* Monitoring and Drift Detection
* Cloud Deployment (AWS/Azure/GCP)

---

## 📚 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* MLflow
* DagsHub
* YAML
* Flask
* Git & GitHub

---

## 👨‍💻 Author

Developed as an End-to-End Machine Learning project demonstrating MLOps best practices, pipeline automation, and experiment tracking for Wine Quality Prediction.

---

### ⭐ If you found this project useful, consider giving it a star on GitHub.
