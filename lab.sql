import pandas as pd
from sqlalchemy import create_engine

# 1. Función para conectar Python a la base de datos Sakila
def rentals_month(engine, month, year):
    """
    Esta función devuelve un DataFrame con los datos de alquileres para el mes y año indicados.
    
    Parámetros:
    engine -- el objeto de conexión a la base de datos
    month -- el mes para el cual se quieren recuperar los datos de alquileres (en formato entero)
    year -- el año para el cual se quieren recuperar los datos de alquileres (en formato entero)
    """
    query = f"""
    SELECT rental_id, rental_date, customer_id
    FROM rental
    WHERE MONTH(rental_date) = {month} AND YEAR(rental_date) = {year};
    """
    return pd.read_sql(query, engine)

# 2. Función para contar los alquileres por cliente en un mes específico
def rental_count_month(df, month, year):
    """
    Esta función cuenta el número de alquileres por cliente en el mes y año proporcionados.
    
    Parámetros:
    df -- DataFrame con los datos de alquileres
    month -- el mes de los alquileres (en formato entero)
    year -- el año de los alquileres (en formato entero)
    
    Retorna:
    Un DataFrame con la cuenta de alquileres por cliente.
    """
    rentals_count = df.groupby('customer_id').size().reset_index(name=f'rentals_{str(month).zfill(2)}_{year}')
    return rentals_count

# 3. Función para comparar los alquileres entre dos meses diferentes
def compare_rentals(df1, df2):
    """
    Compara los alquileres entre dos DataFrames y calcula la diferencia entre ellos.
    
    Parámetros:
    df1 -- DataFrame con el número de alquileres en el primer mes
    df2 -- DataFrame con el número de alquileres en el segundo mes
    
    Retorna:
    Un DataFrame combinado con una columna 'difference' que muestra la diferencia de alquileres.
    """
    comparison = pd.merge(df1, df2, on='customer_id', how='outer').fillna(0)
    comparison['difference'] = comparison.iloc[:, 1] - comparison.iloc[:, 2]
    return comparison

# Ejemplo de uso:

# Establecer la conexión a la base de datos Sakila
# engine = create_engine('mysql+pymysql://user:password@localhost/sakila')

# Cargar los datos de alquileres de mayo y junio
# df_may = rentals_month(engine, 5, 2005)
# df_june = rentals_month(engine, 6, 2005)

# Contar los alquileres por cliente
# rentals_may = rental_count_month(df_may, 5, 2005)
# rentals_june = rental_count_month(df_june, 6, 2005)

# Comparar los alquileres entre mayo y junio
# comparison_df = compare_rentals(rentals_may, rentals_june)

# Mostrar el resultado
# print(comparison_df)