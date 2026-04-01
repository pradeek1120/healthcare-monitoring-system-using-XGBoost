# Configuration for Healthcare Monitoring System

## Project Root
project_root = '/path/to/project/'

## Directory Paths

data_dir = f'{project_root}/data/'
models_dir = f'{project_root}/models/'
logs_dir = f'{project_root}/logs/'

## Data Loading Configuration

data_loading_config = {
    'batch_size': 32,
    'shuffle': True,
    'num_workers': 4,
}

## Model Hyperparameters

# XGBoost Hyperparameters
xgboost_hyperparameters = {
    'learning_rate': 0.1,
    'max_depth': 6,
    'n_estimators': 100,
}

# LightGBM Hyperparameters
lightgbm_hyperparameters = {
    'learning_rate': 0.05,
    'num_leaves': 31,
    'n_estimators': 100,
}

## Logging Setup for Google Cloud Deployment
import logging
from google.cloud import logging as cloud_logging

# Create a Cloud Logging client
cloud_client = cloud_logging.Client()
cloud_client.setup_logging()

logger = logging.getLogger('healthcare_monitoring')
logger.setLevel(logging.INFO)