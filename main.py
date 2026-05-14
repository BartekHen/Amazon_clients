import bz2
import pandas as pd
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob
from tqdm import tqdm

def load_data(filepath, limit=5000):
    opinie = []
    print(f"Pobieranie {limit} opinii z pliku...")
    
    with bz2.open(filepath, 'rt', encoding='utf-8') as f:
        for i, line in tqdm(enumerate(f), total=limit, desc="Wczytywanie"):
            if i >= limit:
                break
            label, text = line.strip().split(' ', 1)
            rating = int(label.replace('__label__', ''))
            opinie.append({'rating': rating, 'review_text': text})
            
    return pd.DataFrame(opinie)

def clean_text_basic(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    return text

def process_data(df):
    print("\nRozpoczynam przetwarzanie tekstu i inżynierię cech...")
    
    tqdm.pandas(desc="Przetwarzanie wierszy")
    
    df['word_count'] = df['review_text'].apply(lambda x: len(str(x).split()))
    df['char_count'] = df['review_text'].apply(lambda x: len(str(x)))
    df['exclamation_count'] = df['review_text'].apply(lambda x: str(x).count('!'))
    
    df['sentiment_score'] = df['review_text'].progress_apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    
    df['clean_review'] = df['review_text'].progress_apply(clean_text_basic)
    
    return df

def generate_wordclouds(df):
    print("\nGenerowanie chmur słów...")
    
    custom_stopwords = set(STOPWORDS)
    custom_stopwords.update([
        'product', 'use', 'one', 'get', 'would', 'also', 'really', 'good', 
        'book', 'movie', 'read', 'time', 'even', 'much'
    ])

    unique_ratings = sorted(df['rating'].unique())
    if len(unique_ratings) >= 2:
        neg_rating = unique_ratings[0]       
        pos_rating = unique_ratings[-1]      
    else:
        neg_rating = pos_rating = unique_ratings[0]

    positive_text = ' '.join(df[df['rating'] == pos_rating]['clean_review'])
    negative_text = ' '.join(df[df['rating'] == neg_rating]['clean_review'])

    if positive_text.strip():
        wordcloud_pos = WordCloud(width=900, height=400, background_color='white',
                                 stopwords=custom_stopwords).generate(positive_text)
        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud_pos, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Najczęstsze słowa w opiniach z oceną {pos_rating}')
        plt.savefig('wordcloud_positive.png', bbox_inches='tight')
        plt.close()
        print(" -> Zapisano: wordcloud_positive.png")

    if negative_text.strip():
        wordcloud_neg = WordCloud(width=900, height=400, background_color='black',
                                 colormap='Reds', stopwords=custom_stopwords).generate(negative_text)
        plt.figure(figsize=(12, 6))
        plt.imshow(wordcloud_neg, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Najczęstsze słowa w opiniach z oceną {neg_rating}')
        plt.savefig('wordcloud_negative.png', bbox_inches='tight')
        plt.close()
        print(" -> Zapisano: wordcloud_negative.png")

def export_data(df, filename='opinie_klientow.csv'):
    cols_to_export = [
        'rating', 'sentiment_score', 'word_count', 
        'char_count', 'exclamation_count', 'clean_review'
    ]
    df[cols_to_export].to_csv(filename, index=False)
    print(f"\nSukces! Zapisano gotowy zbiór danych do pliku: {filename}")

if __name__ == "__main__":
    df_raw = load_data('train.ft.txt.bz2', limit=5000)
    
    print("\nRozkład ocen w pobranej próbce:")
    print(df_raw['rating'].value_counts().sort_index())
    
    df_processed = process_data(df_raw)
    
    generate_wordclouds(df_processed)
    
    export_data(df_processed)
