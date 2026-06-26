import pandas as pd
from pathlib import Path


def extract_data():
    """
    Extracts the raw sales data from the CSV file.
    """

    project_dir = Path(__file__).resolve().parent.parent
    csv_path = project_dir / "data" / "raw" / "train.csv"

    df = pd.read_csv(csv_path)

    print("\n========== EXTRACT ==========")
    print("Data extracted successfully!")
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    return df