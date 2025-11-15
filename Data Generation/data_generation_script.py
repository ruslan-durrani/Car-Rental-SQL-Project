


import os
import sqlite3
from faker import Faker
import random
import datetime
print("Python is using this database file:")
db_path = "/Users/ruslanbabar/Downloads/SQL-Assignment/Car_Rental_SQL_Project/car_rental.db"
print(os.path.abspath(db_path))
# ----------------------------------------
# SETUP
# ----------------------------------------
fake = Faker()
db_path = "car_rental.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("Connected to database:", db_path)

# ----------------------------------------
# Helper function for random dates
# ----------------------------------------
def random_date(start_year=2022, end_year=2025):
    start = datetime.date(start_year, 1, 1)
    end = datetime.date(end_year, 12, 31)
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + datetime.timedelta(days=random_days)

# ----------------------------------------
# Insert Branches
# ----------------------------------------
branches = []
for _ in range(30):
    branches.append((
        fake.company(),
        fake.city(),
        random.choice([1,2,3,4,5, None])  # Missing rating on purpose
    ))

cursor.executemany(
    "INSERT INTO Branches (branch_name, city, rating) VALUES (?,?,?)",
    branches
)
print("Inserted branches:", len(branches))

# ----------------------------------------
# Insert Customers (NO duplicate emails)
# ----------------------------------------
customers = []
emails_used = set()

for _ in range(300):
    first = fake.first_name()
    last = fake.last_name()

    # Always generate an email until it is unique
    email = fake.email()
    while email in emails_used:
        email = fake.email()  # regenerate until unique
    emails_used.add(email)

    # Random missing phone numbers (10%)
    phone = fake.phone_number() if random.random() > 0.10 else None

    membership = random.choice(['Bronze', 'Silver', 'Gold'])

    customers.append((first, last, email, phone, membership))

cursor.executemany(
    "INSERT INTO Customers (first_name, last_name, email, phone, membership_tier) VALUES (?,?,?,?,?)",
    customers
)
print("Inserted customers:", len(customers))


# ----------------------------------------
# Insert Cars
# ----------------------------------------
car_makes = ["Toyota", "Ford", "BMW", "Audi", "Mercedes", "Honda", "Nissan"]

cars = []
for _ in range(200):
    make = random.choice(car_makes)
    model = fake.word().title()
    year = random.randint(2005, 2024)
    mileage = round(random.uniform(0, 200000), 2)
    daily_rate = round(random.uniform(20, 150), 2)
    status = random.choice(['Available','Rented','Maintenance'])

    cars.append((make, model, year, mileage, daily_rate, status))

cursor.executemany(
    "INSERT INTO Cars (make, model, year, mileage, daily_rate, status) VALUES (?,?,?,?,?,?)",
    cars
)
print("Inserted cars:", len(cars))

# ----------------------------------------
# Insert Car_Location (many-to-many)
# ----------------------------------------
car_locations = []
branch_ids = list(range(1, len(branches)+1))
car_ids = list(range(1, len(cars)+1))

for car_id in car_ids:
    assigned_branch = random.choice(branch_ids)
    car_locations.append((car_id, assigned_branch))

cursor.executemany(
    "INSERT INTO Car_Location (car_id, branch_id) VALUES (?,?)",
    car_locations
)
print("Inserted car-location links:", len(car_locations))

# ----------------------------------------
# Insert Rentals (1000+ rows)
# ----------------------------------------
rentals = []
for _ in range(1200):  # 1200 for safety
    customer_id = random.randint(1, 300)
    car_id = random.randint(1, 200)
    rental_date = random_date()

    # Some rentals have no return date (missing)
    if random.random() < 0.1:
        return_date = None
        duration = 0
    else:
        return_date = rental_date + datetime.timedelta(days=random.randint(1, 14))
        duration = (return_date - rental_date).days

    # total cost = duration × daily_rate (lookup is skipped for speed; random approximate instead)
    total_cost = round(random.uniform(20, 1800), 2)

    rentals.append((
        customer_id,
        car_id,
        rental_date.isoformat(),
        return_date.isoformat() if return_date else None,
        duration,
        total_cost
    ))

cursor.executemany(
    "INSERT INTO Rentals (customer_id, car_id, rental_date, return_date, rental_duration_days, total_cost) VALUES (?,?,?,?,?,?)",
    rentals
)
print("Inserted rentals:", len(rentals))

# ----------------------------------------
# Insert Payments
# ----------------------------------------
payments = []
rental_ids = list(range(1, len(rentals)+1))

for rental_id in rental_ids:
    amount = round(random.uniform(10, 1800), 2)
    method = random.choice(['cash','card','online'])
    status = random.choice(['success','failed'])
    payments.append((rental_id, amount, method, status))

cursor.executemany(
    "INSERT INTO Payments (rental_id, amount, method, status) VALUES (?,?,?,?)",
    payments
)
print("Inserted payments:", len(payments))

# ----------------------------------------
# Finish
# ----------------------------------------
conn.commit()
conn.close()
print("All data inserted successfully!")
