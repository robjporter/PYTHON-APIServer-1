from flask import render_template, session, request, redirect, url_for, current_app, jsonify, abort
from . import auth
import datetime
from app.classes import stringFunctions
from app.classes.helpers import request_wants_json, request_wants_xml, request_wants_html
from app.classes.errorHandler import ApiErrorBaseClass, ResourceDoesNotExist, ResourceDoesNotExist2, CustomErrorMessage
from app.classes.decorators.limiter import limit
from app.classes.decorators.timing import add_timing_information
from app.classes.cache import cache
from flask_swagger import swagger

version = "0.0.0"
info = { "developer" : "roporter", "created" : "28/11/2015", "updated" : "4/12/2015", "description" : "Overview" }


def setup( ) :
	pass


@auth.route( "/token", methods = [ "GET" ] )
def auth_token_get( ) :
	#print( "JSON: %s" % request_wants_json( ) )
	#print( "XML: %s " % request_wants_xml( ) )
	#print( "HTML: %s " % request_wants_html( ) )
	if (request.method == "GET") :
		print( "GET" )
		# "<access>"
		# "<token id='' expires='' />"
		# "<user id='' name=''>"
		# "<roles>"
		# "<role id='' name='' description='' />"
		# "</roles>"
		# "</user>"
		# "</access>"
		return jsonify( ACTION = "GET" )
	elif( request.method == "HEAD" ):
		print( "HEAD" )
		return ""
	else:
		raise UnsupportedRequestMethod()

@auth.route( "/token", methods = [ "HEAD" ] )
def auth_token_head( ) :
	print( "HEAD" )
	return jsonify( ACTION = "HEAD" )


@auth.route( "/token", methods = [ "POST" ] )
def auth_token_post( ) :
	print( "POST" )
	return jsonify( ACTION = "POST" )


@auth.route( "/token", methods = [ 'DELETE' ] )
def auth_token_delete( ) :
	print( "DELETE" )
	return jsonify( ACTION = "DELETE" )
