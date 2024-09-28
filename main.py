# Paso 1: Conéctese a la base de datos de Sakila
# Necesitamos configurar la conexión a la base de datos usando SQLAlchemy.

import pandas as pd
from sqlalchemy import create_engine

# Replace the following credentials with the correct ones for your setup
def connect_db():
    DATABASE_URI = 'mysql+pymysql://root:Danny@localhost/sakila'
    engine = create_engine(DATABASE_URI)
    return engine

# Paso 2: Crea la rentals_monthfunción
# Esta función recuperará datos de alquiler para un mes y año específicos.
def rentals_month(engine, month, year):
    query = f"""
    SELECT customer_id, rental_id, rental_date
    FROM rental
    WHERE MONTH(rental_date) = {month} AND YEAR(rental_date) = {year};
    """
    return pd.read_sql(query, engine)

# Paso 3: Crea la rental_count_monthfunción
def rental_count_month(rental_data, month, year):
    # Agrupar por customer_id y contar el número de alquileres
    rental_count = rental_data.groupby('customer_id').size().reset_index(name=f'rentals_{month:02d}_{year}')
    return rental_count

# Ahora necesitamos calcular el número de alquileres de cada uno customer_iddurante un mes específico

def rental_count_month(rental_data, month, year):
    # Group by customer_id and count the number of rentals
    rental_count = rental_data.groupby('customer_id').size().reset_index(name=f'rentals_{month:02d}_{year}')
    return rental_count

# Paso 4: Crea la compare_rentalsfunción
def compare_rentals(df1, df2):
    # Asegúrate de que ambos DataFrames tengan nombres de columnas consistentes antes de unir
    comparison_df = pd.merge(df1, df2, on='customer_id', how='outer').fillna(0)
    
    # Agregar una columna 'difference' que es la diferencia en el número de alquileres entre los dos meses
    rental_col1 = df1.columns[1]
    rental_col2 = df2.columns[1]
    comparison_df['difference'] = comparison_df[rental_col1] - comparison_df[rental_col2]
    return comparison_df


# Esta función comparará la actividad de alquiler a lo largo de dos meses.
def compare_rentals(df1, df2):
    # Merge the two dataframes on customer_id
    comparison_df = pd.merge(df1, df2, on='customer_id', how='outer').fillna(0)
    
    # Add a 'difference' column which is the difference in the number of rentals between the two months
    comparison_df['difference'] = comparison_df.iloc[:, 1] - comparison_df.iloc[:, 2]
    return comparison_df



if __name__ == "__main__":
    # Conectar a la base de datos
    engine = connect_db()
    
    # Obtener datos de alquiler para dos meses y años específicos
    rental_data_jan = rentals_month(engine, 1, 2020)  # Por ejemplo, enero 2020
    rental_data_feb = rentals_month(engine, 2, 2020)  # Por ejemplo, febrero 2020
    
    # Calcular el número de alquileres por cliente para cada mes
    jan_rental_count = rental_count_month(rental_data_jan, 1, 2020)
    feb_rental_count = rental_count_month(rental_data_feb, 2, 2020)
    
    # Comparar la actividad de alquiler entre los dos meses
    comparison_df = compare_rentals(jan_rental_count, feb_rental_count)
    
    # Mostrar el resultado
    print(comparison_df)