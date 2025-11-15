import sqlite3

db_path = "car_rental.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

tables = ["Payments", "Rentals", "Car_Location", "Cars", "Branches", "Customers"]

for table in tables:
    cursor.execute(f"DELETE FROM {table};")
    print(f"Cleared table: {table}")

conn.commit()
conn.close()
print("Database reset complete.")
