import sys
from Src.exception import CustomException
# from Src.logger import logging
from Src.documentloader import DocumentLoader


def main ():
    try :
        loader = DocumentLoader("dl-curriculum.pdf")
        
        docs = loader.get_fileload()
        if docs and len(docs) > 1:
            print(docs[1].page_content)
        
    
    
    
    
    except Exception as  e :
        raise CustomException (e ,str)
    
    
if __name__ == "__main__":
    main()