import sqlite3
from pathlib import Path


def load_to_database(
    dim_product,
    dim_customer,
    dim_date,
    dim_location,
    fact_sales
):
    """
    Loads all transformed tables into the SQLite warehouse.
    """

    db_path = (
        Path(__file__).resolve().parent.parent
        / "warehouse"
        / "sales_dw.db"
    )

    conn = sqlite3.connect(db_path)

    print("\n========== LOAD ==========")

    # Load Dimension Tables
    dim_product.to_sql(
        "Dim_Product",
        conn,
        if_exists="replace",
        index=False
    )

    dim_customer.to_sql(
        "Dim_Customer",
        conn,
        if_exists="replace",
        index=False
    )

    dim_date.to_sql(
        "Dim_Date",
        conn,
        if_exists="replace",
        index=False
    )

    dim_location.to_sql(
        "Dim_Location",
        conn,
        if_exists="replace",
        index=False
    )

    # Load Fact Table
    fact_sales.to_sql(
        "Fact_Sales",
        conn,
        if_exists="replace",
        index=False
    )

    conn.commit()
    conn.close()

    print("Data loaded successfully!")