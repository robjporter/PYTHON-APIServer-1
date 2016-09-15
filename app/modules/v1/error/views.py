from flask import render_template, session, request, redirect, url_for, current_app, jsonify, abort, g
from . import error
import time
from app.classes import stringFunctions
from app.classes.errorHandler import ApiErrorBaseClass, ResourceDoesNotExist, ResourceDoesNotExist2, CustomErrorMessage
from app.classes.decorators.limiter import limit

@error.route( "/display" )
def errorIndex():
    print( "INSIDE->APP->MODULES->v1->ERROR->VIEWS->ERRORINDEX" )
    return render_template( "index.html", code = current_app.config[ 'lastError' ].status, message = current_app.config[ 'lastError' ].message, extra = current_app.config[ 'lastError' ].extras, coded = current_app.config[ 'lastError' ].toJSON  )
