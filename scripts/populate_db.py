# Refine the script for better readability, error handling, and output clarity
import sqlite3
import pandas as pd

# Update the data path to use the absolute path
data_path = '/Users/srinutummalapalli/Desktop/mini project 2/data/non_normalized_sales_data.csv'
df = pd.read_csv(data_path)

# Update the database path to use the absolute path
db_path = '/Users/srinutummalapalli/Desktop/mini project 2/db/sales_data.db'

try:
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Populate Customers table
    customers = df[['CustomerID', 'CustomerName', 'CustomerEmail', 'Region', 'Country']].drop_duplicates()
    customers.to_sql('Customers', conn, if_exists='replace', index=False)

    # Populate Products table
    products = df[['ProductID', 'ProductName', 'Category', 'UnitPrice']].drop_duplicates()
    products.to_sql('Products', conn, if_exists='replace', index=False)

    # Populate Orders table with Region and Country
    orders = df[['OrderID', 'OrderDate', 'CustomerID', 'Region', 'Country']].drop_duplicates()
    orders.to_sql('Orders', conn, if_exists='replace', index=False)

    # Populate OrderDetails table
    order_details = df[['OrderID', 'ProductID', 'Quantity']]
    order_details.to_sql('OrderDetails', conn, if_exists='replace', index=False)

    # Implement SQL queries using Pandas

    # Question 1: Total sales by category
    print("\nQuestion 1: Total Sales by Category")
    query1 = """
    SELECT p.Category, SUM(od.Quantity * p.UnitPrice) AS TotalSales
    FROM OrderDetails od
    JOIN Products p ON od.ProductID = p.ProductID
    GROUP BY p.Category;
    """
    result1 = pd.read_sql_query(query1, conn)
    print(result1.to_string(index=False))

    # Question 2: Region with the highest total sales
    print("\nQuestion 2: Region with the Highest Total Sales")
    query2 = """
    SELECT o.Region, SUM(od.Quantity * p.UnitPrice) AS TotalSales
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    GROUP BY o.Region
    ORDER BY TotalSales DESC
    LIMIT 1;
    """
    result2 = pd.read_sql_query(query2, conn)
    print(result2.to_string(index=False))

    # Question 3: Average order value per customer
    print("\nQuestion 3: Average Order Value per Customer")
    query3 = """
    SELECT c.CustomerID, c.CustomerName, AVG(od.Quantity * p.UnitPrice) AS AvgOrderValue
    FROM Customers c
    JOIN Orders o ON c.CustomerID = o.CustomerID
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    GROUP BY c.CustomerID, c.CustomerName;
    """
    result3 = pd.read_sql_query(query3, conn)
    print(result3.to_string(index=False))

    # Question 4: Top 5 products by sales quantity
    print("\nQuestion 4: Top 5 Products by Sales Quantity")
    query4 = """
    SELECT p.ProductName, SUM(od.Quantity) AS TotalQuantity
    FROM OrderDetails od
    JOIN Products p ON od.ProductID = p.ProductID
    GROUP BY p.ProductName
    ORDER BY TotalQuantity DESC
    LIMIT 5;
    """
    result4 = pd.read_sql_query(query4, conn)
    print(result4.to_string(index=False))

    # Question 5: Monthly sales trend for the last year
    print("\nQuestion 5: Monthly Sales Trend for the Last Year")
    query5 = """
    SELECT strftime('%Y-%m', o.OrderDate) AS Month, SUM(od.Quantity * p.UnitPrice) AS TotalSales
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Products p ON od.ProductID = p.ProductID
    WHERE o.OrderDate >= date('now', '-1 year')
    GROUP BY Month
    ORDER BY Month;
    """
    result5 = pd.read_sql_query(query5, conn)
    print(result5.to_string(index=False))

    print("\nDatabase populated and queries executed successfully.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()
