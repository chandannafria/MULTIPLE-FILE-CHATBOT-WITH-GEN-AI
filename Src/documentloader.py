import sys , os
from typing import Any, cast
from Src.logger import logging
from Src.exception import CustomException
from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
    CSVLoader,
    JSONLoader,
    PyPDFLoader,
    UnstructuredMarkdownLoader,
    UnstructuredHTMLLoader,
    MergedDataLoader,
    Docx2txtLoader
)




class DocumentLoader:

    def __init__(self, folder_path):
        logging.info("file created...")
        self.folder_path = folder_path

    def get_fileload(self):

        try:
            
            extension = os.path.splitext(self.folder_path)[1].lower()
            
            file_types = {
                ".pdf": PyPDFLoader,
                ".txt": TextLoader,
                ".csv": CSVLoader,
                ".json": JSONLoader,
                ".md": UnstructuredMarkdownLoader,
                ".html": UnstructuredHTMLLoader,
                ".docx" : Docx2txtLoader
            }
            logging.info("file uploading in progress...")
            loader_class =file_types.get(extension)
            
            if loader_class is None:
                raise ValueError(
                    f"supported file type: {extension}"
                )
            

            loaders = loader_class(self.folder_path)
            documents = loaders.load()

            logging.info(f"Loaded {len(documents)} documents")
            logging.info("file upload successfully...")

            return documents

        except Exception as e:

            raise CustomException(e, sys)