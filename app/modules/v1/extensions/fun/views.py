from flask import render_template, session, request, redirect, url_for, current_app, jsonify, abort
from . import fun
import datetime
from app.classes import stringFunctions
from app.classes.errorHandler import ApiErrorBaseClass, ResourceDoesNotExist, ResourceDoesNotExist2, CustomErrorMessage
from app.classes.decorators.limiter import limit
from app.classes.decorators.timing import add_timing_information
from app.classes.cache import cache

@fun.route( "/minion" )
def minion():
	return render_template( "minion.html" )

@fun.route( "/olaf" )
def olaf():
	return render_template( "olaf.html" )

@fun.route( "/spongebob" )
def spongebob():
	return render_template( "spongebob.html" )

@fun.route( "/mickey" )
def mickey():
	return render_template( "mickey.html" )

@fun.route( "/elephant" )
def elephant():
	return render_template( "elephant.html" )

@fun.route( "/mike" )
def mike():
	return render_template( "mike.html" )

@fun.route( "/stewie" )
def stewie():
	return render_template( "stewie.html" )

@fun.route( "/brian" )
def brian():
	return render_template( "brian.html" )

@fun.route( "/baymax" )
def baymax():
	return render_template( "baymax.html" )



@fun.route( "/dashboard1" )
def dashboard1():
	return render_template( "dashboard1.html" )

@fun.route( "/dashboard2" )
def dashboard2():
	return render_template( "dashboard2.html" )

@fun.route( "/dashboard3" )
def dashboard3():
	return render_template( "dashboard3.html" )

@fun.route( "/dashboard4" )
def dashboard4():
	return render_template( "dashboard4.html" )

@fun.route( "/dashboard5" )
def dashboard5():
	return render_template( "dashboard5.html" )

@fun.route( "/dashboard6" )
def dashboard6():
	return render_template( "dashboard6.html" )

@fun.route( "/dashboard7" )
def dashboard7():
	return render_template( "dashboard7.html" )

@fun.route( "/dashboard8" )
def dashboard8():
	return render_template( "dashboard8.html" )

@fun.route( "/dashboard9" )
def dashboard9():
	return render_template( "dashboard9.html" )



@fun.route( "/menus1" )
def menus1():
	return render_template( "menus1.html" )

@fun.route( "/menus2" )
def menus2():
	return render_template( "menus2.html" )

@fun.route( "/menus3" )
def menus3():
	return render_template( "menus3.html" )

@fun.route( "/menus4" )
def menus4():
	return render_template( "menus4.html" )

@fun.route( "/menus5" )
def menus5():
	return render_template( "menus5.html" )

@fun.route( "/menus6" )
def menus6():
	return render_template( "menus6.html" )



@fun.route( "/panels1" )
def panels1():
	return render_template( "panels1.html" )

@fun.route( "/panels2" )
def panels2():
	return render_template( "panels2.html" )

@fun.route( "/panels3" )
def panels3():
	return render_template( "panels3.html" )

@fun.route( "/panels4" )
def panels4():
	return render_template( "panels4.html" )

@fun.route( "/panels5" )
def panels5():
	return render_template( "panels5.html" )

@fun.route( "/panels6" )
def panels6():
	return render_template( "panels6.html" )

@fun.route( "/panels7" )
def panels7():
	return render_template( "panels7.html" )

@fun.route( "/panels8" )
def panels8():
	return render_template( "panels8.html" )

@fun.route( "/panels9" )
def panels9():
	return render_template( "panels9.html" )




@fun.route( "/notification1" )
def notification1():
	return render_template( "notification1.html" )

@fun.route( "/notification2" )
def notification2():
	return render_template( "notification2.html" )



@fun.route( "/shadows1" )
def shadows1():
	return render_template( "shadows1.html" )
	
@fun.route( "/shadows2" )
def shadows2():
	return render_template( "shadows2.html" )



@fun.route( "/shapes1" )
def shapes1():
	return render_template( "shapes1.html" )

@fun.route( "/time1" )
def time1():
	return render_template( "time1.html", timestamp = datetime.datetime.now().replace( minute = 0 ))

@fun.route( "/form1" )
def form1():
	return render_template( "form1.html" )

@fun.route( "/animate1" )
def animate1():
	return render_template( "animate1.html" )


@fun.route( "/charts1" )
def charts1():
	return render_template( "charts1.html" )

@fun.route( "/elements1" )
def elements1():
	return render_template( "elements1.html" )

@fun.route( "/table1" )
def table1():
	return render_template( "table1.html" )

@fun.route( "/fonts1" )
def fonts1():
	return render_template( "fonts1.html" )



@fun.route( "/buttons1" )
def buttons1():
	return render_template( "buttons1.html" )

@fun.route( "/buttons2" )
def buttons2():
	return render_template( "buttons2.html" )

@fun.route( "/buttons3" )
def buttons3():
	return render_template( "buttons3.html" )

@fun.route( "/buttons4" )
def buttons4():
	return render_template( "buttons4.html" )

@fun.route( "/buttons5" )
def buttons5():
	return render_template( "buttons5.html" )

@fun.route( "/buttons6" )
def buttons6():
	return render_template( "buttons6.html" )

@fun.route( "/buttons7" )
def buttons7():
	return render_template( "buttons7.html" )

@fun.route( "/buttons8" )
def buttons8():
	return render_template( "buttons8.html" )



@fun.route( "/banner1" )
def banner1():
	return render_template( "banner1.html" )

@fun.route( "/banner2" )
def banner2():
	return render_template( "banner2.html" )

@fun.route( "/banner3" )
def banner3():
	return render_template( "banner3.html" )

@fun.route( "/banner4" )
def banner4():
	return render_template( "banner4.html" )

@fun.route( "/banner5" )
def banner5():
	return render_template( "banner5.html" )

@fun.route( "/banner6" )
def banner6():
	return render_template( "banner6.html" )

@fun.route( "/banner7" )
def banner7():
	return render_template( "banner7.html" )
