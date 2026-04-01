YEAR = """
SELECT *
FROM rental
WHERE YEAR(rental_date) = 2005;
"""

MONTH = """
SELECT *
FROM rental
WHERE MONTH(rental_date) = 8;
"""