from fastapi import APIRouter
from pydantic import BaseModel
from app.logger import logger

import pandas as pd
import joblib

router = APIRouter()

model = joblib.load("app/models/forecast_model.pkl")

class Input(BaseModel):

    Store: int
    Holiday_Flag: int
    Temperature: float
    Fuel_Price: float
    CPI: float
    Unemployment: float
    Year: int
    Month: int
    Day: int
    Week: int
    DayOfWeek: int


@router.post("/forecast")
def forecast_sales(data:Input):
    try:    
        logger.info("forecast prediction request received")

        input_data = pd.DataFrame([{
            "Store": data.Store,
            "Holiday_Flag": data.Holiday_Flag,
            "Temperature": data.Temperature,
            "Fuel_Price": data.Fuel_Price,
            "CPI": data.CPI,
            "Unemployment": data.Unemployment,
            "Year": data.Year,
            "Month": data.Month,
            "Day": data.Day,
            "Week": data.Week,
            "DayOfWeek": data.DayOfWeek
        }])

        prediction = model.predict(input_data)
        logger.info(f"Forecast prediction generated: {prediction}")

        return {"predicted_weekly_sales": round(prediction[0],3)}

    except Exception as e:
        logger.error(f"Forecast API Error: {str(e)}")
        return {"error":"Something went wrong during prediction"}