import pandas as pd
from sqlalchemy import create_engine

# ---------------------------
# 1) Connect Python to Sakila
# ---------------------------
# Update these credentials
# Example for MySQL:
# mysql+mysqlconnector://USER:PASSWORD@HOST:PORT/sakila
engine = create_engine("mysql+mysqlconnector://root:YOUR_PASSWORD@localhost:3306/sakila")


# ----------------------------------------------
# 2) rentals_month(engine, month, year) -> df
# ----------------------------------------------
def rentals_month(engine, month: int, year: int) -> pd.DataFrame:
    """
    Retrieve rental rows for a given month/year from Sakila rental table.
    Returns a pandas DataFrame.
    """
    sql = """
        SELECT rental_id, rental_date, customer_id, inventory_id, return_date, staff_id
        FROM rental
        WHERE YEAR(rental_date) = :year
          AND MONTH(rental_date) = :month
    """
    return pd.read_sql(sql, engine, params={"year": year, "month": month})


# -------------------------------------------------------------------
# 3) rental_count_month(df, month, year) -> df with rentals_MM_YYYY
# -------------------------------------------------------------------
def rental_count_month(rentals_df: pd.DataFrame, month: int, year: int) -> pd.DataFrame:
    """
    Takes the rentals_month output and returns rentals per customer_id for that month/year.
    Column name format: rentals_MM_YYYY (MM is zero-padded).
    """
    col_name = f"rentals_{month:02d}_{year}"

    # groupby customer_id and count rentals
    counts = (
        rentals_df.groupby("customer_id")["rental_id"]
        .count()
        .reset_index(name=col_name)
    )
    return counts


# -------------------------------------------------------------------
# 4) compare_rentals(df1, df2) -> combined df + difference column
# -------------------------------------------------------------------
def compare_rentals(df_month1: pd.DataFrame, df_month2: pd.DataFrame) -> pd.DataFrame:
    """
    Takes two customer rental-count dataframes (one per month) and returns:
    customer_id, rentals_MM_YYYY (month1), rentals_MM_YYYY (month2), difference

    difference = month2 - month1 (so positive means increased in month2).
    Keeps only customers present in BOTH dfs (active in both months).
    """
    # detect the rentals column names (besides customer_id)
    rentals_col_1 = [c for c in df_month1.columns if c != "customer_id"][0]
    rentals_col_2 = [c for c in df_month2.columns if c != "customer_id"][0]

    merged = df_month1.merge(df_month2, on="customer_id", how="inner")

    merged["difference"] = merged[rentals_col_2] - merged[rentals_col_1]
    return merged.sort_values("difference", ascending=False).reset_index(drop=True)


# ---------------------------
# Example: May vs June (2005)
# ---------------------------
may_rentals = rentals_month(engine, 5, 2005)
june_rentals = rentals_month(engine, 6, 2005)

may_counts = rental_count_month(may_rentals, 5, 2005)
june_counts = rental_count_month(june_rentals, 6, 2005)

comparison = compare_rentals(may_counts, june_counts)

print(comparison.head(20))          # top 20 biggest increases
print("Customers active in both:", len(comparison))
