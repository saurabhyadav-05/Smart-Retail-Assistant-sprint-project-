from fastapi import APIRouter
from pydantic import BaseModel
from app.logger import logger

from agents.document_agent import (Document_Agent)
from agents.data_analyst_agent import (DataAnalyst_Agent)
from agents.ml_expert_agent import (MLExpert_Agent)


router = APIRouter()

document_agent = (Document_Agent())

data_analyst_agent = (DataAnalyst_Agent())

ml_expert_agent = (MLExpert_Agent())


class AgentRequest(BaseModel):
    question: str
    input_data: dict = None


@router.post("/agent_chat")
def agent_chat(data: AgentRequest):
        
    try:    
        logger.info("Agent request received")
        question = data.question.lower()

        if ("predict" in question or "forecast" in question):

            if not data.input_data:
                return {"error":"input_data required for prediction"}

            response = (ml_expert_agent.generate_response(data.input_data))

            selected_agent = ("ML Expert Agent")

        elif ("anomaly" in question  or "analytics" in question or "sales trend" in question):

            response = (data_analyst_agent.generate_response(data.question))

            selected_agent = ("Data Analyst Agent")

        else:
            response = (document_agent.generate_response(data.question))
            selected_agent = ("Document Assistant Agent")

        logger.info(f"Agent Response:{response}")    
        return {"selected_agent": selected_agent,"response": response}
    
    except Exception as e:
        logger.error(f"Agents API Error: {str(e)}")
        return {"error":"Something went wrong during response generation"}