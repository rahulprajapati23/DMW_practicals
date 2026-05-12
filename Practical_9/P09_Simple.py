# Practical 9: Decision Tree (Titanic) - Simple Version

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("Dataset Info:")
print(df.head())
print(f"Shape: {df.shape}")

# Data preprocessing
df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Encode categorical features
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

print("\nCleaned Dataset:")
print(df.head())

# Features and target
X = df.drop('Survived', axis=1)
y = df['Survived']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.4f}")

# Test prediction on new passenger
import numpy as np
new_passenger = np.array([[3, 1, 25, 0, 0, 100.0]])
prediction = model.predict(new_passenger)[0]
print(f"Prediction for new passenger: {'Survived' if prediction == 1 else 'Not Survived'}")

# Analysis
print(f"\nFirst Class Survival Rate: {df[df['Pclass'] == 1]['Survived'].mean() * 100:.2f}%")
print(f"Average Age of Survivors: {df[df['Survived'] == 1]['Age'].mean():.2f}")
print(f"Average Age of Non-Survivors: {df[df['Survived'] == 0]['Age'].mean():.2f}")
