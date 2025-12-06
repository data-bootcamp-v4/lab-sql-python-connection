# sakila_rentals.py

# -------------------------------
# 1. Importar librerías
# -------------------------------
from sqlalchemy import create_engine
import pandas as pd

# -------------------------------
# 2. Conexión a la base de datos
# -------------------------------
# Reemplaza 'TU_USUARIO' y 'TU_CONTRASEÑA' por tus datos reales
engine = create_engine("mysql+pymysql://root:edu1993@localhost/sakila")

# -------------------------------
# 3. Funciones
# -------------------------------

def rentals_month(engine, month, year):
    """
    Obtiene los alquileres de un mes y año específicos.
    Devuelve un DataFrame con rental_id, rental_date y customer_id.
    """
    query = f"""
        SELECT rental_id, rental_date, customer_id
        FROM rental
        WHERE MONTH(rental_date) = {month}
        AND YEAR(rental_date) = {year};
    """
    df = pd.read_sql(query, engine)
    return df

def rental_count_month(df, month, year):
    """
    Cuenta el número de alquileres por cliente en el mes especificado.
    Devuelve un DataFrame con customer_id y la columna 'rentals_MM_YYYY'.
    """
    col_name = f"rentals_{month:02d}_{year}"
    result = df.groupby("customer_id").size().reset_index(name=col_name)
    return result

def compare_rentals(df1, df2):
    """
    Compara dos DataFrames de alquileres y devuelve un DataFrame combinado
    con la diferencia de alquileres entre los dos meses.
    """
    merged = df1.merge(df2, on="customer_id", how="outer").fillna(0)
    col1 = merged.columns[1]
    col2 = merged.columns[2]
    merged["difference"] = merged[col2] - merged[col1]
    return merged

# -------------------------------
# 4. Ejecución principal
# -------------------------------
if __name__ == "__main__":
    # Ejemplo: mayo y junio de 2005
    mayo = rentals_month(engine, 5, 2005)
    mayo_counts = rental_count_month(mayo, 5, 2005)

    junio = rentals_month(engine, 6, 2005)
    junio_counts = rental_count_month(junio, 6, 2005)

    resultado = compare_rentals(mayo_counts, junio_counts)

    # Mostrar primeras filas
    print(resultado.head())


