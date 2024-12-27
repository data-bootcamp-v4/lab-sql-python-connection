import pandas as pd
import mysql.connector

def rentals_month(engine, month, year):
    cursor = engine.cursor()

    query = """
    SELECT *
    FROM rental
    WHERE YEAR(rental_date) = {} AND MONTH(rental_date) = {}
    """.format(year, month)

    cursor.execute(query)

    df = pd.DataFrame(cursor.fetchall(), columns=cursor.column_names)

    cursor.close()

    return df

config = {
  'user': 'root',
  'password': 'Todourru91',
  'host': 'localhost',
  'database': 'sakila'
}
cnx = mysql.connector.connect(**config)

rental_data = rentals_month(cnx, 2, 2006)
print(rental_data)


def rental_count_month(rental_data, month, year):
    rental_count = rental_data[(rental_data['rental_date'].dt.month == month) & (rental_data['rental_date'].dt.year == year)]\
        .groupby('customer_id')\
        .size()\
        .reset_index(name='rentals_{:02d}_{}'.format(month, year))

    return rental_count

def compare_rentals(df1, df2):
    merged_df = pd.merge(df1, df2, on='customer_id', suffixes=('_left', '_right'))

    merged_df['difference'] = merged_df.iloc[:, 1] - merged_df.iloc[:, 2]

    return merged_df

data1 = {'customer_id': [1, 2, 3, 4, 5],
         'rentals_05_2005': [10, 5, 8, 12, 6]}
df1 = pd.DataFrame(data1)

data2 = {'customer_id': [1, 2, 3, 4, 5],
         'rentals_05_2006': [8, 4, 6, 10, 5]}
df2 = pd.DataFrame(data2)

result1 = compare_rentals(df1, df2)
print(result1)