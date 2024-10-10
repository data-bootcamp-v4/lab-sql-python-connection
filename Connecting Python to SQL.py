import pandas as pd
from sqlalchemy import create_engine

# Función para conectar a la base de datos
def connect_db():
    # Reemplaza 'username', 'password' y 'host' con tus credenciales de base de datos
    engine = create_engine('mysql+pymysql://root:password@127.0.0.1:3306/sakila')
    return engine

# Función que obtiene los alquileres para un mes y año determinados
def rentals_month(engine, month, year):
    query = f"""
    SELECT customer_id, rental_date
    FROM rental
    WHERE MONTH(rental_date) = {month}
    AND YEAR(rental_date) = {year};
    """
    # Ejecuta la consulta y devuelve el resultado como DataFrame de pandas
    rentals_df = pd.read_sql(query, engine)
    return rentals_df

# Función que cuenta los alquileres por cliente para un mes y año específicos
def rental_count_month(rentals_df, month, year):
    # Agrupamos por 'customer_id' para contar cuántos alquileres realizó cada cliente
    rental_count_df = rentals_df.groupby('customer_id').size().reset_index(name=f'rentals_{month:02d}_{year}')
    return rental_count_df

# Función para comparar los alquileres entre dos meses y años distintos
def compare_rentals(df1, df2):
    # Hacemos un merge para combinar ambos DataFrames por 'customer_id'
    merged_df = pd.merge(df1, df2, on='customer_id', how='outer').fillna(0)
    # Creamos una nueva columna que representa la diferencia de alquileres
    merged_df['difference'] = merged_df.iloc[:, 1] - merged_df.iloc[:, 2]
    return merged_df

# Ejemplo de uso
if __name__ == "__main__":
    # Conectar a la base de datos
    engine = connect_db()

    # Obtener alquileres para mayo de 2005
    rentals_may = rentals_month(engine, 5, 2005)
    rental_count_may = rental_count_month(rentals_may, 5, 2005)

    # Obtener alquileres para junio de 2005
    rentals_june = rentals_month(engine, 6, 2005)
    rental_count_june = rental_count_month(rentals_june, 6, 2005)

    # Comparar alquileres entre mayo y junio de 2005
    comparison_df = compare_rentals(rental_count_may, rental_count_june)

    print(comparison_df.head())
