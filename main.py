from app import create_app
import os, datetime, bcrypt
from werkzeug.exceptions import HTTPException

from flask import render_template, g, jsonify, abort, Response, request, redirect
from flask.ext.script import Manager, Shell, Server
from flask.ext.script.commands import ShowUrls, Clean

from app.classes import stringFunctions
from app.classes.bashcolors import colors
from app.classes.decorators.logged import logged
from app.classes.debug import setupDebug
from app.classes.requests import before_request, teardown_request, after_request, injectHeaders
from app.classes.contexts import inject_time, format_price
from app.classes.filters import reverse_filter, string_trim_upper, string_trim_lower, datetimeformat
from app.classes.manager import managerInteractive, managerClearLogs, managerDumpConfig, managerResetDB, managerRoutes, managerCleanPYC, managerDummyData, _make_context
from app.classes.errorHandler import ApiErrorBaseClass, ResourceDoesNotExist, ResourceDoesNotExist2, RequestFromBlockedIP, RequestForUnsupportedMediaFormat

######################################################################################
# Create App instance
######################################################################################
env = os.environ.get( 'APPNAME_ENV', 'dev' )
app = create_app( 'app.config.%sConfig' % env.capitalize(), env )

######################################################################################
# Manager commands for shell access
######################################################################################
manager = Manager( app )
manager.add_command( "runserver", Server() )
manager.add_command( "runserverpublic", Server( host = "0.0.0.0", port = 9000 ))
manager.add_command( "runservernoreload", Server( use_reloader = False ))
manager.add_command( "shell", Shell( make_context = _make_context ))
manager.add_command( "urls", ShowUrls())
manager.add_command( "clean", Clean())
manager.add_command( "interactive", managerInteractive() )
manager.add_command( "clearlogs", managerClearLogs() )
manager.add_command( "dumpconfig", managerDumpConfig() )
manager.add_command( "resetDB", managerResetDB() )
manager.add_command( "routes", managerRoutes() )
manager.add_command( "cleanpyc", managerCleanPYC() )
manager.add_command( "dummydata", managerDummyData() )

######################################################################################
# Global handlers
######################################################################################
app.before_request( before_request )
app.teardown_request( teardown_request )
app.after_request( after_request )
app.after_request( injectHeaders )

@logged
@app.errorhandler( Exception )
def handle_error( error ):
    app.logger.info( colors.getInfo() + "Inside Main->handle_error | app.errorhandler( Exception )" )
    response = ""
    try:
        if( isinstance( error, HTTPException )):
            app.logger.debug( colors.getDebug() + "Inside Main->handle_error | ERRORHANDLER->ISINSTANCE->HTTPEXCEPTION" )
            if error.code < 400:
                return Response.force_type(e, request.environ)
            else:
                error = "CREATE ME HERE"
                error = ResourceDoesNotExist()

        if( issubclass( error.__class__, ApiErrorBaseClass )):
            if "text/html" in request.accept_mimetypes:
                app.logger.debug( colors.getDebug() + "Inside Main->handle_error | ERRORHANDLER->RESPOND->HTML" )
                response = error.toHTML
            elif "application/json" in request.accept_mimetypes:
                app.logger.debug( colors.getDebug() + "Inside Main->handle_error | ERRORHANDLER->RESPOND->JSON" )
                response = error.toJSON
            elif "application/xml" in request.accept_mimetypes:
                app.logger.debug( colors.getDebug() + "Inside Main->handle_error | ERRORHANDLER->RESPOND->XML" )
                response = error.toXML
            else:
                app.logger.warning( colors.getWarning() + "Inside Main->handle_error | ERRORHANDLER->NONHTTPEXCEPTION" )
                response = None
        else:
            app.logger.warning( colors.getWarning() + "Inside Main->handle_error | UNKNOWN" )
            import sys, traceback
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_details = {
                                 'filename': exc_traceback.tb_frame.f_code.co_filename,
                                 'lineno'  : exc_traceback.tb_lineno,
                                 'name'    : exc_traceback.tb_frame.f_code.co_name,
                                 'type'    : exc_type.__name__,
                                 #'message' : exc_value.message, # or see traceback._some_str()
                                }
            app.logger.error( colors.getError() + traceback.print_exception( exc_type, exc_value, exc_traceback, limit = 2 ))
            response = "UNKNOWN"
            app.config[ 'lastError' ] = error
        #return redirect( url_for( "error.errorIndex" ))
        return response
    except:
        import sys, traceback
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback_details = {
                         'filename': exc_traceback.tb_frame.f_code.co_filename,
                         'lineno'  : exc_traceback.tb_lineno,
                         'name'    : exc_traceback.tb_frame.f_code.co_name,
                         'type'    : exc_type.__name__,
                         #'message' : exc_value.message, # or see traceback._some_str()
                        }
        if( exc_type is None ): 
        	exc_type = ""
        if( exc_value is None ): 
        	exc_value = ""
        if( exc_traceback is None ): 
        	exc_traceback = ""
        print( "EXC_TYPE: %s" % exc_type )
        print( "EXC_VALUE: %s" % exc_value )
        print( "EXC_TRACEBACK: %s" % exc_traceback )
        if( traceback != None ):
        	app.logger.warning( colors.getError() + traceback.print_exception( exc_type, exc_value, exc_traceback, limit = 2 ))
        return "MAJOR ERROR"

######################################################################################
# Template Filters
######################################################################################
app.jinja_env.filters[ 'reverse' ] = reverse_filter
app.jinja_env.filters[ 'trim_upper' ] = string_trim_upper
app.jinja_env.filters[ 'trim_lower' ] = string_trim_lower
app.jinja_env.filters[ 'formatdatetime' ] = datetimeformat

######################################################################################
# Context Processors
######################################################################################
app.jinja_env.globals.update( format_price=format_price )
app.context_processor( inject_time )

######################################################################################
# Run application instance
######################################################################################
if( __name__ == "__main__" ):
    app.logger.info( "\n\n\n\n******************" + colors.YELLOW + str( datetime.datetime.utcnow() ) + colors.DEFAULT + "*******************" )
    if( app.config[ 'DEBUG' ]):
        setupDebug( app )
    manager.run()
