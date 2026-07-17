import sys
from Src.logger import logging
from Src.exception import CustomException
from langchain_ollama import OllamaLLM


class LLM():
    
        def __init__(self):
            try :
                logging.info(" loading llm model....")
                self.model = OllamaLLM(
                    model= "llama3.2",
                    temperature=0
                )
                
                logging.info("llm model successfully")
            
    
            except Exception as e:
                raise CustomException (e, str)
    
        def get_llm (self):
            return self.model