use sakila;

show tables;
select * from rental;


SELECT DATE_FORMAT(rental_date, '%M %d, %Y') AS formatted_date
FROM rental
WHERE DATE_FORMAT(rental_date, '%m') = 7
AND DATE_FORMAT(rental_date, '%y') = 2014;

SELECT DATE_FORMAT(rental_date, '%m') AS month
FROM rental
WHERE DATE_FORMAT(rental_date, '%m') = 7;

SELECT DATE_FORMAT(rental_date, '%Y') AS month
FROM rental;

