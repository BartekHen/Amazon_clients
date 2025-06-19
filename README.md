# Analiza opinii klientów – Python & Power BI

Ten projekt prezentuje analizę opinii klientów sklepu internetowego w dwóch narzędziach:
- **Python** (przygotowanie i czyszczenie danych, generowanie wordcloud, eksport do CSV)
- **Power BI** (dashboard: rozkład ocen, długość opinii, chmura słów, udział pozytywnych/negatywnych opinii)

## Zawartość repozytorium
- `main.py` – kod Pythona do analizy i eksportu opinii
- `opinie_klientow.csv` – dane wejściowe do Power BI
- `analiza_opinii.pbix` – gotowy dashboard Power BI

## Dane
Dane pochodzą z [Kaggle: Amazon Reviews](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews).

## Jak uruchomić?
1. Uruchom `main.py` (Python 3, wymagane biblioteki: pandas, matplotlib, wordcloud)
2. Załaduj `opinie_klientow.csv` do Power BI Desktop
3. Otwórz lub odtwórz dashboard z pliku `.pbix`

## Prezentacja wyników
- Rozkład ocen klientów (wykres słupkowy)
- Średnia długość opinii wg oceny
- Chmura najczęściej używanych słów
- Udział pozytywnych i negatywnych opinii (pie chart)

---
# Amazon_clients
