import sys
from Src.logger import logging
from Src.exception import CustomException
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

class EmbeddingModel():
    def __init__(self):
        
        try:
            logging.info("Initializing Embedding  Model..")
            self.embedding_model = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
            
            logging.info("Embedding Model Loaded succesfully..")
        
        
        except Exception as e:
            raise CustomException (e, sys)
    
    def Get_Embedded_Model(self):
        return self.embedding_model