# Analiza Opinii Klientów (NLP) – Python & Power BI 📊🐍

Ten projekt prezentuje kompleksowy proces ETL (Extract, Transform, Load) oraz analizę sentymentu opinii klientów sklepu internetowego. Łączy moc przetwarzania języka naturalnego w Pythonie z interaktywną wizualizacją w Power BI.

Wykorzystane narzędzia i procesy:
- **Python:** Pobieranie i czyszczenie danych, Inżynieria Cech (Feature Engineering), Analiza Sentymentu (NLP za pomocą TextBlob), generowanie chmur słów (WordCloud), eksport wzbogaconych danych.
- **Power BI:** Interaktywny dashboard analityczny korelujący oceny klientów z faktycznym wydźwiękiem emocjonalnym ich wypowiedzi.

## 📂 Zawartość repozytorium
- `main.py` – modułowy kod Pythona do przetwarzania tekstu, analizy NLP i eksportu.
- `opinie_klientow.csv` – wygenerowany zbiór danych (zawiera m.in. oceny, wynik sentymentu, długość opinii, liczbę znaków interpunkcyjnych).
- `analiza_opinii.pbix` – gotowy, interaktywny dashboard Power BI.
- `wordcloud_positive.png` / `wordcloud_negative.png` – wygenerowane chmury słów dla skrajnych ocen.

## 📦 Dane
Dane pochodzą z potężnego zbioru [Kaggle: Amazon Reviews](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews). Skrypt automatycznie przetwarza próbkę tysięcy opinii, co pozwala na płynną analizę bez przeciążania pamięci.

## 🚀 Jak uruchomić?

1. Zainstaluj wymagane biblioteki w środowisku Python 3:
   ```bash
   pip install pandas matplotlib wordcloud textblob tqdm
   python main.py

   3. Otwórz plik `analiza_opinii.pbix` w programie **Power BI Desktop**.
4. W razie potrzeby odśwież źródło danych, wskazując nowo wygenerowany plik `opinie_klientow.csv`.

## 📈 Prezentacja wyników (Możliwości Dashboardu Power BI)
Dzięki wzbogaceniu danych w Pythonie, dashboard w Power BI prezentuje znacznie więcej niż tylko proste zliczenia:

- **Rozkład ocen vs. Sentyment:** Wykres porównujący oficjalną ocenę klienta (Rating) z rzeczywistym nacechowaniem emocjonalnym tekstu (Sentiment Score od -1.0 do 1.0).
- **Długość opinii (Word Count):** Analiza tego, czy niezadowoleni klienci piszą dłuższe i bardziej wyczerpujące recenzje.
- **Wskaźnik "Furii" (Exclamation Count):** Korelacja użycia wykrzykników (`!!!`) z negatywnymi ocenami.
- **Chmury Słów:** Wizualizacja najczęściej pojawiających się słów i fraz z podziałem na opinie pozytywne i negatywne.

---
# Amazon_clients
