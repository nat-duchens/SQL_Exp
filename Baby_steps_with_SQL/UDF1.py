## UDF User Define Function

## Import the library

import sqlite3
import pandas as pd

## Define the function we want to use

square = lambda n : n*n 
print(square(10))

## Use "with", context manager, to create the "conn" variable to establish the connection and then close it automatically

with sqlite3.connect(r"C:\Users\HP\Documents\SQL_Exp\Northwind.db") as conn: 
    conn.create_function("square",1,square)
    cursor = conn.cursor()
    cursor.execute('SELECT *, square(Price) FROM Products')
    results = cursor.fetchall()
    results_df = pd.DataFrame(results)

print(results_df)
    



