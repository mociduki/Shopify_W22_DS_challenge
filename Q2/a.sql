--How many orders were shipped by Speedy Express in total?

SELECT COUNT(*), ShipperName FROM Orders INNER JOIN Shippers ON Orders.ShipperID=Shippers.ShipperID GROUP BY ShipperName;

--The line above shows a table for number of orders for all shipping methods.
--The answer, number of orders with Speedy Express is 54.
