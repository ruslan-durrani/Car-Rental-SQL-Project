PRAGMA foreign_keys = ON;

CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    membership_tier TEXT CHECK(membership_tier IN ('Bronze','Silver','Gold'))
);

CREATE TABLE Branches (
    branch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    branch_name TEXT NOT NULL,
    city TEXT NOT NULL,
    rating INTEGER CHECK(rating >= 1 AND rating <= 5)
);

CREATE TABLE Cars (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    year INTEGER CHECK(year >= 2000),
    mileage REAL CHECK(mileage >= 0),
    daily_rate REAL CHECK(daily_rate >= 0),
    status TEXT CHECK(status IN ('Available','Rented','Maintenance'))
);

CREATE TABLE Car_Location (
    car_id INTEGER,
    branch_id INTEGER,
    PRIMARY KEY (car_id, branch_id),
    FOREIGN KEY (car_id) REFERENCES Cars(car_id),
    FOREIGN KEY (branch_id) REFERENCES Branches(branch_id)
);

CREATE TABLE Rentals (
    rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    car_id INTEGER,
    rental_date TEXT NOT NULL,
    return_date TEXT,
    rental_duration_days INTEGER CHECK(rental_duration_days >= 0),
    total_cost REAL CHECK(total_cost >= 0),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (car_id) REFERENCES Cars(car_id)
);

CREATE TABLE Payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rental_id INTEGER,
    amount REAL CHECK(amount >= 0),
    method TEXT CHECK(method IN ('cash','card','online')),
    status TEXT CHECK(status IN ('success','failed')),
    FOREIGN KEY (rental_id) REFERENCES Rentals(rental_id)
);
