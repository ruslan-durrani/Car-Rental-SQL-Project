import sqlite3

db_path = "/Users/ruslanbabar/Downloads/SQL-Assignment/Car_Rental_SQL_Project/car_rental.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("=== TEST: Tables exist ===")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

print("\n=== TEST: Count rows ===")
tables = ["Customers", "Branches", "Cars", "Car_Location", "Rentals", "Payments"]
for table in tables:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"{table}: {count}")

print("\n=== TEST: Foreign keys ===")
cursor.execute("PRAGMA foreign_key_check;")
fk_errors = cursor.fetchall()
print("Foreign key errors:", fk_errors)

print("\n=== TEST: Sample rows from Rentals ===")
cursor.execute("SELECT * FROM Rentals LIMIT 5;")
for row in cursor.fetchall():
    print(row)

conn.close()
print("\nAll database tests completed.")
