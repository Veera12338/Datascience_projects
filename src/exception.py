import sys
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "error occured in a python script as name [{0}] line number [{1}] error_message[{2}]".format(
        filename, exc_tb.tb_lineno, str(error))
    
    return error_message

    ##here how we look like error message inside your file with respect to the custom exception

## whenever my error raises i am going to call this particular function
    
class customException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(self, error_message)##here we are going to use the error message to inherit the error message
        self.error_message = error_message_detail(error_message, error_detail = error_detail)
        ##here we dont know the error_message so we called function from over the above and error_detail assigned to error_detail
    def __str__(self):
        return self.error_message


'''if __name__ == "__main__":

    try:
        x = 1/0
    except Exception as E:
        logging.info("zero division error")
        raise customException(E, sys)
'''
    



