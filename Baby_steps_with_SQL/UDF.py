## UDF User Define Function

## Import the library

import sqlite3
import pandas as pd

## Define the function we want to use

square = lambda n : n*n 
print(square(10))

## Variable that calls the module and connects it to the DB

conn = sqlite3.connect(r"C:\Users\HP\Documents\SQL_Exp\Northwind.db")

## Register the function in SQLite
# First the name of the function ""
# How many parameters ask the function
# Wich function of python are you goin to use to create the function

conn.create_function("square",1, square)

## Create something that allows us to make a Query
# In python "cursor" are objects that allows querys in DB with a function

# Connection method

cursor = conn.cursor()

## The function "execute" makes a query
# It is a Transaction, the BEGIN is implicit

cursor.execute('''
    SELECT * FROM Products
    ''')

## Create a variable to check the query using "fetchall"
# fetchall returns a list of tuples

results = cursor.fetchall()
results_df = pd.DataFrame(results)

# "commit" to confirm the transaction and save the changes

conn.commit()

# Use "rollback" to revert changes since the last commit 

## Now I have a system that opens a connection, make a query,
# save the data, close the cursor and close the connection,
# and free up the resources

cursor.close()
conn.close()

print(results_df)

