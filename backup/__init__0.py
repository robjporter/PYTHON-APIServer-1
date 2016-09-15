__APICODENAME__   = "Aula"
__APIVERSION__    = "v0.5"

import time
import random, string
from flask import Flask, url_for, request, redirect, render_template, flash, make_response, session, g, abort

globalUserid = None

@app.route( "/index" )
def index():
    return request.headers.get( 'User-Agent' )

@app.route( "/404" )
def missingFile():
    abort( 404 )
    return "MISSING FILE"

@manager.command
def hello():
    print( "hello" )

@app.route( "/getusernameroute" )
def getUsernameRoute():
    return url_for( "helloUser", username="roporter" )

@app.route( "/login", methods = [ 'GET', 'POST' ])
def login():
    error = None
    app.logger.warning( "No token found: Display login screen" )
    if request.method == "POST":
        if valid_login(
            request.form.get( "username" ),
            bcrypt( request.form.get( "password" ), user.password )
        ):
            flash( "Successfully logged in" )
            session[ "username" ] = request.form.get( "username" )
            return redirect( url_for( "welcome" ))
        else:
            error = "Incorrect username and password"
            app.logger.warning( "Incorrect username and password! (%s)" % request.form.get( "username" ))
    return render_template( 'login.html', error=error )

@app.route( "/logout" )
def logout():
    global globalUserid
    #oldAuth = app.config[ "redis_store" ].get( "auths", globalUserid ).decode( encoding = 'UTF-8' )
    oldAuth = session[ "auth" ]
    session.pop( "auth", None )
    newAuth = randomStringGenerator( 32 )
    app.config[ "redis_store" ].hset( "auths", newAuth, str( globalUserid ));
    app.config[ "redis_store" ].hdel( "auths", oldAuth );
    app.config[ "redis_store" ].hdel( "loggedin", globalUserid );
    app.config[ "redis_store" ].hset( "user:" + str( globalUserid ), "auth", newAuth );
    return redirect( url_for( "login" ))

@app.route( "/dummy" )
def dummyData():
    username = "roporter"
    password = "cr0wellMEWS"
    authSecret = randomStringGenerator( 32 )
    apiKey1 = randomStringGenerator( 64 )
    userid = app.config[ "redis_store" ].incr( "next_user_id" );
    app.config[ "redis_store" ].hset( "users", username, userid )
    data = { "username" : username, "password" : password, "email" : "roporter@cisco.com", "auth" : authSecret, "api" : apiKey1, "flags" : "a", "rTime" : float( time.time())}
    app.config[ "redis_store" ].hmset( "user:" + str( userid ), data );
    app.config[ "redis_store" ].hset( "auths", authSecret, str( userid ));
    app.config[ "redis_store" ].hset( "apis", apiKey1, str( userid ));
    app.config[ "redis_store" ].zadd( "users_by_time", username, float( time.time()) );
    return "New user saved to DB"

@app.route( "/" )
def welcome():
    global globalUsername
    if 'auth' in session:
        app.logger.debug( "Auth is present in the session: Proceeding as user logged in" )
        authCookie = session[ "auth" ]
        userid = app.config[ "redis_store" ].hget( "auths", authCookie ).decode( encoding = 'UTF-8' )
        if userid != None:
            if( app.config[ "redis_store" ].hget( "user:" + str( userid ), "auth" ).decode( encoding = 'UTF-8' ) != authCookie ):
                app.logger.debug( "Session token was not equal to user token: Loading login screen" )
                return redirect( url_for( "login" ))
            else:
                loadUserInfo( userid )
                app.logger.debug( "Login was successful: Loading welcome screen" )
                return render_template( "welcome.html", username = str( globalUsername ))
        else:
            app.logger.debug( "Userid query resulted in None: Loading login screen" )
            return redirect( url_for( "login" ))
    else:
        app.logger.debug( "Auth was not in session state: Loading login screen" )
        return redirect( url_for( "login" ))

def loadUserInfo( userid ):
    global globalUserid, globalUsername
    globalUserid = userid
    globalUsername = app.config[ "redis_store" ].hget( "user:" + str( userid ), "username" ).decode( encoding = 'UTF-8' )
    print( "USERID: " + userid )
    print( "USERNAME: " + globalUsername )

def randomStringGenerator( length ):
    return ''.join( random.SystemRandom().choice( string.ascii_uppercase + string.digits ) for _ in range( length ))

def valid_login( username, password ):
    userid = app.config[ "redis_store" ].hget( "users", username )
    app.logger.debug( "UserID returned from DB query: " + str( userid ))

    if( userid == None ):
        app.logger.debug( "UserID returned from DB query was None" )
        return False
    else:
        if( not isinstance( userid, int )):
            userid = userid.decode( encoding = 'UTF-8' )

    pwd = app.config[ "redis_store" ].hget( "user:" + str( userid ).strip(), "password" )
    if( pwd == None ):
        app.logger.debug( "Password returned from DB Query was None" )
        return False
    else:
        if( app.config[ "redis_store" ].hget( "user:" + str( userid ), "password" ).decode( encoding = 'UTF-8' ) != password ):
            app.logger.debug( "Password entered does not match users password" )
            return False
        else:
            app.logger.debug( "User has logged in successfully!" )
            app.config[ "redis_store" ].hset( "loggedin", str( userid ), float( time.time()));
            session[ "auth" ] = app.config[ "redis_store" ].hget( "user:" + str( userid ), "auth" ).decode( encoding = 'UTF-8' )
            return True

@app.route( "/user/<username>" )
def helloUser( username ):
    return "Hello %s, what a wonderful day!" % ( username )

@app.route( "/post/<int:post_id>" )
def postUser( post_id ):
    return "Post: %d" % post_id

@app.before_first_request
def before_first_request():
    print( "BEFORE_FIRST_REQUEST" )

@app.before_request
def before_request():
    print( "BEFORE_REQUEST" )

#@app.after_request
#def after_request( response ):
#    print( "AFTER_REQUEST" )

@app.teardown_request
def teardown_request( exc ):
    print( "TEARDOWN_REQUEST" )
