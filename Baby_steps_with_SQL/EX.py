## Import libraries

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

## establish connection with DB

conn = sqlite3.connect(r"C:\Users\HP\Documents\SQL_Exp\Northwind.db")

## query of the most profitable product

query = ''' 
    SELECT * FROM OrderDetails as od
  
'''

show_table = pd.read_sql_query(query, conn)

print(show_table)