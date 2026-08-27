import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = 'opinie_klientow.csv'
IMAGES_DIR = 'docs/images'

def label_name(rating):
    return 'Negative (1)' if rating == 1 else 'Positive (2)'

def plot_sentiment_by_rating(df):
    avg_sentiment = df.groupby('rating')['sentiment_score'].mean()
    labels = [label_name(r) for r in avg_sentiment.index]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, avg_sentiment.values, color='steelblue')
    plt.axhline(0, color='gray', linewidth=0.8)
    plt.ylabel('Average sentiment score')
    plt.title('Average sentiment score by rating label')
    plt.tight_layout()
    plt.savefig(f'{IMAGES_DIR}/sentiment_by_rating.png')
    plt.close()
    print(f" -> Saved: {IMAGES_DIR}/sentiment_by_rating.png")

def plot_wordcount_by_label(df):
    avg_word_count = df.groupby('rating')['word_count'].mean()
    labels = [label_name(r) for r in avg_word_count.index]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, avg_word_count.values, color='steelblue')
    plt.ylabel('Average word count')
    plt.title('Average review length by rating label')
    plt.tight_layout()
    plt.savefig(f'{IMAGES_DIR}/wordcount_by_label.png')
    plt.close()
    print(f" -> Saved: {IMAGES_DIR}/wordcount_by_label.png")

if __name__ == "__main__":
    os.makedirs(IMAGES_DIR, exist_ok=True)
    df = pd.read_csv(DATA_FILE)

    plot_sentiment_by_rating(df)
    plot_wordcount_by_label(df)
