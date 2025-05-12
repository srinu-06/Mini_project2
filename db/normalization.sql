-- Normalization of the dataset into 3NF

-- Create table for Customers
CREATE TABLE Customers (
    CustomerID TEXT PRIMARY KEY,
    CustomerName TEXT,
    CustomerEmail TEXT
);

-- Create table for Products
CREATE TABLE Products (
    ProductID TEXT PRIMARY KEY,
    ProductName TEXT,
    Category TEXT,
    UnitPrice REAL
);

-- Create Orders table with Region and Country
CREATE TABLE Orders (
    OrderID TEXT PRIMARY KEY,
    OrderDate DATE,
    CustomerID TEXT,
    Region TEXT,
    Country TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create OrderDetails table for product details in orders
CREATE TABLE OrderDetails (
    OrderID TEXT,
    ProductID TEXT,
    Quantity INTEGER,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
