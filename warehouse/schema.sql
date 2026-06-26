-- ===========================================
-- Product Dimension Table
-- ===========================================

CREATE TABLE IF NOT EXISTS Dim_Product (
    Product_ID TEXT PRIMARY KEY,
    Product_Name TEXT NOT NULL,
    Category TEXT NOT NULL,
    Sub_Category TEXT NOT NULL
);

-- ===========================================
-- Customer Dimension Table
-- ===========================================

CREATE TABLE IF NOT EXISTS Dim_Customer (
    Customer_ID TEXT PRIMARY KEY,
    Customer_Name TEXT NOT NULL,
    Segment TEXT NOT NULL
);

-- ===========================================
-- Date Dimension Table
-- ===========================================

CREATE TABLE IF NOT EXISTS Dim_Date (
    Date_ID INTEGER PRIMARY KEY,
    Order_Date TEXT NOT NULL,
    Month INTEGER NOT NULL,
    Quarter INTEGER NOT NULL,
    Year INTEGER NOT NULL
);

-- ===========================================
-- Location Dimension Table
-- ===========================================

CREATE TABLE IF NOT EXISTS Dim_Location (
    Location_ID INTEGER PRIMARY KEY,
    Country TEXT NOT NULL,
    Region TEXT NOT NULL,
    State TEXT NOT NULL,
    City TEXT NOT NULL,
    Postal_Code TEXT
);

-- ===========================================
-- Sales Fact Table
-- ===========================================

CREATE TABLE IF NOT EXISTS Fact_Sales (
    Order_ID TEXT PRIMARY KEY,
    Product_ID TEXT NOT NULL,
    Customer_ID TEXT NOT NULL,
    Date_ID INTEGER NOT NULL,
    Location_ID INTEGER NOT NULL,
    Ship_Mode TEXT NOT NULL,
    Sales REAL NOT NULL,

    FOREIGN KEY (Product_ID) REFERENCES Dim_Product(Product_ID),
    FOREIGN KEY (Customer_ID) REFERENCES Dim_Customer(Customer_ID),
    FOREIGN KEY (Date_ID) REFERENCES Dim_Date(Date_ID),
    FOREIGN KEY (Location_ID) REFERENCES Dim_Location(Location_ID)
);