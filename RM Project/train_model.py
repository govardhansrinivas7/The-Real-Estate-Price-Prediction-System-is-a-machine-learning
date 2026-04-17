import pandas as pd
import numpy as np
import json
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("data/bengaluru_house_prices.csv")

# Basic cleaning
df = df.dropna()
df['location'] = df['location'].str.lower()

# One-hot encoding
dummies = pd.get_dummies(df['location'])
df = pd.concat([df, dummies], axis=1)
df.drop('location', axis=1, inplace=True)

X = df.drop('price', axis=1)
y = df['price']

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
with open("model/house_price_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save columns
with open("model/columns.json", "w") as f:
    json.dump({"data_columns": list(X.columns)}, f)

print("✅ Model trained and saved successfully")
