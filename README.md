# RetailMind AI

RetailMind AI is a retail analytics project that I built to help businesses make better decisions using data and AI.

The platform can:

- Forecast future sales
- Detect unusual sales patterns
- Answer questions from business documents using RAG
- Route user queries to specialized AI agents

## Why I Built This

Retail companies generate a lot of sales data, but turning that data into useful insights can be difficult. I wanted to create a single platform that could not only analyze historical data but also predict future trends and provide intelligent assistance through AI.

## Technologies Used

- FastAPI
- MongoDB Atlas
- Scikit-Learn
- Azure OpenAI
- FAISS
- Docker
- Azure App Service

## Main Features

### Sales Forecasting
Uses a Random Forest model to predict weekly sales based on factors such as store information, holidays, temperature, fuel price, CPI, and unemployment.

### Anomaly Detection
Uses Isolation Forest to identify unusual sales records that may indicate business issues or unexpected trends.

### RAG-Based Document Search
Allows users to ask questions about retail documents and receive answers generated using Azure OpenAI and FAISS.

### Multi-Agent System
The application includes:
- ML Expert Agent
- Data Analyst Agent
- Document Assistant Agent

Each agent is responsible for handling a different type of user query.

## API Endpoints

- POST /ingest-data
- POST /forecast
- POST /detect-anomaly
- POST /search-docs
- POST /agent_chat

## Deployment

The application is containerized using Docker and deployed on Azure App Service.

## Future Improvements

Some enhancements I would like to add in the future:

- Authentication and role-based access
- Real-time analytics
- CI/CD automation
- Advanced forecasting models
