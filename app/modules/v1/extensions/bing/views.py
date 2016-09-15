from flask import render_template, session, request, redirect, url_for, current_app, jsonify, abort
from . import bing
import datetime
from app.classes import stringFunctions
from app.classes.errorHandler import ApiErrorBaseClass, ResourceDoesNotExist, ResourceDoesNotExist2, CustomErrorMessage
from app.classes.decorators.limiter import limit
from app.classes.decorators.timing import add_timing_information
from app.classes.cache import cache

@bing.route( "/" )
@cache.memoize( timeout = 30 )
@add_timing_information
def index():
	return render_template( "index.html" )
