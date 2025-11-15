-- Test 6
SELECT COUNT(*) 
FROM Rentals 
WHERE return_date IS NULL;

-- Test 7
SELECT * FROM Cars WHERE mileage < 0;

-- Test 8
SELECT * FROM Branches WHERE rating < 1 OR rating > 5;

-- Test 9
SELECT * FROM Payments 
WHERE rental_id NOT IN (SELECT rental_id FROM Rentals);
