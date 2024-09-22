-- Write a Python function called rentals_month that retrieves rental data for a given month and year (passed as parameters)
-- from the Sakila database as a Pandas DataFrame.  
import mysql.connector
from mysql.connector import Error

def rentals_month(year, month):
        connection = mysql.connector.connect(
            host='localhost',  
            database='sakila',  
            user='root',       
            password='1234' 
        )
if connection.is_connected():
            cursor = connection.cursor()

-- Consulta para obtener los datos de alquiler de un mes y año específico
          
SELECT rental_id, rental_date, return_date, customer_id, inventory_id
FROM rental
WHERE YEAR(rental_date) = %s AND MONTH(rental_date) = %s;


