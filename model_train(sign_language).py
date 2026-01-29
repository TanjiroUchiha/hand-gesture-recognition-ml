import os
import numpy as np
import glob
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

X, y = [], []

for file in glob.glob("data/*.csv"):
    label = os.path.basename(file).replace(".csv", "")
    data = np.loadtxt(file, delimiter=",")
    X.extend(data)
    y.extend([label]*len(data))

X = np.array(X)
y = np.array(y)

print(f"Loaded {len(X)} samples from {len(set(y))} gestures.")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)

acc = model.score(X_test, y_test)
print(f"✅ Model trained successfully. Accuracy: {acc*100:.2f}%")

pickle.dump(model, open("model.pkl", "wb"))
print("Model saved as model.pkl")