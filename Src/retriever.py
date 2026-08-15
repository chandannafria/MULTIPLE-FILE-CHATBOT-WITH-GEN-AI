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
                search_type="mmr",
                search_kwargs ={
                    "k" : 2,
                    "fetch_k": 15,
                    "lambda_mult": 0.5
                }
            )
            logging.info("Retrieve created")
            
            return retriever
        
        
        
        
        except Exception as e:
            raise CustomException (e, sys)
        
    
    def retrieve_documents(self, query):
        try:
            logging.info(f"retrieving documents for query : {query}")
            retriever = self.get_retriever()
            documents = retriever.invoke(query)
            
            logging.info(f"{len(documents)} documents retrieved")
            
            return documents
        
        
        except Exception as e:
            raise CustomException(e, sys)