
import pandas as pd
from sqlalchemy import create_engine

# Función para conectar con la base de datos
def connect_to_sakila(user, password, host, database):
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    return engine

# Función rentals_month para recuperar datos de alquiler para un mes y año específicos
def rentals_month(engine, month, year):
    query = f'''
    SELECT r.rental_id, r.customer_id, r.rental_date
    FROM rental r
    WHERE MONTH(r.rental_date) = {month} AND YEAR(r.rental_date) = {year};
    '''
    # Ejecutar la consulta y devolver el resultado como un DataFrame de pandas
    rentals_df = pd.read_sql(query, engine)
    return rentals_df

# Función rental_count_month para agrupar por customer_id y contar el número de alquileres
def rental_count_month(rentals_df, month, year):
    # Agrupar por customer_id y contar los alquileres
    rental_counts = rentals_df.groupby('customer_id').size().reset_index(name=f'rentals_{month:02d}_{year}')
    return rental_counts

# Ejemplo de uso:
# engine = connect_to_sakila('user', 'password', 'localhost', 'sakila')
# may_rentals = rentals_month(engine, 5, 2005)
# may_rental_count = rental_count_month(may_rentals, 5, 2005)
# print(may_rental_count)
