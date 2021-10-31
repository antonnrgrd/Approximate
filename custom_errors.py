
class ErrornousShape(Exception):
    def __init__(self,msg_error = 'Error, provided vectors are of a different shape. Ensure both vectors are of the exact same shape'):
        self.msg_error = msg_error
        

