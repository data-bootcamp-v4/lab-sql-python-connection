def get_rentals_month_query():
    query = """
            SELECT * \
            FROM rental
            WHERE MONTH(rental_date) = %s
              AND YEAR(rental_date) = %s; \
            """
    return query