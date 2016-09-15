__version_info__ = ('0', '1', '0')
__version__ = '.'.join(__version_info__)
__author__ = 'Rob Porter'
__license__ = 'MSD'
__copyright__ = '(c) 2014 by Rob Porter'
__APICODENAME__   = "Aula"
__APIVERSION__    = "v0.5"

import time, random, string, os, logging, sys
from logging.handlers import RotatingFileHandler
from flask import Flask, url_for, request, redirect, render_template, flash, make_response, session, g, abort
from app.classes.decorators import limiter
from app.classes.bashcolors import colors
from app.classes.errorHandler import ApiErrorBaseClass, ResourceDoesNotExist, ResourceDoesNotExist2
from app.classes.wrapper_momentjs import momentjs
from app.classes.cache import cache
from datetime import timedelta

from flask_featureflags import FeatureFlag
from flask.ext.redis import FlaskRedis
from flask.ext.bower import Bower
from flask_registry import Registry, ListRegistry
from flask_registry import Registry, ModuleDiscoveryRegistry
from flask_registry import ImportPathRegistry

######################################################################################
# Main app creation
######################################################################################
def create_app( configName, env = "prod" ):
    app = Flask( __name__ )
    #app.config.from_object( config[ configName ])
    app.config.from_object( configName )
    app.config[ 'LOADED_ROUTES' ] = 0
    app.config[ 'ENV' ] = env

# Create error log handler, logging format and set logging level to debug
    formatter = logging.Formatter( "[%(asctime)s] {%(pathname)s->%(funcName)s:%(lineno)d} %(levelname)s - %(message)s" )
    handler = RotatingFileHandler( app.config[ 'APP_LOG_NAME' ], maxBytes = 10000, backupCount = 5 )
    handler.setLevel( logging.INFO )
    handler.setFormatter( formatter )

# Create handler for web server to captcha the routes called and CLI output
    logger = logging.getLogger( 'werkzeug' )
    handler2 = logging.FileHandler( app.config[ 'ACCESS_LOG_NAME' ] )

# Add handlers
    logger.addHandler( handler2 )
    app.logger.addHandler( handler )

# Tweak to remove template cache limits and add loopcontrol extension
    app.jinja_env.cache = {}
    app.jinja_env.add_extension( 'jinja2.ext.loopcontrols' )
    app.jinja_env.globals[ 'momentjs' ] = momentjs

# Create Bower instance for easy bower integration
    Bower(app)

# Initialise the regsitry object
    Registry( app = app )
    if not hasattr(app, 'extensions'):
        app.extensions = {}
    app.extensions[ 'registry' ][ app.config[ 'EXTENSION_NAMESPACE' ]] = ListRegistry()

# Cache
    cache.init_app( app )

# Feature Flags
    feature_flags = FeatureFlag( app )

# Add Redis instance to App config array
    app.config[ "DB" ] = FlaskRedis( app )

# Create session expiration
    app.permanent_session_lifetime = timedelta( seconds = app.config[ 'SESSION_LIFETIME' ] )

# Get the path to the our modules directory
    path = os.path.join( os.path.dirname(os.path.realpath(__file__)), "modules" )
# Get all folders in the directory and check their format comlies to our expectations
    modules = load_modules( app, path )
# Load the known modules we need
    load_standard_modules( app, path, modules )
# Load the 3rd party modules and extensions
    load_extensions( app, path, modules )

    app.logger.debug( colors.getDebug() + "Total number of routes loaded: %s%s%s" % ( colors.RED, app.config[ 'LOADED_ROUTES' ], colors.DEFAULT ))
    return app

def load_modules( app, path ):
    tmp = []
    for f in os.listdir( path ):
        if( f not in app.config[ 'HIDDEN_FILES_FOLDERS' ]):
            if( f.startswith( "v" ) and len( f ) == 2 ):
                tmp.append( f )
            else:
                print( f )
                app.logger.error( colors.getError() + "The modules directory can only contain folders with the format v and a number, for example: v1" )
                exit()
    return tmp

