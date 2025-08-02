import pandas as pd

# Load the dataset
df = pd.read_csv("data/EV_Dataset.csv")

# Drop rows with missing County or State
df = df.dropna(subset=["County", "State"])

# Convert 'Date' to datetime format
df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

# Clean numeric columns
numeric_cols = [
    "Battery Electric Vehicles (BEVs)",
    "Plug-In Hybrid Electric Vehicles (PHEVs)",
    "Electric Vehicle (EV) Total",
    "Non-Electric Vehicle Total",
    "Total Vehicles"
]

for col in numeric_cols:
    df[col] = df[col].astype(str).str.replace(",", "")
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with NaNs in critical columns
df.dropna(subset=numeric_cols, inplace=True)

# Save cleaned data
df.to_csv("data/cleaned_ev_data.csv", index=False)

print("✅ Cleaned data saved to data/cleaned_ev_data.csv")
