from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_forecast_api():

    response = client.post("/forecast",

        json={

            "Store": 1,
            "Holiday_Flag": 1,
            "Temperature": 42.31,
            "Fuel_Price": 2.57,
            "CPI": 211.09,
            "Unemployment": 8.10,
            "Year": 2010,
            "Month": 2,
            "Day": 5,
            "Week": 5,
            "DayOfWeek": 4
        }
    )

    assert response.status_code == 200

    assert "predicted_weekly_sales" in response.json()



def test_rag_api():

    response = client.post(

        "/search_docs",

        json={

            "question":
            "What affects retail sales?"
        }
    )

    assert response.status_code == 200


def test_agent_api():

    response = client.post(

        "/agent_chat",

        json={

            "question":
            "What affects retail sales?"
        }
    )

    assert response.status_code == 200

    assert "selected_agent" in response.json()