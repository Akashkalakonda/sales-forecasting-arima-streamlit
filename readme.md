📊 Sales Forecasting & Decision Support System

MySQL · ARIMA · Streamlit · Time Series Analysis

🔍 Project Overview

This project is an end-to-end sales forecasting and decision-support system built using time-series analysis (ARIMA) and an interactive Streamlit dashboard.

The system enables stakeholders to:

Analyze historical sales trends

Generate accurate short-term demand forecasts

Interactively explore scenarios using user controls

Support inventory planning, revenue forecasting, and business decisions

The project demonstrates a production-style analytics pipeline, from data modeling to deployment-ready visualization.

🎯 Business Problem

E-commerce businesses need reliable short-term demand forecasting to:

Avoid overstocking or stockouts

Plan inventory and procurement

Estimate near-term revenue

Make data-driven operational decisions

Static dashboards or spreadsheets are often insufficient.
This project addresses the gap by delivering an interactive, scenario-based forecasting tool.

🧠 Solution Summary

Designed a structured sales database using MySQL

Applied ARIMA time-series models for demand forecasting

Achieved ~97% forecast accuracy (MAPE-based)

Built an interactive Streamlit application with:

Dynamic date filters

Adjustable forecast horizon

Interactive plots and KPIs

Prepared the system for free cloud deployment

📦 Dataset

Amazon Sales Dataset (Synthetic, Realistic E-commerce Data)

~100,000 Amazon-style transactions

Includes orders, pricing, discounts, taxes, delivery status

Simulates real-world e-commerce sales behavior

Suitable for analytics, forecasting, and BI use cases

🔗 Dataset link:
https://www.kaggle.com/datasets/rohiteng/amazon-sales-dataset

⚠️ Note: The dataset is synthetic but designed to reflect realistic business patterns.


🏗️ Project Architecture

Raw Sales Data (CSV)
        ↓
MySQL Database
  ├─ clean_sales
  ├─ monthly_sales
  └─ arima_forecast
        ↓
Python (ARIMA Modeling)
        ↓
Streamlit Application
  ├─ Interactive Charts
  ├─ Dynamic KPIs
  └─ Scenario Controls

🧰 Tech Stack

| Layer                | Tools                     |
| -------------------- | ------------------------- |
| Database             | MySQL                     |
| Data Processing      | Python, Pandas, NumPy     |
| Time-Series Modeling | ARIMA (statsmodels)       |
| Visualization        | Plotly                    |
| App Framework        | Streamlit                 |
| Deployment           | Streamlit Community Cloud |


📈 Modeling Approach
1️⃣ Time-Series Exploration

Visualized historical trends and seasonality

Performed ADF stationarity test

Identified that the series is stationary (d = 0)

2️⃣ ARIMA Modeling

Selected ARIMA(1,0,1) based on diagnostics

Used a train–test split (last 6 months as holdout)

Evaluated performance using MAPE

3️⃣ Forecast Accuracy

MAPE ≈ 3%

Forecast accuracy ≈ 97%

Forecast accuracy is calculated honestly using holdout validation.


🎛️ Streamlit Application Features
✅ Interactive Controls

Historical date range selection

Forecast horizon slider (3–12 months)

Toggle forecast visibility

📊 Visualizations

Actual vs Forecast interactive line chart

Forecast-only chart for short-term planning

Hover, zoom, and pan enabled (Plotly)

📌 Dynamic KPIs

Average monthly sales (selected period)

Forecasted sales (selected horizon)

Expected demand change (%)

Forecast horizon

Model accuracy (transparent)

🧠 Decision Insights

Interpretable business narrative

Designed for non-technical stakeholders

🚀 Deployment Strategy
Free Deployment (Current)

Deployed using Streamlit Community Cloud

Uses CSV-backed data for public demo

Database-backed version runs locally

This hybrid approach keeps the app free, portable, and interview-friendly.

🧪 Key Learnings

Importance of stationarity testing before ARIMA

Separating exploration notebooks from production code

Designing state-driven interactive applications

Translating ML outputs into business decisions

Handling real-world deployment constraints

📌 Future Enhancements

Connect to cloud-hosted MySQL (PlanetScale / Railway)

Add scenario comparison (multiple forecast horizons)

Enable forecast download as CSV

Add authentication for restricted access

Deploy as a Dockerized service

🙌 Acknowledgements

Kaggle community for dataset

Statsmodels & Streamlit open-source contributors