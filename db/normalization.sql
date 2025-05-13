-- Final 3NF Normalized SQL Schema

-- Table for unique Regions and their Countries
CREATE TABLE Regions (
    RegionID INTEGER PRIMARY KEY AUTOINCREMENT,
    Region TEXT NOT NULL UNIQUE,
    Country TEXT NOT NULL,
    UNIQUE (Region, Country)
);

-- Table for storing Customers
CREATE TABLE Customers (
    CustomerID TEXT PRIMARY KEY,
    CustomerName TEXT NOT NULL,
    CustomerEmail TEXT NOT NULL UNIQUE
);

-- Table for storing Product catalog
CREATE TABLE Products (
    ProductID TEXT PRIMARY KEY,
    ProductName TEXT NOT NULL,
    Category TEXT NOT NULL,
    UnitPrice REAL NOT NULL CHECK (UnitPrice >= 0)
);

-- Table for Orders referencing Region and Customer
CREATE TABLE Orders (
    OrderID TEXT PRIMARY KEY,
    OrderDate DATE NOT NULL,
    CustomerID TEXT NOT NULL,
    RegionID INTEGER NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (RegionID) REFERENCES Regions(RegionID)
);

-- Table for Order Details (composite key per line item)
CREATE TABLE OrderDetails (
    OrderID TEXT,
    ProductID TEXT,
    Quantity INTEGER NOT NULL CHECK (Quantity > 0),
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
