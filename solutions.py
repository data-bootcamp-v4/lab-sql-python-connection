import pandas as pd
from sqlalchemy import create_engine

#1.
user = "root"
password = "password_here"
host = "localhost"
database = "sakila"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

#2.
def rentals_month(engine, month, year):
    query = f"""
        SELECT *
        FROM rental
        WHERE MONTH(rental_date) = {int(month)}
          AND YEAR(rental_date) = {int(year)};
    """
    return pd.read_sql(query, engine)

#3.
def rental_count_month(df, month, year):
    col = f"rentals_{str(month).zfill(2)}_{year}"
    return (df.groupby("customer_id")["rental_id"]
              .count().reset_index()
              .rename(columns={"rental_id": col}))

#4.
def compare_rentals(df1, df2):
    merged = df1.merge(df2, on="customer_id", how="inner")
    c1, c2 = merged.columns[1], merged.columns[2]
    merged["difference"] = merged[c2] - merged[c1]
    return merged


may = rental_count_month(rentals_month(engine, 5, 2005), 5, 2005)
jun = rental_count_month(rentals_month(engine, 6, 2005), 6, 2005)
result = compare_rentals(may, jun)
print(result.head())
