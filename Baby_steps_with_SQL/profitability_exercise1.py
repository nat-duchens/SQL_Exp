## Import libraries

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

## Establish connection with DB

conn = sqlite3.connect(r"C:\Users\HP\Documents\SQL_Exp\Northwind.db")

## Query of the most profitable product

query = ''' 
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails as od
    JOIN Products as p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''
## Show the table

top_products = pd.read_sql_query(query, conn)

# print(top_products)

## Make a graphic of the table

top_products.plot(x="ProductName" , kind="bar" ,figsize=(10,5),legend=False)

plt.title("The 10 most profitable products")
plt.xlabel("Products (qty)")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=90)
plt.show()

####

## Query which of the employees is the most efficient

# || "" "" || to concatenate in SQLite
query2 = '''
    SELECT FirstName || " " || LastName as Employee, COUNT(*) as TotalOrders
    FROM Orders as o
    JOIN Employees as e
    ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY TotalOrders DESC
'''

results = pd.read_sql_query(query2, conn)
print(results)


top_employees = pd.read_sql_query(query2,conn)
top_employees.plot(x="Employee" , y="TotalOrders" ,kind="bar", figsize=(10,5),legend=False)

plt.title("Top 10 most efficient employees")
plt.xlabel("Employees")
plt.ylabel("Total sold")
plt.xticks(rotation = 45)

plt.show()