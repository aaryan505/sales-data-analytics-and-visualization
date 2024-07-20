import pandas as pd
import sqlite3

# Connect to SQLite database (assuming a database named 'sales.db')
conn = sqlite3.connect('sales.db')

# SQL query to extract sales data
query = '''
SELECT *
FROM sales_data
'''
# Load data into a DataFrame
sales_data = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Data Cleaning
# Handle missing values
sales_data.dropna(inplace=True)

# Remove duplicates
sales_data.drop_duplicates(inplace=True)

# Correct data types if necessary
sales_data['date'] = pd.to_datetime(sales_data['date'])
