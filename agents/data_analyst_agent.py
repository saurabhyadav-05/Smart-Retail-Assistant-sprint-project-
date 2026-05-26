from app.database import sales_data

from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

import pandas as pd
import os


load_dotenv()


class DataAnalyst_Agent:

    def __init__(self):

        self.role = "Retail Data Analyst"

        self.model = ChatOpenAI(

            api_key=os.getenv(
                "AZURE_OPENAI_API_KEY"
            ),

            base_url=os.getenv(
                "AZURE_OPENAI_ENDPOINT"
            ),

            model=os.getenv(
                "AZURE_OPENAI_DEPLOYMENT"
            )
        )

        self.prompt = PromptTemplate(

            template="""You are a Retail Data Analyst Agent.
            Analyze the retail analytics below
            and answer the user question.

            Analytics Data:
            {analytics_data}

            Question:
            {question}""",

            input_variables=[
                "analytics_data",
                "question"
            ]
        )

        self.output_parser = StrOutputParser()

        self.chain = (
            self.prompt
            | self.model
            | self.output_parser
        )


    def fetch_analytics_data(self):

        data = list(
            sales_data.find()
        )

        df = pd.DataFrame(data)

        analytics_summary = f"""
        Average Weekly Sales:
        {df['Weekly_Sales'].mean()}

        Maximum Weekly Sales:
        {df['Weekly_Sales'].max()}

        Minimum Weekly Sales:
        {df['Weekly_Sales'].min()}
        """

        return analytics_summary


    def generate_response(self, question):

        analytics_data = (
            self.fetch_analytics_data()
        )

        response = self.chain.invoke({

            "analytics_data": analytics_data,

            "question": question
        })

        return response