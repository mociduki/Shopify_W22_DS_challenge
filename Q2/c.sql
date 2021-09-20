-- What product was ordered the most by customers in Germany?

-- There could be multiple answers depending on how the most sold is defined.

-- The product ordered the most based on the number of quantities.
SELECT SUM(Quantity) as SumQuantity,ProductID,Country
FROM Orders
INNER JOIN OrderDetails ON OrderDetails.OrderID=Orders.OrderID
INNER JOIN Customers ON Customers.CustomerID=Orders.CustomerID
WHERE Country='Germany'
GROUP BY ProductID
ORDER BY SumQuantity desc;

-- According to this criteria, the product ordered the most was productID 40 with the quantity of 160 sold.

-- The product ordered the most based on the number of (different) customers
SELECT COUNT(DISTINCT Orders.CustomerID) as SumCustomers,ProductID,Country
FROM Orders
INNER JOIN OrderDetails ON OrderDetails.OrderID=Orders.OrderID
INNER JOIN Customers ON Customers.CustomerID=Orders.CustomerID
WHERE Country='Germany'
GROUP BY ProductID
ORDER BY SumCustomers desc; 

-- According to this criteria, the product ordered the most was productID 31 ordered by 5 customers.
