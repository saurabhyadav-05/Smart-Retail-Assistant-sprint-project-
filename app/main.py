from fastapi import FastAPI
from app.routes.ingest import router as ingest_router
from app.routes.forecast import router as forecast
from app.routes.anomaly import router as detect_anomaly
from app.routes.rag import router as search_docs
from app.routes.agents import router as agent_chat
app = FastAPI()

app.include_router(ingest_router)
app.include_router(forecast)
app.include_router(detect_anomaly)
app.include_router(search_docs)
app.include_router(agent_chat)