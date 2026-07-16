import warnings
warnings.filterwarnings("ignore")

def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    error_message = (
        f"Error occured in file [{file_name}]"
        f"at line number [{line_number}]"
        f"with message[{str(error)}]"
    )
    
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_detail):
        super().__init__(error)
        self.error_message  =error_message_detail(error, error_detail)
        
    def __str__(self) -> str:
        return self.error_message
        
        