import pandas as pd
from sqlalchemy import create_engine

user = "root"
password = "password"
host = "localhost"
database = "sakila"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

def rentals_month(engine, month, year):
    query = f"""
    SELECT
        rental_id,
        rental_date,
        customer_id
    FROM rental
    WHERE MONTH(rental_date) = {month}
      AND YEAR(rental_date) = {year};
    """
    
    df = pd.read_sql(query, engine)
    return df

def rental_count_month(df, month, year):
    column_name = f"rentals_{str(month).zfill(2)}_{year}"
    
    result = (
        df.groupby("customer_id")
          .size()
          .reset_index(name=column_name)
    )
    
    return result

def compare_rentals(df1, df2):
    df = pd.merge(df1, df2, on="customer_id", how="outer").fillna(0)
    
    col1 = df.columns[1]
    col2 = df.columns[2]
    
    df["difference"] = df[col2] - df[col1]
    
    return df

active_both = comparison[
    (comparison["rentals_05_2005"] > 0) &
    (comparison["rentals_06_2005"] > 0)
]
