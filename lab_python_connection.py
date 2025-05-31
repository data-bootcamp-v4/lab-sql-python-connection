import pandas as pd
import pymysql
from sqlalchemy import create_engine
import mysql.connector

from getpass import getpass

pwd = getpass()
connection = mysql.connector.connect(host = "localhost",
                                     user = "root",
                                     passwd = pwd)

user = "root"
host = "localhost"

engine = create_engine(f"mysql+pymysql://{user}:{pwd}@{host}")

print(f'Connection made correctly:{connection.is_connected()}')

def select_schema():
    schema_name = input('Please enter the name of the schema you want to analyze')
    cursor = connection.cursor()
    cursor.execute(f"""
                    Use {schema_name}
                    """)

def rental_count_month(month_int, year_int):
    df = rentals_month(month_int, year_int)
    col_name = f'rentals_{month_int}_{year_int}'
    df = df.groupby(['month', 'year']).agg(month_count=('month', 'count')).reset_index()
    df.rename(columns={'month_count': col_name}, inplace=True)
    return df

def compare_rentals(month_int, year_int):
    cursor = connection.cursor()
    cursor.execute(f"""
                    WITH 
                    current_m AS (SELECT customer_id, COUNT(*) AS current_rentals
                        FROM rental
                        WHERE MONTH(rental_date) = {month_int} AND YEAR(rental_date) = {year_int}
                        GROUP BY customer_id),
                    previous_m AS (SELECT customer_id, COUNT(*) AS previous_rentals
                        FROM rental
                        WHERE MONTH(rental_date) = {month_int-1} AND YEAR(rental_date) = {year_int}
                        GROUP BY customer_id)

                    SELECT 
                        COALESCE(c.customer_id, p.customer_id) AS customer_id,
                        COALESCE(p.previous_rentals,0) AS month_{month_int-1}_rentals,
                        COALESCE(c.current_rentals,0) AS month_{month_int}_rentals
                    FROM current_m AS c
                    LEFT JOIN previous_m AS p 
                        ON c.customer_id = p.customer_id

                    UNION

                    SELECT 
                        COALESCE(c.customer_id, p.customer_id) AS customer_id,
                        COALESCE(p.previous_rentals,0) AS month_{month_int-1}_rentals,
                        COALESCE(c.current_rentals,0) AS month_{month_int}_rentals
                    FROM previous_m AS p
                    LEFT JOIN current_m AS c 
                        ON p.customer_id = c.customer_id;
                    """)
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=cursor.column_names)
    df['diff_rentals'] = df[df.columns[-1]] - df[df.columns[-2]]
    return df

def get_user_input():
    month = input('Enter the month number you want to analyze:')
    year = input('Enter the year you want to analyze:')

    display(rental_count_month(month, year))
    display(compare_rentals(month, year))