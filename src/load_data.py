import pandas as pd
import mysql.connector
from src.db_config import DB_CONFIG

def load_monthly_sales():
    connection = mysql.connector.connect(**DB_CONFIG)

    query = """
    SELECT month, total_sales
    FROM monthly_sales
    ORDER BY month
    """

    df = pd.read_sql(query, connection)
    connection.close()

    df["month"] = pd.to_datetime(df["month"])
    return df


if __name__ == "__main__":
    df = load_monthly_sales()

    print("Data loaded successfully")
    print(df.head())
    print("\nRows:", df.shape[0])
    print("Date range:", df["month"].min(), "to", df["month"].max())
