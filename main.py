import bz2
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import re





opinie = []
with bz2.open('train.ft.txt.bz2', 'rt', encoding='utf-8') as f:
    for i, line in enumerate(f):
        label, text = line.strip().split(' ', 1)
        rating = int(label.replace('__label__', ''))
        opinie.append({'rating': rating, 'review_text': text})
        if i == 999:
            break

df = pd.DataFrame(opinie)


print("Rozkład ocen w zbiorze:")
print(df['rating'].value_counts().sort_index())


unique_ratings = sorted(df['rating'].unique())
if len(unique_ratings) >= 2:
    neg_rating = unique_ratings[0]       
    pos_rating = unique_ratings[-1]      
else:
    neg_rating = pos_rating = unique_ratings[0]

print(f"\nUżyte progi: negatywne = {neg_rating}, pozytywne = {pos_rating}")


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  
    text = re.sub(r'\d+', '', text)      
    return text

df['clean_review'] = df['review_text'].apply(clean_text)


custom_stopwords = set(STOPWORDS)
custom_stopwords.update([
    'product', 'use', 'one', 'get', 'would', 'also', 'really', 'good'
])


positive_text = ' '.join(df[df['rating'] == pos_rating]['clean_review'])
negative_text = ' '.join(df[df['rating'] == neg_rating]['clean_review'])


if positive_text.strip():
    wordcloud_pos = WordCloud(width=900, height=400, background_color='white',
                             stopwords=custom_stopwords).generate(positive_text)
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud_pos, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Najczęstsze słowa w opiniach z oceną {pos_rating}')
    plt.savefig('wordcloud_positive.png')
    plt.show()
    print("Wygenerowano plik: wordcloud_positive.png")
else:
    print("Brak pozytywnych opinii dla wskazanego progu ocen!")


if negative_text.strip():
    wordcloud_neg = WordCloud(width=900, height=400, background_color='black',
                             colormap='Reds', stopwords=custom_stopwords).generate(negative_text)
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud_neg, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Najczęstsze słowa w opiniach z oceną {neg_rating}')
    plt.savefig('wordcloud_negative.png')
    plt.show()
    print("Wygenerowano plik: wordcloud_negative.png")
else:
    print("Brak negatywnych opinii dla wskazanego progu ocen!")

df_to_export = df[['rating', 'clean_review']]
df_to_export.to_csv('opinie_klientow.csv', index=False)
print("Zapisano plik: opinie_klientow.csv")