import time
from flask import make_response
from functools import update_wrapper

def add_timing_information( f ):
    def timed_function( *args, **kwargs ):
        now = time.time()
        rv = make_response( f( *args, **kwargs ))
        rv.headers[ "X-Runtime2" ] = str( time.time() - now )
        return rv
    return update_wrapper( timed_function, f )
