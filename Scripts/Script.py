import pandas as pd
from sqlalchemy import create_engine
import pymysql

# Database connection
DB_USER = 'root'
DB_PASSWORD = '14t46p74z06c'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'sakila'

engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

def rentals_month(engine, month, year):
    query = f"SELECT * FROM rental WHERE MONTH(rental_date) = {month} AND YEAR(rental_date) = {year}"
    
    df = pd.read_sql(query, engine.connect())
    return df

def rental_count_month(df, month, year):
    rentals_count = df.groupby('customer_id').size().reset_index(name="rentals_{month}_{year}")
    return rentals_count

def compare_rentals(df1, df2):
    main_df = pd.merge(df1, df2, on='customer_id').fillna(0)
    rentals_col1 = main_df.columns[1]
    rentals_col2 = main_df.columns[2]
    main_df['difference'] = main_df[rentals_col2] - main_df[rentals_col1]
    return main_df

may_rentals = rentals_month(engine, 5, 2005)
june_rentals = rentals_month(engine, 6, 2005)

may_rental_counts = rental_count_month(may_rentals, 5, 2005)
june_rental_counts = rental_count_month(june_rentals, 6, 2005)

comparison = compare_rentals(may_rental_counts, june_rental_counts)

# Display the results
print(comparison)