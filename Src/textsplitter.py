import sys , os
from Src.logger import logging
from Src.exception import CustomException
from langchain_text_splitters import RecursiveCharacterTextSplitter , MarkdownTextSplitter , MarkdownHeaderTextSplitter
from Src.config import CHUNK_SIZE , CHUNK_OVERLAP
from Src.documentloader import DocumentLoader


class TextSplitter:
    try:
        def  __init__(self ,
                      
                      chunk_size=  CHUNK_SIZE, 
                      chunk_overlap=CHUNK_OVERLAP) :
            
          
            self.chunk_size = chunk_size
            self.chunk_overlap= chunk_overlap
            
        def split_document(self, document):
            logging.info("split document creat...")
            
            file_type =document[0].metadata.get("file_type")
            logging.info(f"file type {file_type}")
            
            # Markdown.....
            if file_type == ".md":
                headers = [
                     ("#", "Header 1"),

                    ("##", "Header 2"),

                    ("###", "Header 3")
                ]
                splitter = MarkdownHeaderTextSplitter(
                    headers_to_split_on=headers
                )
                Chunks =splitter.split_text(
                    document[0].page_content
                )
                logging.info("markdown splitter successfully")
            # Default Splitter
            
            else:
                splitter = RecursiveCharacterTextSplitter(
                    chunk_size= self.chunk_size,
                    chunk_overlap = self.chunk_overlap,
                    separators=[
                        "\n\n",
                        "\n",
                        ". ",
                        " ",
                        ""
                    ]
                )
                
                chunks = splitter.split_documents(document)
                logging.info("splitter successfully....")
                # meta data
                
                for index , chunk  in enumerate(chunks):
                    chunk.metadata["chunk_id"] =index 
                 
                    
                logging.info(f"Total chunk {len(chunks)}")
                
                
                return chunks
            
                       
            
    except Exception as e:
        logging.error(str(e))
        raise CustomException (e ,sys)