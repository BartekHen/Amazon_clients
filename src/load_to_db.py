import duckdb
import pandas as pd

CSV_FILE = 'opinie_klientow.csv'
DB_FILE = 'reviews.duckdb'

def load_reviews(csv_file=CSV_FILE, db_file=DB_FILE):
    df = pd.read_csv(csv_file)

    con = duckdb.connect(db_file)
    con.execute("DROP TABLE IF EXISTS reviews")
    con.register('reviews_df', df)
    con.execute("CREATE TABLE reviews AS SELECT * FROM reviews_df")
    con.close()

    print(f"Loaded {len(df)} reviews into {db_file}")

if __name__ == "__main__":
    load_reviews()
