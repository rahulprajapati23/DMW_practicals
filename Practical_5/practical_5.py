# Practical 5: Text Mining (tweet_data.csv)
# This file contains the analysis and plotting code extracted from the source.

import pandas as pd
import matplotlib.pyplot as plt
import random
import re
import os
from wordcloud import WordCloud
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Update the path to your local file
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(SCRIPT_DIR, "tweet_data.csv")


def main():
    df = pd.read_csv(FILE_PATH)

    # Normalize column names
    df.columns = df.columns.str.lower()
    print("Columns in Dataset:", df.columns.tolist())

    text_col = None
    sentiment_col = None
    id_col = None

    for col in df.columns:
        if 'text' in col:
            text_col = col
        if 'sentiment' in col:
            sentiment_col = col
        if col == 'id' or 'id' in col:
            id_col = col

    print("Detected Text Column:", text_col)
    print("Detected Sentiment Column:", sentiment_col)
    print("Detected ID Column:", id_col)

    if text_col is None or sentiment_col is None:
        raise Exception("Required columns not found in dataset.")

    total_tweets = len(df)
    unique_tweets = df[text_col].nunique()

    print("\nTotal Tweets:", total_tweets)
    print("Unique Tweets:", unique_tweets)

    # Random tweet sample
    random_index = random.randint(0, total_tweets - 1)
    tweet_row = df.iloc[random_index]

    print("\nRandom Tweet by Index:", random_index)
    print("Tweet ID:", tweet_row.get(id_col, 'N/A'))
    print("Text:", tweet_row[text_col])
    print("Sentiment:", tweet_row[sentiment_col])

    # Positive / Negative counts
    sentiment_counts = df[sentiment_col].str.lower().value_counts()
    positive_count = sentiment_counts.get('positive', 0)
    negative_count = sentiment_counts.get('negative', 0)

    print("\nPositive Tweets:", positive_count)
    print("Negative Tweets:", negative_count)

    # Visualization examples (will display when run in an environment with a display)
    total_sentiments = positive_count + negative_count
    positive_pct = (positive_count / total_sentiments) * 100 if total_sentiments else 0
    negative_pct = (negative_count / total_sentiments) * 100 if total_sentiments else 0

    plt.figure()
    plt.pie([positive_pct, negative_pct], labels=['Positive', 'Negative'], autopct='%1.1f%%')
    plt.title("Percentage of Positive vs Negative Tweets")
    plt.show()

    plt.figure()
    plt.bar(['Positive', 'Negative'], [positive_count, negative_count])
    plt.title("Count of Positive vs Negative Tweets")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Tweets")
    plt.show()

    positive_text = " ".join(df[df[sentiment_col].str.lower() == 'positive'][text_col].astype(str))
    if positive_text.strip():
        wordcloud_pos = WordCloud(width=800, height=400).generate(positive_text)
        plt.figure()
        plt.imshow(wordcloud_pos)
        plt.axis("off")
        plt.title("Word Cloud - Positive Tweets")
        plt.show()

    negative_text = " ".join(df[df[sentiment_col].str.lower() == 'negative'][text_col].astype(str))
    if negative_text.strip():
        wordcloud_neg = WordCloud(width=800, height=400).generate(negative_text)
        plt.figure()
        plt.imshow(wordcloud_neg)
        plt.axis("off")
        plt.title("Word Cloud - Negative Tweets")
        plt.show()

    # Data cleaning examples
    retweets = df[df[text_col].astype(str).str.startswith("RT", na=False)]
    if not retweets.empty:
        random_retweet = retweets.sample(1).iloc[0]
        clean_retweet = re.sub(r'^RT\s+', '', random_retweet[text_col])
        print("\nOriginal Retweet:", random_retweet[text_col])
        print("After Removing RT:", clean_retweet)

    random_tweet = df.sample(1).iloc[0]
    clean_text = re.sub(r'@\w+', '', str(random_tweet[text_col]))
    clean_text = re.sub(r'#\w+', '', clean_text)
    print("\nOriginal Tweet:", random_tweet[text_col])
    print("After Removing Hashtags & Handles:", clean_text.strip())

    emoji_tweet = df[df[text_col].astype(str).str.contains(r'[^\x00-\x7F]+', na=False)]
    if not emoji_tweet.empty:
        sample_emoji = emoji_tweet.sample(1).iloc[0]
        text_with_emoji = sample_emoji[text_col]
        emoji_replaced = re.sub(r'[^\x00-\x7F]+', ' EMOJI ', text_with_emoji)
        print("\nTweet with Emoji:", text_with_emoji)
        print("After Replacing Emoji:", emoji_replaced)

    print("\nEnglish Stop Words:")
    print(sorted(list(ENGLISH_STOP_WORDS)))

    raw_text = "Text mining is fun. Natural Language Processing helps analyze tweets!"
    sentences = re.split(r'[.!?]', raw_text)
    words = re.findall(r'\b\w+\b', raw_text)

    print("\nTokenized Sentences:")
    print([s.strip() for s in sentences if s.strip()])

    print("\nTokenized Words:")
    print(words)

if __name__ == '__main__':
    main()
