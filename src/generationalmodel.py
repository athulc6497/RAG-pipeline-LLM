### Simple RAG Pipeline with Groq LLM

from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

from src.vector_store import FaissVectorStore




class ChatGroqModel:

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model="openai/gpt-oss-20b",
        temperature=0.1,
        max_tokens=1024
    )

    @staticmethod
    def rag_simple(query,retriever):

       
        context = "\n\n".join(  doc["metadata"]["text"] for doc in retriever)

        prompt = f"""
        Context:
        {context}

        Question:
        {query}

        Answer:
        """

        response = ChatGroqModel.llm.invoke(prompt)

        return response.content



  

    