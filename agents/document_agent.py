from rag.rag_pipeline import rag

class Document_Agent:
    def __init__(self):
        self.role = "Retail Document Assistant"

    def generate_response(self, question):
        agent_prompt = f"""You are a Retail Document Assistant Agent.
        Answer the user question using retail business knowledge.
        User Question:{question}"""

        response = rag(agent_prompt)

        return response
