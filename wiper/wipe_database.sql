DELETE FROM Payments;
DELETE FROM Rentals;
DELETE FROM Car_Location;
DELETE FROM Cars;
DELETE FROM Branches;
DELETE FROM Customers;

VACUUM;   -- optional: compacts DB
