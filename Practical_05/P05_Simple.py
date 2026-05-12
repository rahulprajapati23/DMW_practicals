# Practical 5: Text Mining - Simple Version

import pandas as pd
import matplotlib.pyplot as plt
import random
import re
import os
from wordcloud import WordCloud
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(SCRIPT_DIR, "tweet_data.csv"))

# Normalize columns
df.columns = df.columns.str.lower()

# Find text and sentiment columns
text_col = [c for c in df.columns if 'text' in c][0]
sentiment_col = [c for c in df.columns if 'sentiment' in c][0]
id_col = [c for c in df.columns if 'id' in c][0] if any('id' in c for c in df.columns) else None

print("Columns:", df.columns.tolist())
print("Total Tweets:", len(df))
print("Unique Tweets:", df[text_col].nunique())

# Random tweet
idx = random.randint(0, len(df) - 1)
print(f"\nRandom Tweet (Index {idx}):")
print(f"ID: {df.iloc[idx].get(id_col, 'N/A')}")
print(f"Text: {df.iloc[idx][text_col]}")
print(f"Sentiment: {df.iloc[idx][sentiment_col]}")

# Sentiment counts
sentiment_counts = df[sentiment_col].str.lower().value_counts()
print(f"\nPositive Tweets: {sentiment_counts.get('positive', 0)}")
print(f"Negative Tweets: {sentiment_counts.get('negative', 0)}")

# Visualization
positive_count = sentiment_counts.get('positive', 0)
negative_count = sentiment_counts.get('negative', 0)
plt.figure(figsize=(8, 5))
plt.pie([positive_count, negative_count], labels=['Positive', 'Negative'], autopct='%1.1f%%')
plt.title("Positive vs Negative Tweets")
plt.show()

# Word clouds
positive_text = " ".join(df[df[sentiment_col].str.lower() == 'positive'][text_col].astype(str))
negative_text = " ".join(df[df[sentiment_col].str.lower() == 'negative'][text_col].astype(str))

if positive_text.strip():
    plt.figure(figsize=(10, 5))
    plt.imshow(WordCloud(width=800, height=400).generate(positive_text))
    plt.axis("off")
    plt.title("Positive Tweets Word Cloud")
    plt.show()

if negative_text.strip():
    plt.figure(figsize=(10, 5))
    plt.imshow(WordCloud(width=800, height=400).generate(negative_text))
    plt.axis("off")
    plt.title("Negative Tweets Word Cloud")
    plt.show()

# Data cleaning example
print("\nEnglish Stop Words:", sorted(list(ENGLISH_STOP_WORDS))[:10], "...")
raw_text = "Text mining is fun. Natural Language Processing helps analyze tweets!"
print(f"\nTokenized Sentences: {[s.strip() for s in re.split(r'[.!?]', raw_text) if s.strip()]}")
print(f"Tokenized Words: {re.findall(r'\b\w+\b', raw_text)}")
