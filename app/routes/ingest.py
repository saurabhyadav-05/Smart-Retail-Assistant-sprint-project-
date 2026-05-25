from fastapi import APIRouter
from pydantic import BaseModel
from app.database import sales_data
from app.logger import logger

router = APIRouter()

class SalesData(BaseModel):

    Store: int
    Date: str
    Weekly_Sales: float
    Holiday_Flag: int
    Temperature: float
    Fuel_Price: float
    CPI: float
    Unemployment: float


@router.post("/ingest-data")
def ingest_data(data: SalesData):
    try:    
        logger.info("data ingestion request received")
        sales_data_card = {
            "Store": data.Store,
            "Date": data.Date,
            "Weekly_Sales": data.Weekly_Sales,
            "Holiday_Flag": data.Holiday_Flag,
            "Temperature": data.Temperature,
            "Fuel_Price": data.Fuel_Price,
            "CPI": data.CPI,
            "Unemployment": data.Unemployment
        }

        sales_data.insert_one(sales_data_card)
        logger.info("data stored successfully")

        return {
            "message": "Sales data stored successfully"
        }
    
    except Exception as e:
        logger.error(f"Ingest API Error: {str(e)}")
        return {"error":"Something went wrong during storing data"}