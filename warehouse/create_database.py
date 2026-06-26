import sqlite3
from pathlib import Path


def create_database():
    """
    Creates the SQLite database and executes the schema.sql file.
    """

    base_dir = Path(__file__).resolve().parent

    db_path = base_dir / "sales_dw.db"
    schema_path = base_dir / "schema.sql"

    conn = sqlite3.connect(db_path)

    with open(schema_path, "r") as file:
        schema = file.read()

    conn.executescript(schema)

    conn.commit()
    conn.close()

    print("Database created successfully!")


if __name__ == "__main__":
    create_database()