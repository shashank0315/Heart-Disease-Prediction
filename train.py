import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Sample training dataset (Age, Cholesterol, Blood Pressure)
X = np.array([[25, 180, 120], [45, 200, 130], [60, 220, 140], [50, 210, 135]])
y = np.array([0, 1, 1, 1])  # 0 = No heart disease, 1 = Heart disease

# Train a simple model
model = RandomForestClassifier()
model.fit(X, y)

# Save the trained model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved as model.pkl")
