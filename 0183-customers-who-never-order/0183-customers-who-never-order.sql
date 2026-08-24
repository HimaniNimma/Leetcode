# Write your MySQL query statement below
SELECT name AS Customers 
FROM Customers c
WHERE id NOT IN(
    SELECT customerID FROM Orders
);