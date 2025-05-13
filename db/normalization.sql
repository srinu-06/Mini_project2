-- Normalization of the dataset into 3NF

--- Create table for Regions (to remove transitive dependency)
CREATE TABLE Regions (
    RegionID INTEGER PRIMARY KEY AUTOINCREMENT,
    Region TEXT UNIQUE,
    Country TEXT
);

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

-- Create table for Orders with foreign key to RegionID
CREATE TABLE Orders (
    OrderID TEXT PRIMARY KEY,
    OrderDate DATE,
    CustomerID TEXT,
    RegionID INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (RegionID) REFERENCES Regions(RegionID)
);

-- Create table for OrderDetails (composite primary key)
CREATE TABLE OrderDetails (
    OrderID TEXT,
    ProductID TEXT,
    Quantity INTEGER,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
