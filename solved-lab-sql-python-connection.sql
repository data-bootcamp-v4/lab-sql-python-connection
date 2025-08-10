USE sakila;

# 1. Establish a connection between Python and the Sakila database.
# Done in Jupyter Notebook

# 2. Write a Python function called rentals_month that retrieves rental data for a given month and year (passed as parameters) from the Sakila database as a Pandas DataFrame. The function should take in three parameters:

# engine
# month
# year


# 3. The number of rentals made by each customer_id during the selected month and year.
SELECT customer_id, COUNT(rental_id)
FROM rental
WHERE MONTH(rental_date) = {month} AND YEAR(rental_date) = {year} 
GROUP BY customer_id;


rename column {year} 




The function should also include the month and year as parameters and use them to name the new column according to the month and year, for example, if the input month is 05 and the year is 2005, the column name should be 
