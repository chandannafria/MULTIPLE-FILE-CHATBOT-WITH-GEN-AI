import sys
from Src.exception import CustomException
from Src.logger import logging
from Src.documentloader import DocumentLoader
from Src.textsplitter import TextSplitter
from Src.embedding import EmbeddingModel
from Src.vectorstore import vectorstore

def main ():
    try :
        loader = DocumentLoader("Data/dl-curriculum.pdf")
            
        docs = loader.get_fileload()
            
        # print(type(docs))
        split_text  = TextSplitter()
        
        chunks = split_text.split_document(docs)
        # if not chunks:
        #     print("No chunks available")
        # else:
        #     print(chunks[1].page_content)
        embedding = EmbeddingModel()
        embedding_model = embedding.Get_Embedded_Model()
        
        # query = "What is deep learning?"
        # query_result = embedding_model.embed_query(query)
        # print("Query embedding:", query_result)

        # # Corrected: embed_documents expects a list of strings
        # if chunks:
        #     doc_result = embedding_model.embed_documents([chunk.page_content for chunk in chunks])
        # else:
        #     doc_result = []
        # print("Document embeddings (first 5):")
        # for i, res in enumerate(doc_result[:5]):
        #     print(f"  Chunk {i}: {res[:10]}...") 
        vector_db =vectorstore()
        db =vector_db.create_vector_store(chunks)
        
        print(db)
            
        
        
            
        
        
        
    
    except Exception as  e :
        logging.error(e)
        raise CustomException (e ,sys)
    
    
if __name__ == "__main__":
    main()