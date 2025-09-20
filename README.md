
## Healthcare Monitoring System using XGBoost

This project develops a machine learning model to predict the likelihood of a patient having hypertension based on various health metrics. The goal is to build a highly accurate system for early detection and monitoring.

**Key aspects of the project:**

*   **Data Loading and Preprocessing:** The project starts by loading a synthetic patient healthcare monitoring dataset. The data is checked for missing values and categorical features are one-hot encoded to prepare it for model training.
*   **Model Selection:** Several classification models were considered, including Logistic Regression, LightGBM, and XGBoost, given the binary classification nature of the problem (predicting hypertension or not).
*   **Initial Training and Evaluation:** The selected models were trained on the preprocessed data and evaluated using key metrics like accuracy, precision, recall, and F1-score.
*   **Hyperparameter Tuning:** To enhance model performance, hyperparameter tuning was performed on the LightGBM and XGBoost models using GridSearchCV with F1-score as the scoring metric.
*   **Final Evaluation:** The tuned models were evaluated on the test set, and their performance was compared to the initial models. The tuned LightGBM model demonstrated the best performance.
*   **Model Saving and Usage:** The best performing model (tuned LightGBM) was saved using `joblib` for future use. A demonstration of loading the saved model and making predictions on new data is included.
*   **Model Interpretation:** The feature importances of the best model were analyzed to understand which health metrics are most influential in predicting hypertension. The analysis revealed that Heart Rate, Systolic Blood Pressure, and Diastolic Blood Pressure are the most important features.

This project provides a comprehensive workflow for building and evaluating a healthcare monitoring system using advanced machine learning techniques, with a focus on achieving high accuracy and interpretability.
