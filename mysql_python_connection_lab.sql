
-- 1. Rentals for a given month/year
SELECT customer_id,
       rental_date
FROM sakila.rental
WHERE MONTH(rental_date) = @month
  AND YEAR(rental_date) = @year;

-- 2. Rentals count per customer for May 2005
SELECT customer_id,
       COUNT(*) AS rentals_05_2005
FROM sakila.rental
WHERE MONTH(rental_date) = 5
  AND YEAR(rental_date) = 2005
GROUP BY customer_id;

-- 3. Rentals count per customer for June 2005
SELECT customer_id,
       COUNT(*) AS rentals_06_2005
FROM sakila.rental
WHERE MONTH(rental_date) = 6
  AND YEAR(rental_date) = 2005
GROUP BY customer_id;

-- 4. Compare May vs. June 2005 and show difference
WITH may_counts AS (
  SELECT customer_id,
         COUNT(*) AS rentals_05_2005
  FROM sakila.rental
  WHERE MONTH(rental_date) = 5
    AND YEAR(rental_date) = 2005
  GROUP BY customer_id
),
jun_counts AS (
  SELECT customer_id,
         COUNT(*) AS rentals_06_2005
  FROM sakila.rental
  WHERE MONTH(rental_date) = 6
    AND YEAR(rental_date) = 2005
  GROUP BY customer_id
)
SELECT m.customer_id,
       m.rentals_05_2005,
       j.rentals_06_2005,
       (j.rentals_06_2005 - m.rentals_05_2005) AS difference
FROM may_counts m
INNER JOIN jun_counts j
  ON m.customer_id = j.customer_id
ORDER BY difference DESC;
