#making the custom excetpion module that will be use in some time
import sys

def error_message_details(error,error_details:sys):
    # the first two parameters, we don't require , the third is required
    # the third parameter consist error_file_name,file_error_line_number,error_type
    _,_,exc_tb=error_details.exc_info()
    error_file_name=exc_tb.tb_frame.f_code.co_filename
    error_line_number=exc_tb.tb_lineno
    error_type=error

    error_message="the error occured in python script [{0}] the line number [{1}] the error type is [{2}]".format(
        error_file_name,
        error_line_number,
        error_type
    )

    return error_message


class Custom_Exception(Exception):
    def __init__(self, error_message,error_details:sys) :
        super().__init__(error_message)
        #initialize the custom_excetpion error message
        self.error_message=error_message_details(error_message,error_details=error_details) 

    #Whenever we get the error we print this error message by __str__ function 
    def __str__(self):
        return self.error_message