-- Question 1: What are the total sales (quantity * unit price) by category?
SELECT p.Category, SUM(od.Quantity * p.UnitPrice) AS TotalSales
FROM OrderDetails od
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY p.Category;

-- Question 2: Which region has the highest total sales?
SELECT o.Region, SUM(od.Quantity * p.UnitPrice) AS TotalSales
FROM Orders o
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY o.Region
ORDER BY TotalSales DESC
LIMIT 1;

-- Question 3: What is the average order value per customer?
SELECT c.CustomerID, c.CustomerName, AVG(od.Quantity * p.UnitPrice) AS AvgOrderValue
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY c.CustomerID, c.CustomerName;

-- Question 4: What are the top 5 products by sales quantity?
SELECT p.ProductName, SUM(od.Quantity) AS TotalQuantity
FROM OrderDetails od
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalQuantity DESC
LIMIT 5;

-- Question 5: What is the monthly sales trend for the last year?
SELECT strftime('%Y-%m', o.OrderDate) AS Month, SUM(od.Quantity * p.UnitPrice) AS TotalSales
FROM Orders o
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE o.OrderDate >= date('now', '-1 year')
GROUP BY Month
ORDER BY Month;
