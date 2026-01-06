import pandas as pd
import mysql.connector
from statsmodels.tsa.arima.model import ARIMA

from src.db_config import DB_CONFIG
from src.load_data import load_monthly_sales


def generate_forecast():
    # Load full historical data
    df = load_monthly_sales()

    # Train final ARIMA model on full data
    model = ARIMA(df["total_sales"], order=(1, 0, 1))
    model_fit = model.fit()

    # Forecast next 6 months
    forecast = model_fit.forecast(steps=6)

    future_months = pd.date_range(
        start=df["month"].iloc[-1] + pd.offsets.MonthBegin(1),
        periods=6,
        freq="MS"
    )

    forecast_df = pd.DataFrame({
        "month": future_months,
        "forecast_sales": forecast.values
    })

    # Round for business use (no fake precision)
    forecast_df["forecast_sales"] = forecast_df["forecast_sales"].round(0).astype(int)

    return forecast_df


def write_forecast_to_mysql(forecast_df):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS arima_forecast (
            month DATE,
            forecast_sales DECIMAL(12,2)
        )
    """)

    # Clear old forecasts
    cursor.execute("DELETE FROM arima_forecast")

    # Insert new forecast
    for _, row in forecast_df.iterrows():
        cursor.execute(
            "INSERT INTO arima_forecast (month, forecast_sales) VALUES (%s, %s)",
            (row["month"].date(), float(row["forecast_sales"]))
        )

    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    forecast_df = generate_forecast()
    write_forecast_to_mysql(forecast_df)

    print("ARIMA forecast successfully written to MySQL")
    print(forecast_df)
