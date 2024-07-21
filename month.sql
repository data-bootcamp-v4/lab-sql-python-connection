USE sakila;
SELECT *
FROM rental
WHERE MONTH(rental_date) = 5
AND YEAR(rental_date) = 2005;