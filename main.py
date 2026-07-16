import sys
from Src.exception import CustomException
from Src.logger import logging
from Src.documentloader import DocumentLoader
from Src.textsplitter import TextSplitter


def main ():
    try :
        loader = DocumentLoader("Data/california_housing_test.csv")
            
        docs = loader.get_fileload()
            
        print(type(docs))
            
        
        
        
    
    except Exception as  e :
        logging.error(e)
        raise CustomException (e ,sys)
    
    
if __name__ == "__main__":
    main()