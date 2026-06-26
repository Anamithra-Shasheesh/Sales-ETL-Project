from extract import extract_data

from transform import (
    transform_data,
    create_product_dimension,
    create_customer_dimension,
    create_date_dimension,
    create_location_dimension,
    create_fact_sales,
)

from load import load_to_database


def run_pipeline():

    print("=" * 50)
    print("SALES ETL PIPELINE")
    print("=" * 50)

    # -----------------------------
    # Extract
    # -----------------------------
    df = extract_data()

    # -----------------------------
    # Transform
    # -----------------------------
    clean_df = transform_data(df)

    dim_product = create_product_dimension(clean_df)
    dim_customer = create_customer_dimension(clean_df)
    dim_date = create_date_dimension(clean_df)
    dim_location = create_location_dimension(clean_df)

    fact_sales = create_fact_sales(
        clean_df,
        dim_date,
        dim_location
    )

    # -----------------------------
    # Load
    # -----------------------------
    load_to_database(
        dim_product,
        dim_customer,
        dim_date,
        dim_location,
        fact_sales
    )

    print("\nETL Pipeline Completed Successfully!")


if __name__ == "__main__":
    run_pipeline()