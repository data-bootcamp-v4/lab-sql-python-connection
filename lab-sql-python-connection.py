import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:d5*y44<iVz>E@localhost/sakila')

def rentals_month(engine, month, year):
    query = f"""
    select *
    from rental
    where month(rental_date) = {month}
    and year(rental_date) = {year}
    """
    df = pd.read_sql(query, engine)
    return df

def rental_count_month(df, month, year):
    result = df.groupby('customer_id').size().reset_index(name=f'rentals_{month:02d}_{year}')
    return result

def compare_rentals(df1, df2):
    merged = pd.merge(df1, df2, on='customer_id', how='outer')
    merged = merged.fillna(0)
    merged['difference'] = merged.iloc[:, 2] - merged.iloc[:, 1]
    return merged

# get may 2005 rentals
print("Getting May 2005 rentals...")
may_rentals = rentals_month(engine, 5, 2005)
print(f"Found {len(may_rentals)} rentals in May 2005")

# count may rentals per customer
may_counts = rental_count_month(may_rentals, 5, 2005)
print(f"\n{len(may_counts)} customers rented in May")
print(may_counts.head())

# get june 2005 rentals
print("\nGetting June 2005 rentals...")
june_rentals = rentals_month(engine, 6, 2005)
print(f"Found {len(june_rentals)} rentals in June 2005")

# count june rentals per customer
june_counts = rental_count_month(june_rentals, 6, 2005)
print(f"\n{len(june_counts)} customers rented in June")
print(june_counts.head())

# compare the two months
print("\nComparing May and June activity...")
comparison = compare_rentals(may_counts, june_counts)
print(comparison.head(10))

print(f"\nCustomers active in both months: {len(comparison)}")
print(f"Customers who rented MORE in June: {len(comparison[comparison['difference'] > 0])}")
print(f"Customers who rented LESS in June: {len(comparison[comparison['difference'] < 0])}")