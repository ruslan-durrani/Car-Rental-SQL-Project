import os
import sqlite3
from faker import Faker
import random
import datetime

# ----------------------------------------
# DATABASE PATH (IMPORTANT)
# ----------------------------------------
db_path = "/Users/ruslanbabar/Downloads/SQL-Assignment/Car_Rental_SQL_Project/Car-Rental-SQL-Project/Database - SQL/car_rental.db"
print("Using DB:", os.path.abspath(db_path))

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
print("Connected successfully.")

fake = Faker()

# ----------------------------------------
# Random date generator
# ----------------------------------------
def random_date(start_year=2022, end_year=2025):
    start = datetime.date(start_year, 1, 1)
    end = datetime.date(end_year, 12, 31)
    delta = end - start
    return start + datetime.timedelta(days=random.randrange(delta.days))

# ----------------------------------------
# Branches
# ----------------------------------------
branches = [
    (fake.company(), fake.city(), random.choice([1,2,3,4,5, None]))
    for _ in range(30)
]

cursor.executemany(
    "INSERT INTO Branches (branch_name, city, rating) VALUES (?,?,?)",
    branches
)
print("Inserted branches:", len(branches))

# ----------------------------------------
# Customers
# ----------------------------------------
emails_used = set()
customers = []

for _ in range(300):
    email = fake.email()
    while email in emails_used:
        email = fake.email()
    emails_used.add(email)

    customers.append((
        fake.first_name(),
        fake.last_name(),
        email,
        fake.phone_number() if random.random() > 0.10 else None,
        random.choice(['Bronze','Silver','Gold'])
    ))

cursor.executemany(
    "INSERT INTO Customers (first_name, last_name, email, phone, membership_tier) VALUES (?,?,?,?,?)",
    customers
)
print("Inserted customers:", len(customers))

# ----------------------------------------
# Cars
# ----------------------------------------
car_makes = ["Toyota","Ford","BMW","Audi","Mercedes","Honda","Nissan"]
car_models = ["Corolla","Civic","A3","A4","X5","Fiesta","Focus","Camry","Accord"]

cars = [
    (
        random.choice(car_makes),
        random.choice(car_models),
        random.randint(2005, 2024),
        round(random.uniform(0, 200000), 2),
        round(random.uniform(20, 150), 2),
        random.choice(['Available','Rented','Maintenance'])
    )
    for _ in range(200)
]

cursor.executemany(
    "INSERT INTO Cars (make, model, year, mileage, daily_rate, status) VALUES (?,?,?,?,?,?)",
    cars
)
print("Inserted cars:", len(cars))

# ----------------------------------------
# Car Location
# ----------------------------------------
car_locations = [
    (car_id, random.randint(1, len(branches)))
    for car_id in range(1, len(cars)+1)
]

cursor.executemany(
    "INSERT INTO Car_Location (car_id, branch_id) VALUES (?,?)",
    car_locations
)
print("Inserted car-location links:", len(car_locations))

# ----------------------------------------
# Rentals
# ----------------------------------------
rentals = []
for _ in range(1200):
    rental_date = random_date()

    if random.random() < 0.10:
        return_date = None
        duration = 0
    else:
        return_date = rental_date + datetime.timedelta(days=random.randint(1, 14))
        duration = (return_date - rental_date).days

    rentals.append((
        random.randint(1, 300),
        random.randint(1, 200),
        rental_date.isoformat(),
        return_date.isoformat() if return_date else None,
        duration,
        round(random.uniform(20, 1800), 2)
    ))

cursor.executemany(
    "INSERT INTO Rentals (customer_id, car_id, rental_date, return_date, rental_duration_days, total_cost) VALUES (?,?,?,?,?,?)",
    rentals
)
print("Inserted rentals:", len(rentals))

# ----------------------------------------
# Payments
# ----------------------------------------
cursor.execute("SELECT rental_id FROM Rentals")
rental_ids = [row[0] for row in cursor.fetchall()]

payments = [
    (
        rid,
        round(random.uniform(10, 1800), 2),
        random.choice(['cash','card','online']),
        random.choice(['success','failed'])
    )
    for rid in rental_ids
]

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
