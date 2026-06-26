import pandas as pd


def transform_data(df):
    """
    Cleans the raw dataset.
    """

    print("\n========== TRANSFORM ==========")

    df = df.copy()

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Remove rows with missing values
    df.dropna(inplace=True)

    # Convert Order Date
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True
    )

    print("Data transformed successfully!")

    return df


# --------------------------------------------------
# Product Dimension
# --------------------------------------------------

def create_product_dimension(df):

    dim_product = (
        df[
            [
                "Product ID",
                "Product Name",
                "Category",
                "Sub-Category"
            ]
        ]
        .drop_duplicates(subset=["Product ID"])
        .reset_index(drop=True)
    )

    dim_product.columns = [
        "Product_ID",
        "Product_Name",
        "Category",
        "Sub_Category"
    ]

    return dim_product


# --------------------------------------------------
# Customer Dimension
# --------------------------------------------------

def create_customer_dimension(df):

    dim_customer = (
        df[
            [
                "Customer ID",
                "Customer Name",
                "Segment"
            ]
        ]
        .drop_duplicates(subset=["Customer ID"])
        .reset_index(drop=True)
    )

    dim_customer.columns = [
        "Customer_ID",
        "Customer_Name",
        "Segment"
    ]

    return dim_customer


# --------------------------------------------------
# Date Dimension
# --------------------------------------------------

def create_date_dimension(df):

    dim_date = (
        df[
            ["Order Date"]
        ]
        .drop_duplicates()
        .sort_values("Order Date")
        .reset_index(drop=True)
    )

    dim_date["Date_ID"] = dim_date.index + 1

    dim_date["Month"] = dim_date["Order Date"].dt.month
    dim_date["Quarter"] = dim_date["Order Date"].dt.quarter
    dim_date["Year"] = dim_date["Order Date"].dt.year

    dim_date["Order Date"] = dim_date["Order Date"].dt.strftime("%Y-%m-%d")

    dim_date = dim_date[
        [
            "Date_ID",
            "Order Date",
            "Month",
            "Quarter",
            "Year"
        ]
    ]

    dim_date.columns = [
        "Date_ID",
        "Order_Date",
        "Month",
        "Quarter",
        "Year"
    ]

    return dim_date


# --------------------------------------------------
# Location Dimension
# --------------------------------------------------

def create_location_dimension(df):

    dim_location = (
        df[
            [
                "Country",
                "Region",
                "State",
                "City",
                "Postal Code"
            ]
        ]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    dim_location["Location_ID"] = dim_location.index + 1

    dim_location = dim_location[
        [
            "Location_ID",
            "Country",
            "Region",
            "State",
            "City",
            "Postal Code"
        ]
    ]

    dim_location.columns = [
        "Location_ID",
        "Country",
        "Region",
        "State",
        "City",
        "Postal_Code"
    ]

    return dim_location


# --------------------------------------------------
# Fact Table
# --------------------------------------------------

def create_fact_sales(df, dim_date, dim_location):

    fact = df.copy()

    fact["Order Date"] = fact["Order Date"].dt.strftime("%Y-%m-%d")

    fact = fact.merge(
        dim_date[
            [
                "Date_ID",
                "Order_Date"
            ]
        ],
        left_on="Order Date",
        right_on="Order_Date",
        how="left"
    )

    location_lookup = dim_location.copy()

    location_lookup.columns = [
        "Location_ID",
        "Country",
        "Region",
        "State",
        "City",
        "Postal Code"
    ]

    fact = fact.merge(
        location_lookup,
        on=[
            "Country",
            "Region",
            "State",
            "City",
            "Postal Code"
        ],
        how="left"
    )

    fact = fact[
        [
            "Order ID",
            "Product ID",
            "Customer ID",
            "Date_ID",
            "Location_ID",
            "Ship Mode",
            "Sales"
        ]
    ]

    fact.columns = [
        "Order_ID",
        "Product_ID",
        "Customer_ID",
        "Date_ID",
        "Location_ID",
        "Ship_Mode",
        "Sales"
    ]

    return fact