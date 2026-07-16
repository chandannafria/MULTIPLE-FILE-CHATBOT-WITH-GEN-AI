import sys
from typing import Any, cast
from Src.logger import logging
from Src.exception import CustomException
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

class DocumentLoader():
    try:
        def __init__(self, file_path:str):
            logging.info("create a file path")
            self.file_path = file_path
            
        def get_fileload(self):
            logging.info("upload file....")
            loader = DirectoryLoader(self.file_path,
                                     glob="*.pdf",
                                     loader_cls=cast(Any, PyPDFLoader)
                                     )
            
            
            Document = loader.load()
            logging.info("Successfully loaded")
            print(Document)
            
    except Exception as e:
        logging.error(e)
        raise CustomException(e, sys)
    