import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to the database
db_path = '/Users/srinutummalapalli/Desktop/mini project 2/db/sales_data.db'
conn = sqlite3.connect(db_path)

# Visualization 1: Total Sales by Category
query1 = """
SELECT p.Category, SUM(od.Quantity * p.UnitPrice) AS TotalSales
FROM OrderDetails od
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY p.Category;
"""
data1 = pd.read_sql_query(query1, conn)
data1.plot(kind='bar', x='Category', y='TotalSales', title='Total Sales by Category', legend=False)
plt.ylabel('Total Sales ($)')
plt.savefig('visuals/total_sales_by_category.png')

# Visualization 2: Region with the Highest Total Sales
query2 = """
SELECT o.Region, SUM(od.Quantity * p.UnitPrice) AS TotalSales
FROM Orders o
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
GROUP BY o.Region;
"""
data2 = pd.read_sql_query(query2, conn)
data2.plot(kind='pie', y='TotalSales', labels=data2['Region'], autopct='%1.1f%%', title='Sales Distribution by Region')
plt.ylabel('')
plt.savefig('visuals/sales_by_region.png')

# Visualization 3: Monthly Sales Trend
query3 = """
SELECT strftime('%Y-%m', o.OrderDate) AS Month, SUM(od.Quantity * p.UnitPrice) AS TotalSales
FROM Orders o
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE o.OrderDate >= date('now', '-1 year')
GROUP BY Month
ORDER BY Month;
"""
data3 = pd.read_sql_query(query3, conn)
data3.plot(kind='line', x='Month', y='TotalSales', title='Monthly Sales Trend', marker='o')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.savefig('visuals/monthly_sales_trend.png')

# Close the connection
conn.close()

print("Visualizations generated successfully.")
