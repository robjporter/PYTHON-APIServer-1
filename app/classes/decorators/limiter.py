import functools
import time
from flask import request, current_app, g, Response
from app.classes.errorHandler import ApiErrorBaseClass

def limit( requests = 100, window = 20, by = "ip", group = None ):
    if not callable(by):
        by = { 'ip': lambda: request.access_route[ 0 ] }[by]

    def decorator(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            group = None
            group = group or request.endpoint
            #group = request.endpoint
            key = ":".join(["rl", group, by()])

            if( 'RATE_LIMIT_WINDOW' in current_app.config ):
                window = current_app.config[ 'RATE_LIMIT_WINDOW' ]

            try:
                remaining = requests - int( current_app.config[ 'DB' ].get(key))
            except (ValueError, TypeError):
                remaining = requests
                current_app.config[ 'DB' ].set(key, 0)

            ttl = current_app.config[ 'DB' ].ttl(key)
            if not ttl:
                current_app.config[ 'DB' ].expire(key, window)
                ttl = window

            g.view_limits = (requests,remaining-1,time.time()+ttl)

            if remaining > 0:
                current_app.config[ 'DB' ].incr(key, 1)
                return f(*args, **kwargs)
            else:
                return errorHandler().respond( request.accept_mimetypes, 429, "Too many requests", "You are attempting to send too many requests within a specified period.  Please try to slow the requests you are making.", "Please wait a short time before submitting further requests." )
        return wrapped
    return decorator
