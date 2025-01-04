USE sakila;

SHOW TABLES; 

SELECT * FROM actor LIMIT 10;
/*
SELECT *
FROM rental
WHERE MONTH(rental_date) = :month AND YEAR(rental_date) = :year;
*/

/*
number of rentals made by each customer_id during the selected month and year
*/

SELECT * FROM sakila.rental;

SELECT customer_id FROM sakila.rental;

SELECT COUNT(*) AS total_rentals FROM rental;

SELECT COUNT(*) AS rentals_by_inventory_id, 
		inventory_id
FROM rental
GROUP BY inventory_id;

SELECT
    COUNT(*) AS rentals_by_inventory_id,
    inventory_id
    -- rental_date,
    -- return_date
FROM rental
-- WHERE
    -- DiseaseCategory = 'Infectious'
    -- AND rental_date BETWEEN 2020 AND 2024
GROUP BY
    inventory_id;
---
    SELECT
    -- COUNT(*) AS rentals_by_customer_id,
    -- customer_id
	SUM(rental_id) AS rentals_by_rental_id,
    rental_id
    
    -- rental_date,
    -- return_date
FROM rental
-- WHERE
    -- DiseaseCategory = 'Infectious'
    -- AND rental_date BETWEEN 2020 AND 2024
GROUP BY
    rental_id;
---

SELECT
    inventory_id,
    -- DiseaseCategory,
    rental_date,
    return_date
FROM rental
-- WHERE
    -- DiseaseCategory = 'Infectious'
    -- AND rental_date BETWEEN 2020 AND 2024
ORDER BY
    inventory_id DESC;
-- working 
SELECT
    inventory_id,
    -- DiseaseCategory,
    (return_date - rental_date) AS time_rented
FROM rental
-- WHERE
    -- DiseaseCategory = 'Infectious'
    -- AND rental_date BETWEEN 2020 AND 2024
ORDER BY
    inventory_id DESC;
--
SELECT
	-- COUNT(*) AS rentals_by_inventory_id,
    inventory_id,   
    (return_date - rental_date) AS time_rented
    -- COUNT(*) AS counts_inventory_id,
    -- inventory_id
FROM rental
-- WHERE
    -- DiseaseCategory = 'Infectious'
    -- AND rental_date BETWEEN 2020 AND 2024
ORDER BY
    -- inventory_id DESC;
    time_rented DESC;
--  
    SELECT
    COUNT(*) AS rentals_by_customer_id,
    customer_id
    -- rental_date,
    -- return_date
FROM rental
-- WHERE
    -- DiseaseCategory = 'Infectious'
    -- AND rental_date BETWEEN 2020 AND 2024
GROUP BY
    customer_id;
    
    --
SELECT MIN(YEAR(rental_date)) AS earliest_year, MAX(YEAR(rental_date)) AS latest_year
FROM rental;


-- 
SELECT *
FROM rental
WHERE MONTH(rental_date) = 7 AND YEAR(rental_date) = 2005;


SELECT *
FROM rental
WHERE MONTH(rental_date) = 8 AND YEAR(rental_date) = 2005;

SELECT *
FROM rental
WHERE MONTH(rental_date) = 9 AND YEAR(rental_date) = 2005;

SELECT *
FROM rental
WHERE MONTH(rental_date) = 10 AND YEAR(rental_date) = 2005;

SELECT *
FROM rental
WHERE MONTH(rental_date) = 11 AND YEAR(rental_date) = 2005;

SELECT *
FROM rental
WHERE MONTH(rental_date) = 1 AND YEAR(rental_date) = 2006;



-- count the number of rentals made by each customer_id during a specific month and year
SELECT 
    customer_id, 
    COUNT(*) AS rental_count
FROM 
    rental
WHERE 
    MONTH(rental_date) = 8rental_date AND YEAR(rental_date) = 2005
GROUP BY 
    customer_id
ORDER BY 
    rental_count DESC;


