import sys
from Src.logger import logging
from Src.exception import CustomException
from langchain_chroma import Chroma
from Src.embedding import EmbeddingModel

class vectorstore():
    def __init__(self):
        try:
            logging.info("Initialize embedding moidel to vector....")
            self.embedding_model = (
                EmbeddingModel().Get_Embedded_Model()
            )
        except Exception as e :
            raise CustomException (e, sys)
            
            
    def create_vector_store(self, chunks):
        try : 
            logging.info("create vector store...")
            vector_db = Chroma.from_documents(
                documents=chunks,
                embedding= self.embedding_model,
                persist_directory="vectorstore_db"
                
            )        
            logging.info("vector store successfully...")
            return vector_db
            
        
        except Exception as e :
            raise CustomException (e, sys)