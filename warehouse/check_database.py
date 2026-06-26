import sqlite3
from pathlib import Path

db_path = Path(__file__).resolve().parent / "sales_dw.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

tables = [
    "Dim_Product",
    "Dim_Customer",
    "Dim_Date",
    "Dim_Location",
    "Fact_Sales"
]

print("\n========== DATABASE TABLES ==========\n")

for table in tables:

    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]

    print(f"{table}: {count} rows")

conn.close()