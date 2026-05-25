import joblib
import pandas as pd

from langchain_huggingface import (ChatHuggingFace,HuggingFaceEndpoint)

from langchain_core.prompts import (PromptTemplate)

from langchain_core.output_parsers import (StrOutputParser)

from dotenv import load_dotenv


load_dotenv()


class MLExpert_Agent:

    def __init__(self):

        self.role = "Retail ML Expert"

        self.model = joblib.load("app/models/forecast_model.pkl")

        self.llm = HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V4-Pro",task="text-generation")

        self.chat_model = ChatHuggingFace(llm=self.llm)

        self.prompt = PromptTemplate( template="""You are a Retail ML Expert Agent.
        Analyze the machine learning prediction below
        and explain the business insights.
        Prediction:{prediction} Input Features:{features}
        Provide a professional explanation.""",
        input_variables=["prediction","features"])

        self.output_parser = StrOutputParser()

        self.chain = (self.prompt|self.chat_model|self.output_parser)


    def predict_sales(self, input_data):
        df = pd.DataFrame([input_data])
        prediction = self.model.predict(df)

        return round(prediction[0], 2)


    def generate_response(self, input_data):
        prediction = self.predict_sales(
            input_data
        )

        response = self.chain.invoke({
            "prediction": prediction,
            "features": input_data
        })

        return response