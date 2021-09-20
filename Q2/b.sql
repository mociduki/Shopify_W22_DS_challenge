-- What is the last name of the employee with the most orders?

SELECT COUNT(OrderID) as nOrders, Orders.EmployeeID, LastName 
FROM Orders INNER JOIN Employees on Orders.EmployeeID=Employees.EmployeeID 
GROUP BY Orders.EmployeeID
ORDER BY nOrders desc;

-- The code above will show a table with nOrders (number of orders) along with the employee and their LastName. The answer for this question is 'Peacock'.
