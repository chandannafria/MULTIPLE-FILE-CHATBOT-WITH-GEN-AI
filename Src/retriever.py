import sys
from Src.logger import logging
from Src.exception import CustomException
from langchain_community.retrievers import RemoteLangChainRetriever


class Retriever():
    def __init__(self , vector_db):
        self.vector_db = vector_db
        
        
    def get_retriever(self):
        try:
            logging.info("Creating Retriever...")
            retriever = self.vector_db.as_retriever(
                search_type="similarity",
                search_kwargs ={
                    "k" : 2
                }
            )
            logging.info("Retrieve created")
            
            return retriever
        
        
        
        
        except Exception as e:
            raise CustomException (e, sys)        