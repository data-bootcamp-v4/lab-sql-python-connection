#Welcome to the Connecting Python to SQL lab!
#In this lab, you will be working with the Sakila database on movie rentals. Specifically, you will be practicing how to do basic SQL queries using Python. By connecting Python to SQL, you can leverage the power of both languages to efficiently manipulate and analyze large datasets. Throughout this lab, you will practice how to use Python to retrieve and manipulate data stored in the Sakila database using SQL queries. Let's get started!

#Challenge
#In this lab, the objective is to identify the customers who were active in both May and June, and how did their activity differ between months. 
#To achieve this, follow these steps:

#1.Establish a connection between Python and the Sakila database.




#2.Write a Python function called rentals_month that retrieves rental data for a given month and year (passed as parameters) from the Sakila database as a Pandas DataFrame. The function should take in three parameters:
#engine: an object representing the database connection engine to be used to establish a connection to the Sakila database.
#month: an integer representing the month for which rental data is to be retrieved.
#year: an integer representing the year for which rental data is to be retrieved.
#The function should execute a SQL query to retrieve the rental data for the specified month and year from the rental table in the Sakila database, and return it as a pandas DataFrame.




#3.Develop a Python function called rental_count_month that takes the DataFrame provided by rentals_month as input along with the month and year and returns a
#new DataFrame containing the number of rentals made by each customer_id during the selected month and year.
#The function should also include the month and year as parameters and use them to name the new column according to the month and year, 
#for example, if the input month is 05 and the year is 2005, the column name should be "rentals_05_2005".
#Hint: Consider making use of pandas groupby()



#4.Create a Python function called compare_rentals that takes two DataFrames as input containing the number of rentals made by each customer in different months and years.
# The function should return a combined DataFrame with a new 'difference' column, which is the difference between the number of rentals in the two months.




#---------------------------END----------------------#