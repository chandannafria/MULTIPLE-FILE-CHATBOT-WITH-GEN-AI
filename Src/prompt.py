import sys
from Src.logger import logging
from Src.exception import CustomException
from langchain_core.prompts import ChatPromptTemplate

class PromptTemplate:

    @staticmethod
    def get_prompt():

        return ChatPromptTemplate.from_template(
"""
You are an AI Assistant.

Use ONLY the given context.

If the answer is not present in the context,

reply:

I don't know.

Context:
{context}

Question:
{question}

Answer:
"""
        )
    