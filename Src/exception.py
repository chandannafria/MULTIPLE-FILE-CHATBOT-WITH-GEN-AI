import sys
import os
import warnings
warnings.filterwarnings("ignore")


def error_message_detail(error, error_message):
    _, _, exc_tb = error_message.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    error_detail = (f"Error Occured in file [{file_name}]"
                    f"at line number {line_number}"
                    f"with message {str(error)}")
    return error_detail
    
class CustomException(Exception):
    def __init__(self, error, error_message):
        super().__init__(error)
        self.error_detail = error_message_detail(error, error_message)
        
        
    def __str__(self) -> str:
        return self.error_detail
        
        