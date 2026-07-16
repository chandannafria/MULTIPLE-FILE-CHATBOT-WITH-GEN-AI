import sys , os
from Src.logger import logging
from Src.exception import CustomException
from langchain_text_splitters import RecursiveCharacterTextSplitter , MarkdownTextSplitter , MarkdownHeaderTextSplitter
from Src.config import CHUNK_SIZE , CHUNK_OVERLAP


class TextSplitter:
    try:
        def  __init__(self ,
                      file_path,
                      chunk_size=  CHUNK_SIZE, 
                      chunk_overlap=CHUNK_OVERLAP) :
            
            self.file_path = file_path
            self.chunk_size = chunk_size
            self.chunk_overlap= chunk_overlap
            
        def split_document(self, document):
            logging.info("split document creat...")
            
            extension = os.path.splitext(self.file_path)[1].lower()
            logging.info(f"file type {extension}")
            
            # Markdown.....
            if extension == ".md":
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
                    chunk.metadata["file_type"] = extension
                    
                logging.info(f"Total chunk {len(chunks)}")
                
                
                return chunks
            
                       
            
    except Exception as e:
        logging.error(str(e))
        raise CustomException (e ,sys)