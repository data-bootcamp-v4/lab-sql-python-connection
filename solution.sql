import pandas as pd
from sqlalchemy import create_engine


# Create connection to Sakila database
def get_engine():

    username = "root"
    password = "YOUR_PASSWORD"
    host = "localhost"
    database = "sakila"

    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}/{database}"
    )

    return engine



# ---------------------------------------------------
# Function 1:
# Get rentals for a specific month and year
# ---------------------------------------------------

def rentals_month(engine, month, year):

    query = f"""
    SELECT *
    FROM rental
    WHERE MONTH(rental_date) = {month}
    AND YEAR(rental_date) = {year};
    """

    rentals = pd.read_sql(query, engine)

    return rentals



# ---------------------------------------------------
# Function 2:
# Count rentals per customer
# ---------------------------------------------------

def rental_count_month(rentals_df, month, year):

    rental_count = (
        rentals_df
        .groupby("customer_id")
        .size()
        .reset_index(
            name=f"rentals_{month:02d}_{year}"
        )
    )

    return rental_count



# ---------------------------------------------------
# Function 3:
# Compare two months
# ---------------------------------------------------

def compare_rentals(df1, df2):

    comparison = pd.merge(
        df1,
        df2,
        on="customer_id",
        how="outer"
    )

    comparison = comparison.fillna(0)


    first_column = df1.columns[1]
    second_column = df2.columns[1]


    comparison["difference"] = (
        comparison[first_column] -
        comparison[second_column]
    )


    return comparison



# ---------------------------------------------------
# Run the exercise
# ---------------------------------------------------

if __name__ == "__main__":

    engine = get_engine()


    # May 2005
    may_rentals = rentals_month(
        engine,
        5,
        2005
    )

    may_customer_rentals = rental_count_month(
        may_rentals,
        5,
        2005
    )


    print("\nMay 2005")
    print(may_customer_rentals.head())



    # June 2005
    june_rentals = rentals_month(
        engine,
        6,
        2005
    )


    june_customer_rentals = rental_count_month(
        june_rentals,
        6,
        2005
    )


    print("\nJune 2005")
    print(june_customer_rentals.head())



    # Compare May vs June
    result = compare_rentals(
        may_customer_rentals,
        june_customer_rentals
    )


    print("\nComparison")
    print(result.head())
    password = "YOUR_PASSWORD"
    python solution.py
