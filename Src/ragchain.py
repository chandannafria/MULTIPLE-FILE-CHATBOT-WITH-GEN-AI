import sys
from Src.exception import CustomException
from Src.logger import logging
from Src.prompt import PromptTemplate
from Src.model import LLM
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


class RagChain:

    def __init__(self, retriever):
        try :

            self.retriever = retriever

            self.llm = LLM().get_llm()

            self.prompt = PromptTemplate.get_prompt()
            
        except Exception as e:
            raise CustomException (e , sys)

    def create_chain(self):
        try: 
            logging.info("create chian...")
            chain = (

                {

                    "context": self.retriever,

                    "question": RunnablePassthrough()

                }

                |

                self.prompt

                |

                self.llm

                |

                StrOutputParser()

            )
            logging.info("chain created...")
            return chain
            
        
        
        except Exception as  e :
            raise CustomException (e, sys)