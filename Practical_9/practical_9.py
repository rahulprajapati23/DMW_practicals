# Practical 9: Decision Tree (Titanic)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Basic inspection
print("Initial Data:")
print(df.head())
print(df.info())

# Note: This file contains the initial steps for building a Decision Tree classifier.
# Further preprocessing (handling missing values, encoding categorical variables)
# and model training should be implemented as needed.
