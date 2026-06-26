# Sales ETL Project

## Overview

A simple ETL (Extract, Transform, Load) pipeline using Python and SQLite. Raw sales dataset cleaned, transformed into a star schema, loaded into a SQLite database, and visualized using Power BI. This project uses the publicly available Sample Superstore Sales dataset from Kaggle.

## Features

* Extracts data from a CSV file
* Cleans and transforms the data using Pandas
* Loads the transformed data into a SQLite data warehouse
* Creates an interactive Power BI dashboard

## Technologies Used

* Python
* Pandas
* NumPy
* SQLite
* SQL
* Power BI

## Project Structure

```text
Sales-ETL-Project/
│
├── data/
├── etl/
├── warehouse/
├── dashboard/
├── README.md
└── .gitignore
```

## How to Run

1. Create the SQLite database.

```bash
python warehouse/create_database.py
```

2. Run the ETL pipeline.

```bash
python etl/etl_pipeline.py
```

3. Open the Power BI dashboard (`Sales_ETL_Dashboard.pbix`) to view the visualizations.

## Future Improvements
* Automate the ETL pipeline using Apache Airflow
* Add more dashboard reports
