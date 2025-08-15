# 🏥 AI-Powered Health Recommendation System  

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)  
[![Streamlit](https://img.shields.io/badge/Powered%20By-Streamlit-FF4B4B?logo=streamlit)](https://streamlit.io/)  

## 📂 Project Structure  

```plaintext

│
├── 📜 README.md                # Project documentation
├── 📜 requirements.txt         # List of dependencies
│
├── 🗃️ dataset/                  # Datasets for training & testing
│   ├── symptoms_dataset.csv     # Symptom-to-disease mapping data
│   ├── heart_disease_dataset.csv# Heart disease training data
│   ├── diabetes_dataset.csv     # Diabetes training data
│   └── diseases_info.csv        # General disease information
│
├── 📂 models/                   # Saved ML/DL models for different diseases
│   ├── general_health_model.pkl # General symptom-based model
│   ├── heart_disease_model.pkl  # ❤️ Heart disease prediction model
│   └── diabetes_model.pkl       # 🍬 Diabetes prediction model
│
├── 📂 src/                      # Main source code
│   ├── __init__.py              # Marks the folder as a package
│   ├── data_preprocessing.py    # Data cleaning & preparation
│   ├── train_model.py           # Model training script
│   ├── predict.py               # Prediction logic
│   └── utils.py                 # Helper functions
│
├── 📂 app/                      # Frontend interface
│   └── streamlit_app.py         # Streamlit web app for predictions
│
└── 📂 tests/                    # Unit tests for code & models
    ├── test_model.py            # Tests for ML models
    └── test_api.py              # Tests for app/API endpoints
