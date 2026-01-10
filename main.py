import os
import pandas as pd
from sqlalchemy import create_engine, text


def get_engine():
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD","Kalamarhs1997")
    host = os.getenv("MYSQL_HOST", "127.0.0.1")
    port = os.getenv("MYSQL_PORT", "3306")
    db = os.getenv("MYSQL_DB", "sakila")

    if not password:
        raise ValueError("MYSQL_PASSWORD not set")

    url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url)


def rentals_month(engine, month, year):
    query = text("""
        SELECT rental_id, rental_date, inventory_id, customer_id, return_date, staff_id
        FROM rental
        WHERE YEAR(rental_date) = :year
          AND MONTH(rental_date) = :month
    """)
    return pd.read_sql(query, engine, params={"year": year, "month": month})


def rental_count_month(df, month, year):
    col = f"rentals_{month:02d}_{year}"
    return df.groupby("customer_id").size().reset_index(name=col)


def compare_rentals(df1, df2):
    col1 = [c for c in df1.columns if c.startswith("rentals_")][0]
    col2 = [c for c in df2.columns if c.startswith("rentals_")][0]

    merged = df1.merge(df2, on="customer_id", how="inner")
    merged["difference"] = merged[col2] - merged[col1]

    return merged.sort_values("difference", ascending=False)


def main():
    engine = get_engine()

    may = rentals_month(engine, 5, 2005)
    june = rentals_month(engine, 6, 2005)

    may_counts = rental_count_month(may, 5, 2005)
    june_counts = rental_count_month(june, 6, 2005)

    comparison = compare_rentals(may_counts, june_counts)

    print(comparison.head(20))

    comparison.to_csv("may_vs_june_rentals.csv", index=False)
    print("Saved to may_vs_june_rentals.csv")


if __name__ == "__main__":
    main()
