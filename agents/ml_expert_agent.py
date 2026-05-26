import joblib
import pandas as pd

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from app.llm import llm


class MLExpert_Agent:

    def __init__(self):

        self.role = "Retail ML Expert"

        self.model = joblib.load("app/models/forecast_model.pkl")

        self.prompt = PromptTemplate(
            template="""
            You are a Retail ML Expert Agent.

            Analyze the machine learning prediction below
            and explain the business insights.

            Prediction: {prediction}

            Input Features: {features}

            Provide a professional explanation.
            """,

            input_variables=[
                "prediction",
                "features"
            ]
        )

        self.output_parser = StrOutputParser()

        self.chain = (self.prompt|llm|self.output_parser)

    def predict_sales(self, input_data):

        df = pd.DataFrame([input_data])

        prediction = self.model.predict(df)

        return round(prediction[0], 2)

    def generate_response(self, input_data):

        prediction = self.predict_sales(input_data)

        response = self.chain.invoke({"prediction": prediction,"features": input_data})

        return response