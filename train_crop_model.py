# train_crop_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# ✅ Load dataset (make sure the CSV is in the root folder)
df = pd.read_csv('Crop_recommendation_with_fertilizer.csv')

# ✅ Features & Target
X = df.drop(['label', 'fertilizer'], axis=1)
y = df['label']

# ✅ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Train Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ✅ Evaluate model (optional)
accuracy = model.score(X_test, y_test)
print(f"✅ Model Accuracy: {accuracy * 100:.2f}%")

# ✅ Save model to ml_models/
os.makedirs('ml_models', exist_ok=True)
joblib.dump(model, 'ml_models/crop_model.pkl')

print("✅ Model saved at: ml_models/crop_model.pkl")
