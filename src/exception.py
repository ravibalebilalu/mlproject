import sys

def error_message_details(eror,error_detail):
    _,_,exc_tb = error_detail.exc_info
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(errror)
    )
    return error_message

class CustomException(Exception):
    def  __init__(self,error_message,error_detail):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail = error_detail)

