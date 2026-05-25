from fastapi import APIRouter
from pydantic import BaseModel
from app.logger import logger

from rag.rag_pipeline import rag

router = APIRouter()

class query(BaseModel):
    question: str


@router.post("/search_docs")
def search_documents(data: query):

    try:    
        logger.info("rag request received")
        response = rag(data.question)
        logger.info(f"rag response:{response}")
        return {"response": response}
    
    except Exception as e:
        logger.error(f"Rag API Error: {str(e)}")
        return {"error":"Something went wrong during searching in documents"}