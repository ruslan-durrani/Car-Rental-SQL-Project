-- Test 1
SELECT name FROM sqlite_master WHERE type='table';

-- Test 2
SELECT 'Customers', COUNT(*) FROM Customers
UNION ALL
SELECT 'Branches', COUNT(*) FROM Branches
UNION ALL
SELECT 'Cars', COUNT(*) FROM Cars
UNION ALL
SELECT 'Car_Location', COUNT(*) FROM Car_Location
UNION ALL
SELECT 'Rentals', COUNT(*) FROM Rentals
UNION ALL
SELECT 'Payments', COUNT(*) FROM Payments;


-- Test 3
PRAGMA foreign_key_check;

-- Test 4
SELECT rental_id 
FROM Rentals 
WHERE customer_id NOT IN (SELECT customer_id FROM Customers)
   OR car_id NOT IN (SELECT car_id FROM Cars);

-- Test 5
SELECT car_id, COUNT(*) 
FROM Car_Location
GROUP BY car_id
HAVING COUNT(*) > 1;

