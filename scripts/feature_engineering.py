import pandas as pd

# Load cleaned data
df = pd.read_csv("data/cleaned_ev_data.csv")

# Convert 'Date' again just in case
df["Date"] = pd.to_datetime(df["Date"])

# Create new features
df["year"] = df["Date"].dt.year
df["month"] = df["Date"].dt.month
df["Region"] = df["County"] + ", " + df["State"]

# Select final columns
df_final = df[["year", "month", "Region", "Electric Vehicle (EV) Total"]]

# Save processed dataset
df_final.to_csv("data/final_data.csv", index=False)

print("✅ Final dataset saved to data/final_data.csv")
