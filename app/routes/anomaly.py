from fastapi import APIRouter
from pydantic import BaseModel
from app.logger import logger

import pandas as pd
import joblib

router = APIRouter()

model = joblib.load("app/models/anomaly_model.pkl")

class Input(BaseModel):

    Weekly_Sales: float
    Temperature: float
    Fuel_Price: float
    CPI: float
    Unemployment: float


@router.post("/detect_anomaly")
def detect_anomaly(data:Input):

    try:    
        logger.info("anomaly detection request received")
        input_data = pd.DataFrame([{
            "Weekly_Sales": data.Weekly_Sales,
            "Temperature": data.Temperature,
            "Fuel_Price": data.Fuel_Price,
            "CPI": data.CPI,
            "Unemployment": data.Unemployment
        }])

        prediction = model.predict(input_data)

        if prediction[0] == -1:
            result = "Anomaly Detected"

        else:
            result = "Normal Transaction"

        logger.info(f"Anomaly result:{result}")    
        return {
            "prediction": result
        }
    
    except Exception as e:
        logger.error(f"anomaly API Error: {str(e)}")
        return {"error":"Something went wrong during prediction"}