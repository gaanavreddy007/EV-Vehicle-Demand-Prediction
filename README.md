# 🔌 EV Adoption Demand Prediction

This project predicts electric vehicle (EV) registration demand based on historical data using machine learning.

---

## 📊 Overview

- Uses a real-world EV registration dataset
- Performs data cleaning and feature engineering
- Trains a Random Forest model to predict future EV demand
- Includes an interactive Streamlit web app

---

## 📁 Project Structure

EV-Adoption-Demand-Prediction/
├── data/ # Raw and processed data
├── scripts/ # Python scripts (cleaning, training, app)
├── models/ # Trained ML model
├── notebooks/ # (Optional) Jupyter analysis notebook
├── README.md
├── requirements.txt

yaml
Copy
Edit

---

## ⚙️ How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
2. Run Each Step
bash
Copy
Edit
python scripts/clean_data.py
python scripts/feature_engineering.py
python scripts/train_model.py
3. Launch the Web App
bash
Copy
Edit
streamlit run scripts/app.py
🧠 ML Model
Model: Random Forest Regressor

Input: year, month, region

Output: Predicted number of EVs registered

📈 Dataset Source
Custom dataset: EV_Dataset.csv — Contains date-wise EV registration data by U.S. region.

👨‍💻 Author
Built by [Your Name] | 2025

yaml
Copy
Edit

---

## 📦 6. `requirements.txt`

> Required Python libraries for this project.

### 📁 Save this as: `EV-Adoption-Demand-Prediction/requirements.txt`

pandas
numpy
scikit-learn
joblib
streamlit
matplotlib
seaborn

yaml
Copy
Edit

---

## ❌ 7. `.gitignore`

> Excludes unnecessary files from GitHub.

### 📁 Save this as: `EV-Adoption-Demand-Prediction/.gitignore`

pycache/
*.pkl
*.pyc
.ipynb_checkpoints/
.env
.DS_Store

yaml
Copy
Edit

---