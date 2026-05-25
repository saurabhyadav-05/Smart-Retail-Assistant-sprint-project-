from app.database import sales_data
from langchain_huggingface import (ChatHuggingFace,HuggingFaceEndpoint)
from langchain_core.prompts import (PromptTemplate)

from langchain_core.output_parsers import (StrOutputParser)

from dotenv import load_dotenv
import pandas as pd


load_dotenv()

class DataAnalyst_Agent:

    def __init__(self):
        self.role = "Retail Data Analyst"
        self.llm = HuggingFaceEndpoint(
            repo_id="deepseek-ai/DeepSeek-V4-Pro",
            task="text-generation"
        )

        self.model = ChatHuggingFace(
            llm=self.llm
        )

        self.prompt = PromptTemplate(

            template="""You are a Retail Data Analyst Agent.
            Analyze the retail analytics below
            and answer the user question.
            Analytics Data:{analytics_data} Question:{question}""",
            input_variables=["analytics_data","question"])

        self.output_parser = StrOutputParser()

        self.chain = (self.prompt|self.model|self.output_parser)


    def fetch_analytics_data(self):

        data = list(
            sales_data.find()
        )

        df = pd.DataFrame(data)

        analytics_summary = f"""Average Weekly Sales:{df['Weekly_Sales'].mean()}
        Maximum Weekly Sales:{df['Weekly_Sales'].max()}
        Minimum Weekly Sales:{df['Weekly_Sales'].min()}"""

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