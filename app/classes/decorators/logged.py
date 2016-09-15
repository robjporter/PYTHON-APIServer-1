import datetime
from functools import wraps

def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        #print( str( datetime.datetime.utcnow()) + " | " + func.__name__ + " was called" )
        return func(*args, **kwargs)
    return with_logging
