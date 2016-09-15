import time
from htmlmin.main import minify
from flask import request, current_app, g
from app.classes.bashcolors import colors

def before_request():
    #print( "Path: %s" % request.path )
    #print( "Script root: %s" % request.script_root )
    #print( "Base URL: %s" % request.base_url )
    #print( "URL: %s" % request.url )
    #print( "URL root: %s" % request.url_root )
    remote_addr = request.remote_addr
    if remote_addr == "" or remote_addr == None:
        remote_addr = request.headers.getlist("X-Forwarded-For")[0]

    validateRemoteIP( remote_addr )

    found = False
    for i in range( 0, len( current_app.config[ 'TRACKING_IGNORE_EXT' ])):
        if( current_app.config[ 'TRACKING_IGNORE_EXT' ][ i ] in request.path ):
            found = True
    if( not found ):
        current_app.logger.debug( colors.getDebug() + "Inside Main->before_request | REMOTE ADDRESS = " + remote_addr + " | REQUEST ADDRESS = " + request.path )

    current_app.config[ 'REQUEST_CORE_URL' ] = found
    g.start = time.time()
    
def teardown_request( error = None ):
    res = getattr( g, 'resource', None )
    if res is not None:
        res.release()
        
def after_request( response ):
    if( "REQUEST_CORE_URL" in current_app.config and not current_app.config[ 'REQUEST_CORE_URL' ]):
        current_app.logger.info( colors.getInfo() + "Inside Main->returnResponse | app.after_request" )
        if( request.is_xhr ):
            print( "XHR request" )
    if( current_app.config[ 'MINIFY_PAGE' ]):
    	if response.content_type == u'text/html; charset=utf-8':
        	response.set_data( minify( response.get_data( as_text = True ), remove_comments = True ))
    return response
    
def injectHeaders( response ):
    if( "REQUEST_CORE_URL" in current_app.config and not current_app.config[ 'REQUEST_CORE_URL' ]):
        try:
            requests, remaining, reset = map( int, g.view_limits )
        except( AttributeError, ValueError ):
            pass
        else:
            response.headers[ "X-RateLimit-Remaining" ] = remaining
            response.headers[ "X-RateLimit-Limit" ] = requests
            response.headers[ "X-RateLimit-Reset" ] = reset
            current_app.logger.debug( colors.getDebug() + "Inside Main->injectHeaders | Response headers set with rate limiting" )
        try:
            diff = 0
            if current_app.config[ "DEBUG" ]:
                if( g.start ):
                    diff = str( time.time() - g.start )
            if( "REQUEST_CORE_URL" in current_app.config and not current_app.config[ 'REQUEST_CORE_URL' ]):
                current_app.logger.debug( colors.getDebug() + request.path + " - Exec Time: %s" % diff )
            response.headers[ "X-Frame-Options" ] = "SAMEORIGIN"
            response.headers[ "X-Runtime" ] = diff
            response.headers[ "X-Powered-By" ] = current_app.config[ "APP_POWERED_BY" ]
            response.headers[ "X-XSS-Protection" ] = "1; mode=block"
            response.headers[ "X-Content-Type-Options" ] = "nosniff"
            response.headers[ "cache-control" ] = current_app.config[ 'CACHE_HTTP_HEADER' ]
            response.headers[ "content-length" ] = len( response.response[ 0 ])
        except:
            # Remove app.logger to fix issue 0002
            pass
    return response

def validateRemoteIP( addr ):
    if( addr in current_app.config[ 'BLOCKED_IP' ]):
        raise RequestFromBlockedIP()