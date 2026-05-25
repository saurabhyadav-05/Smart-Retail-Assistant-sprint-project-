import pandas as pd
import joblib

df = pd.read_csv("data/Walmart_Sales.csv")

df["Date"] = pd.to_datetime(df["Date"],format="%d-%m-%Y")

df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Week"] = df["Date"].dt.isocalendar().week
df["DayOfWeek"] = df["Date"].dt.dayofweek


forecast_model = joblib.load(
    "app/models/forecast_model.pkl"
)

anomaly_model = joblib.load(
    "app/models/anomaly_model.pkl"
)


forecast_features = [
    "Store",
    "Holiday_Flag",
    "Temperature",
    "Fuel_Price",
    "CPI",
    "Unemployment",
    "Year",
    "Month",
    "Day",
    "Week",
    "DayOfWeek"
]


df["Forecasted_Sales"] = (forecast_model.predict(df[forecast_features]))


anomaly_features = [
    "Weekly_Sales",
    "Temperature",
    "Fuel_Price",
    "CPI",
    "Unemployment"
]


df["Anomaly"] = (anomaly_model.predict(df[anomaly_features]))

df.to_csv("enhanced_walmart_sales.csv",index=False)

print("Enhanced dataset generated successfully!")