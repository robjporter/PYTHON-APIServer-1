import os, sys

moduleName = ""

# Check user supplied required elements
if( len( sys.argv ) == 3 ):
    moduleVersion = sys.argv[ 1 ].lower()
    moduleName = sys.argv[ 2 ].lower()
else:
    print( "Please provide the name of the module to create" )
    exit()

# Get modules root directory
modulesDirRoot = os.path.join( os.path.sep, os.getcwd(), 'app','modules', moduleVersion, 'extensions' )
moduleDir = os.path.join( os.path.sep, modulesDirRoot, moduleName )
moduleDirStatic = os.path.join( os.path.sep, moduleDir, 'static' )
moduleDirStatiCSS = os.path.join( os.path.sep, moduleDir, 'static', 'css' )
moduleDirStaticJS = os.path.join( os.path.sep, moduleDir, 'static', 'js' )
moduleDirStaticData = os.path.join( os.path.sep, moduleDir, 'static', 'data' )
moduleDirStaticImages = os.path.join( os.path.sep, moduleDir, 'static', 'images' )
moduleDirTemplates = os.path.join( os.path.sep, moduleDir, 'templates' )


if not os.path.exists( moduleDir ):
    os.makedirs( moduleDir )
    os.makedirs( moduleDirStatic )
    os.makedirs( moduleDirStatiCSS )
    os.makedirs( moduleDirStaticJS )
    os.makedirs( moduleDirStaticData )
    os.makedirs( moduleDirStaticImages )
    os.makedirs( moduleDirTemplates )
    # Create init file
    fo = open( os.path.join( os.path.sep, moduleDir, "__init__.py" ), "w" )
    fo.write( "from flask import Blueprint\n" )
    fo.write( moduleName + " = Blueprint( '" + moduleName + "',  __name__, template_folder = 'templates', static_folder = 'static', static_url_path = '" + moduleName + "/static' )\n" )
    fo.write( "from . import views" )
    fo.close()
    # Create index template file
    fo = open( os.path.join( os.path.sep, moduleDirTemplates, "index.html" ), "w" )
    fo.write( moduleName + " - INDEX PAGE")
    fo.close()
    # Create views file
    fo = open( os.path.join( os.path.sep, moduleDir, "views.py" ), "w" )
    fo.write( "from flask import render_template, session, request, redirect, url_for, current_app, jsonify, abort\n" )
    fo.write( "from . import " + moduleName + "\n" )
    fo.write( "import datetime\n" )
    fo.write( "from app.classes import stringFunctions\n" )
    fo.write( "from app.classes.errorHandler import ApiErrorBaseClass, ResourceDoesNotExist, ResourceDoesNotExist2, CustomErrorMessage\n" )
    fo.write( "from app.classes.decorators.limiter import limit\n" )
    fo.write( "from app.classes.decorators.timing import add_timing_information\n" )
    fo.write( "from app.classes.cache import cache\n\n" )
    fo.write( "version = '0.0.0'\n" )
    fo.write( "info = { 'developer' : 'roporter', 'created' : '28/11/2015', 'updated' : '4/12/2015', 'description' : 'Overview' }\n\n" )
    fo.write( "@" + moduleName + ".route( '/' )\n" )
    fo.write( "@cache.memoize( timeout = 30 )\n" )
    fo.write( "@add_timing_information\n" )
    fo.write( "def index():\n" )
    fo.write( "\treturn render_template( 'index.html', toreverse = '" + moduleName + "', timed = str( datetime.datetime.utcnow() ) )\n\n" )
    fo.write( "@" + moduleName + ".route( '/version' )\n" )
    fo.write( "def localversion():\n" )
    fo.write( "\treturn jsonify( version = version )\n\n" )
    fo.write( "@" + moduleName + ".route( '/info' )\n" )
    fo.write( "def localinfo():\n" )
    fo.write( "\treturn jsonify( info = info )\n" )


    fo.close()
