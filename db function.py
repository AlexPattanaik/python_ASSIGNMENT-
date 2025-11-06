import sqlite3
import pandas as pd

conn = sqlite3.connect("./sales_data.db")

def total_records():
    query = "SELECT COUNT(*) AS total_records FROM sales_table"
    result = pd.read_sql_query(query, conn)
    return result.iloc[0]['total_records']

def total_sales_by_region():
    query = """
    SELECT region, SUM(total_sales) AS total_sales_amount
    FROM sales_table
    GROUP BY region
    """
    return pd.read_sql_query(query, conn)

def avg_sales_per_transaction():
    query = "SELECT AVG(net_sale) AS avg_sales_per_transaction FROM sales_table"
    result = pd.read_sql_query(query, conn)
    return result.iloc[0]['avg_sales_per_transaction']

def duplicate_order_ids():
    query = """
    SELECT OrderId, COUNT(*) AS count
    FROM sales_table
    GROUP BY OrderId
    HAVING COUNT(*) > 1
    """
    df = pd.read_sql_query(query, conn)
    if df.empty:
        return "No duplicate OrderId values found."
    else:
        return df


print("Total Records:", total_records())
print("\nTotal Sales by Region:\n", total_sales_by_region())
print("\nAverage Sales Per Transaction:", avg_sales_per_transaction())
print("\nDuplicate Order IDs:\n", duplicate_order_ids())