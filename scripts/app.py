import streamlit as st
import pandas as pd
import joblib

# Load final data to extract available regions
df = pd.read_csv("data/final_data.csv")
regions = sorted(df["Region"].unique())

# Load trained model
model = joblib.load("models/ev_model.pkl")

# Title
st.title("🔌 EV Registration Demand Predictor")

st.markdown("Predict expected electric vehicle registrations based on date and location.")

# Inputs
year = st.selectbox("Select Year", sorted(df["year"].unique()))
month = st.selectbox("Select Month", list(range(1, 13)))
region = st.selectbox("Select Region", regions)

# Create input dataframe
input_data = pd.DataFrame([[year, month]], columns=["year", "month"])

# Add region columns (dummy variables)
for reg in model.feature_names_in_:
    if reg.startswith("Region_"):
        input_data[reg] = 1 if reg == f"Region_{region}" else 0

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"🔋 Predicted EV Registrations: **{int(prediction)}** vehicles")
