import mysql.connector
import pandas as pd

# Establish the connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='234678',
    database='sakila'
)

# Define the function to retrieve rental data for a specific month and year
def rentals_month(engine, month, year):
    query = f"""
        SELECT customer_id, rental_date, film_id
        FROM rental
        WHERE MONTH(rental_date) = {month} AND YEAR(rental_date) = {year};
    """
    return pd.read_sql(query, engine)

# Retrieve data for May 2005
df_may_2005 = rentals_month(connection, 5, 2005)
print(df_may_2005.head())

# Close the connection
connection.close()
