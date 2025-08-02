import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib
import os

# Load final dataset
df = pd.read_csv("data/final_data.csv")

# One-hot encode 'Region'
df_encoded = pd.get_dummies(df, columns=["Region"])

# Split features and target
X = df_encoded.drop("Electric Vehicle (EV) Total", axis=1)
y = df_encoded["Electric Vehicle (EV) Total"]

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"✅ Model trained. MAE: {mae:.2f} EVs")

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/ev_model.pkl")
print("✅ Model saved to models/ev_model.pkl")
