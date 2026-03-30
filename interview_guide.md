# Retail Sales Prediction Engine
## Technical Documentation & Interview Guide

---

### 1. Project Overview
This is an end-to-end Machine Learning project designed to forecast retail item sales across multiple store outlets. The application predicts the future sales of a product based on its attributes (like weight, MRP, fat content) and the outlet's characteristics (like size, location type).

### 2. How Does the Project Work?
The project follows a modular, production-ready machine learning pipeline:

- **Data Ingestion (`data_ingestion.py`)**: Responsible for reading the raw dataset, splitting it into training and testing sets, and persisting them into an `artifacts` folder for tracking.
- **Data Transformation (`data_transformation.py`)**: Cleans and preprocesses the raw data. 
  - *Numerical features* are processed using SimpleImputer (to handle missing values) and StandardScaler (for normalization).
  - *Categorical features* are processed using SimpleImputer (most frequent) and OneHotEncoder.
  - The finalized scaling pipeline is saved as `preprocessor.pkl`.
- **Model Training (`model_trainer.py`)**: Evaluates multiple regression models (Random Forest, Decision Tree, Gradient Boosting, Linear Regression, XGBoost, CatBoost, AdaBoost). It performs automated hyperparameter tuning via Grid Search and selects the highest performing model based on its R2 score, saving it as `model.pkl`.
- **Prediction Pipeline (`predict_pipeline.py`)**: Consumes incoming payload requests, converts the payload into a pandas DataFrame, applies the exact same transformation steps via the saved `preprocessor.pkl`, and passes it to `model.pkl` to return the predicted sales figure.
- **Web Application (`app.py`)**: A Flask-based frontend with a modern aesthetic that serves as the interface between the user and the predictive ML engine.

### 3. What Does It Contain? (Project Structure)
- **`src/`**: The main module directory containing exception handling (`exception.py`), custom logging (`logger.py`), and utility functions.
- **`src/components/`**: Core machine learning modules handling Ingestion, Transformation, and Training.
- **`src/pipeline/`**: Execution pipelines for training the model and predicting unseen data.
- **`artifacts/`**: System-generated folder storing the outputs of our ML pipeline (models, preprocessors, cleaned data).
- **`templates/`**: HTML/CSS frontend templates (`index.html`, `home.html`).
- **`notebook/`**: Jupyter notebooks detailing the exploratory data analysis (EDA) and initial model experiments.
- **`app.py`**: The Flask entry point.

### 4. Technologies & Tools Used
- **Language**: Python 3.8+
- **Machine Learning**: Scikit-Learn, XGBoost, CatBoost
- **Data Manipulation**: Pandas, NumPy
- **Web Framework**: Flask
- **Frontend**: HTML5, Vanilla CSS (Modern Interface)
- **Version Control**: Git & GitHub

---

### 5. Potential Interview Questions (And How to Answer Them)

**Q1: How did you prevent Data Leakage in your pipeline?**
*Answer:* I separated the dataset into training and testing sets during the Data Ingestion phase *before* any transformation was applied. The data transformer (StandardScaler and Imputer) was `fit` ONLY on the training data, and then used to `transform` both the train and test sets, ensuring no testing data information leaked into the model during training.

**Q2: Why did you evaluate multiple tree-based models (XGBoost, CatBoost, Random Forest) instead of just using Linear Regression?**
*Answer:* Retail sales data often has complex, non-linear relationships and high cardinality features (like outlet identifiers and item categories). Tree-based ensemble algorithms like Random Forest and Gradient Boosters tend to automatically capture non-linearities and interactions between features much better than simple linear models. I tested multiple algorithms to let the data dictate the best performer based on the highest R2 score.

**Q3: What is the purpose of pickling the `preprocessor.pkl` file alongside the `model.pkl`?**
*Answer:* Productionizing a model requires that any new user input goes through the exact same transformations as the training data (e.g., standardizing using the exact same mean and standard deviation). By saving the preprocessor object, we guarantee preprocessing consistency during prediction time in `predict_pipeline.py`.

**Q4: How did you handle errors and track operations during the pipeline execution?**
*Answer:* I built custom exception handling (`src/exception.py`) that uses the `sys` module to extract exact line numbers and file names where an error occurs. I paired this with a centralized custom logger (`src/logger.py`) that writes all pipeline steps directly to log files, ensuring robust debugging and monitoring in production.

**Q5: What challenges did you face when handling the deployment pipeline folder (`.ebextensions`)?**
*Answer:* Configuring the environment for AWS Elastic Beanstalk (via `.ebextensions/python.config`) required specifying exactly where the WSGI application lives. For this project, setting `WSGIPath: app:application` maps the Elastic Beanstalk entry point to our Flask `application` variable inside `app.py`.
