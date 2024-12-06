SELECT *
FROM rental
WHERE YEAR(rental_date)= 2005 AND MONTH(rental_date)=5;

-- 3. Develop a Python function called `rental_count_month` that takes the DataFrame provided by `rentals_month` 
-- as input along with the month and year and returns a new DataFrame containing the number of rentals made by each customer_id 
-- during the selected month and year. 

-- The function should also include the month and year as parameters and use them to name the new column according to the month and year, 
-- for example, if the input month is 05 and the year is 2005, the column name should be "rentals_05_2005".

SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    COUNT(r.rental_id) AS rentals_05_2005
FROM rental r
JOIN customer c USING (customer_id)
WHERE YEAR(r.rental_date) = 2005 AND MONTH(r.rental_date) = 5
GROUP BY customer_name
ORDER BY rentals_05_2005 DESC;


-- Create a Python function called `compare_rentals` that takes two 
-- DataFrames as input containing the number of rentals made by each customer in different months and years. 
-- The function should return a combined DataFrame with a new 'difference' column, which is the difference 
-- between the number of rentals in the two months.


