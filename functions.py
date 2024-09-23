from sqlalchemy import create_engine
import pymysql
import pandas as pd

## First funct from SQL

def rentals_month(engine, month, year):
    query = f"""
        SELECT rental_id, rental_date, customer_id
        FROM rental
        WHERE MONTH(rental_date) = {month} AND YEAR(rental_date) = {year}
    """
    # Ejecutar la consulta y retornar el resultado como un DataFrame
    df = pd.read_sql(query, engine)
    return df

## Second funct from SQL

def rental_count_month(df, month, year):
    # Agrupar por customer_id y contar las filas (alquileres)
    rental_counts = df.groupby('customer_id').size().reset_index(name=f'rentals_{month:02d}_{year}')
    return rental_counts


def compare_rentals(df1, df2):
    # Combinar los dos DataFrames por customer_id
    merged_df = pd.merge(df1, df2, on='customer_id', how='outer').fillna(0)
    
    # Calcular la diferencia entre los alquileres de los dos meses
    col1 = df1.columns[1]
    col2 = df2.columns[1]
    merged_df['difference'] = merged_df[col1] - merged_df[col2]
    
    return merged_df
