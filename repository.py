import sqlite3
import pandas as pd

def normalize_month(month):
    """
    Zero-pad single-digit months (e.g. 6 -> '06') for use in date strings.
    """
    
    if month < 10:
        month = f"0{month}"
    return month

def rentals_month(engine, month, year):
    """
    Fetch all rental records for the given month and year from the database.
    """

    month = normalize_month(month)

    query = f"SELECT * FROM rental WHERE rental_date >= datetime('{year}-{month}-01') AND rental_date <= datetime('{year}-{month}-31')"
    df = pd.read_sql_query(query, engine)
    return df

def rental_count_month(df, month, year):
    """
    Count distinct rentals per customer for the given month and year.

    Returns a DataFrame with a single column named 'rental_MM_YYYY'.
    """
    month = normalize_month(month)
    result = pd.DataFrame()
    result[f"rental_{month}_{year}"] = df.groupby("customer_id")["rental_id"].nunique()
    return result


def compare_rentals(df1, df2):
    """
    Merge two monthly rental-count DataFrames on customer_id (outer join)
    and add a 'difference' column (df1 count minus df2 count).
    """
    first_column = df1.columns[0]
    second_column = df2.columns[0]
    df1 = df1.reset_index()
    df2 = df2.reset_index()
    result = pd.DataFrame()
    result = pd.merge(left=df1, right=df2, how="outer")
    result["difference"] = result[first_column] - result[second_column]
    return result


if __name__ == "__main__":
    connection = sqlite3.connect("sqlite-sakila.db")

    june_rentals = rentals_month(connection, 6, 2005)
    df1 = rental_count_month(june_rentals, 6, 2005)
    df2 = rental_count_month(june_rentals, 5, 2005)
    print(compare_rentals(df1, df2))