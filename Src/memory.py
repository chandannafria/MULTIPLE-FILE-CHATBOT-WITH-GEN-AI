import sys
from Src.exception import CustomException 
from Src.logger import logging
from langchain_community.chat_message_histories import ChatMessageHistory


class Memory():
    def __init__(self):
        try:
            logging.info("create history in a memory...")
            self.history = ChatMessageHistory()
    
    
    
        except Exception as e:
            raise CustomException (e, sys)
        
    def get_history (self):
        return self.history