def load_extensions( app, path, modules ):
    if( len( modules ) > 0 ):
        for i in range( 0, len( modules )):
            tmpPath = os.path.join( path, modules[ i ])
            for f in os.listdir( tmpPath ):
                if( f not in app.config[ 'DEFAULT_MODULES' ] and f not in app.config[ 'HIDDEN_FILES_FOLDERS' ] ):
                    if( f.strip() != app.config[ 'EXTENSION_DIR_NAME' ] ):
                        app.logger.error( colors.getError() + "The extensions directory is the only folder expected and allowed in the root api folder, except the core modules." )
                        exit()
            load_extension_folder( app, os.path.join( tmpPath, app.config[ 'EXTENSION_DIR_NAME' ] ), modules[ i ] )

def load_extension_folder( app, path, module ):
    for f in os.listdir( path ):
        if( f not in app.config[ 'HIDDEN_FILES_FOLDERS' ]):
            load_extension( app, os.path.join( path, f ), module )

def load_extension( app, path, module ):
    print( path )
    tmpFilenames = os.listdir( path )
    for file in tmpFilenames:
        if file not in app.config[ "HIDDEN_FILES_FOLDERS" ]:
            if( file == "__init__.py" ):
                parts = path[ path.find( module ) + len( module ): ].split( "/" )
                part1 = "/" + module + "/"
                part2 = app.config[ 'EXTENSION_DIR_NAME' ] + "/"
                part3 = parts[ 2 ]
                exec( "from app.modules." + module + "." + app.config[ 'EXTENSION_DIR_NAME' ] + "." + part3 + " import " + part3 + " as extension_" + part3 + "_blueprint" )
                eval( "app.register_blueprint( extension_" + part3 + "_blueprint, url_prefix = '" + part1 + app.config[ 'EXTENSION_URL_SUBSET' ] + part3 + "' )" )
                try:
                    eval( "modules." + module + "." + app.config[ 'EXTENSION_DIR_NAME' ] + "." + part3 + ".views.setup()" )
                except Exception as e:
                    # No start method defined for extension
                    pass
                count = load_extension_routes( path, part3 )
                app.logger.debug( colors.getDebug() + "Extension %s loaded, along with %s%s%s defined routes" % ( part3, colors.RED, str( count ), colors.DEFAULT ))
                app.config[ 'LOADED_ROUTES' ] += count

def load_extension_routes( path, name ):
    viewFile = path + "/views.py"
    f = open( viewFile, "r", encoding="utf-8" )
    contents = f.read().split()
    search = "@" + name + ".route("
    return contents.count( search )

def load_standard_modules( app, path, moduless ):
    count = 0
    for i in range( 0, len( moduless )):
        for j in range( 0, len( app.config[ 'DEFAULT_MODULES' ])):
            if( app.config[ 'DEFAULT_MODULES' ][ j ] in app.blueprints ):
                print( "LOADED: %s" % app.config[ 'DEFAULT_MODULES' ][ j ])
            else:
                print( "LOADING: %s" % app.config[ 'DEFAULT_MODULES' ][ j ])
            exec( "from .modules." + moduless[ i ] + "." + app.config[ 'DEFAULT_MODULES' ][ j ] + " import " + app.config[ 'DEFAULT_MODULES' ][ j ] + " as " + app.config[ 'DEFAULT_MODULES' ][ j ] + "_" + moduless[ i ] + "_blueprint" )
            if( app.config[ 'DEFAULT_MODULES' ][ j ] == "default" ):
                eval( "app.register_blueprint( " + app.config[ 'DEFAULT_MODULES' ][ j ] + "_" + moduless[ i ] + "_blueprint, url_prefix = '/" + moduless[ i ] + "/' )" )
            else:
                eval( "app.register_blueprint( " + app.config[ 'DEFAULT_MODULES' ][ j ] + "_" + moduless[ i ] + "_blueprint, url_prefix = '/" + moduless[ i ] + "/" + app.config[ 'DEFAULT_MODULES' ][ j ] + "' )" )
            try:
                eval( "modules." + moduless[ i ] + "." + app.config[ 'DEFAULT_MODULES' ][ j ] + ".views.setup()" )
            except Exception as e:
                # No start method defined for extension
                pass
            count += load_extension_routes( path + "/" + moduless[ i ] + "/" + app.config[ 'DEFAULT_MODULES' ][ j ], app.config[ 'DEFAULT_MODULES' ][ j ] )
        app.logger.debug( colors.getDebug( ) + "Module %s loaded, along with all core packages and %s%s%s core routes" % ( moduless[ i ], colors.RED, count, colors.DEFAULT ))
    app.config[ 'LOADED_ROUTES' ] += count
