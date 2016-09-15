from flask import render_template, session, request, redirect, url_for, current_app, jsonify, abort
from . import default
import datetime
from app.classes import stringFunctions
from app.classes.errorHandler import ApiErrorBaseClass, ResourceDoesNotExist, ResourceDoesNotExist2, CustomErrorMessage
from app.classes.decorators.limiter import limit
from app.classes.decorators.timing import add_timing_information
from app.classes.cache import cache
from flask_swagger import swagger

version = "0.0.0"
info = { "developer" : "roporter", "created" : "28/11/2015", "updated" : "4/12/2015", "description" : "Overview" }

def setup():
	pass

@default.route( "/" )
@cache.memoize( timeout = 30 )
@add_timing_information
def index():
	return render_template( "about-index.html", toreverse = "roporter", timed = str( datetime.datetime.utcnow() ) )

@default.route("/spec")
def spec():
	print( "HERE" )
	swag = swagger( current_app )
	swag[ 'info' ][ 'version' ] = "1.0"
	swag[ 'info' ][ 'title' ] = "My API"
	return jsonify( swag )

@default.route( 'version' )
def localversion():
    return jsonify( version = version )

@default.route( 'versions' )
def globalversions():
    return jsonify( versions = version )

@default.route( 'info' )
def localinfo():
    return jsonify( info = info )

@default.route( 'infos' )
def globalinfos():
	return jsonify( infos = info )

@default.route( 'whereami' )
def whereami():
	import geoip
	print( request.remote_addr  )
	match = geoip.geolite2.lookup( str( request.remote_addr ))
	resp = ""
	if( match is None ):
		print( "NOT FOUND" )
	else:
		print( str( match ))
		print( str( match.timezone ))
		print( match.country )
		print( match.continent )
		print( match.timezone )
		print( match.subdivisions )
		resp = match
	return jsonify( resp )
######################################################################################
# Temporary routes for debug and testing
######################################################################################
@default.route( "load" )
@limit( requests = 2, by = 'ip' )
def load():
    current_app.logger.debug( "/load Called" )
    return "loading"

@default.route( "test" )
def testing():
    #raise InvalidUsage('This view is gone', status_code=410)
    #about( 404, code="404", description="TEST", name="Not Found", page_title="TEST" )
    #tmp = { "code" : "404", "description" : "Test", "name" : "Not Found", "page_title" : "TEST" }
    #return generic_error_handler( tmp )
	current_app.logger.debug( "/test Called" )
	raise ResourceDoesNotExist()
	#raise Exception( "test" ) #eh.errorHandler.respondSimple( 500 ))

@default.route( "test2")
def abortme():
	current_app.logger.debug( "/test2 Called" )
	#return handle_error( errorHandler.errorHandler.respondSimple( 501 ))
	raise ResourceDoesNotExist2()

@default.route( "test3" )
def raiseme():
	current_app.logger.debug( "/test3 Called" )
	raise CustomErrorMessage( 123 )
