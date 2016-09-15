import pprint
import subprocess
from flask import current_app, url_for
from app.classes.bashcolors import colors
from flask.ext.script import Command, prompt_choices

class managerInteractive( Command ):
    def run(self, **kwargs):
    	choices = (
        	(1, "\nmember"),
        	(2, "\nmoderator"),
        	(3, "\nadmin")
   		)
    	role = prompt_choices( "role", choices = choices, resolve = int, default = 1 )
    	print( role )

class managerClearLogs( Command ):
    def run(self, **kwargs):
    	path = os.getcwd()
    	logs = os.path.join( os.path.sep, path, "logs" )
    	for the_file in os.listdir( logs ):
        	file_path = os.path.join( logs, the_file )
        	try:
        		if os.path.isfile( file_path ):
        			os.unlink( file_path )
        			print( file_path + " - Deleted successfully" )
        	except Exception as e:
        		print( e )
    	print( "Logs directory cleared." )
    	
class managerDumpConfig( Command ):
	def run( self, **kwargs ):
		pprint.pprint( current_app.config )
		
class managerResetDB( Command ):
	def run( self, **kwargs ):
		current_app.logger.info( "Inside Main->resetDB | DB Flushed" )
		current_app.config[ "DB" ].flushdb()

class managerRoutes( Command ):
	def run( self, **kwargs ):
		current_app.logger.info( "Inside Main->routes | Routes printed" )
		import urllib
		output = []
		count = 0
		tmp = ""
		for rule in current_app.url_map.iter_rules():
			options = {}
			for arg in rule.arguments:
				options[arg] = "[{0}]".format(arg)
			methods = ','.join(rule.methods)
			url = url_for(rule.endpoint, **options)
			line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
			output.append(line)
			tmp += line + "\n"
			count += 1
		current_app.logger.debug( "%sCurrently there are %s active routes\n%s%s" % ( colors.GREEN,str( count ), colors.DEFAULT, tmp ))
		
class managerCleanPYC( Command ):
	"""Removes all *.pyc files from the project folder"""
	def run( self, **kwargs ):
		clean_command = "find . -name *.pyc -delete".split()
		subprocess.call( clean_command )

class managerDummyData( Command ):
	def run( self, **kwargs ):
		current_app.logger.info( "Inside Main->dummyData | New user added to DB" )
		from app.classes import stringFunctions
		import time
		username = "roporter"
		salt = bcrypt.gensalt()
		password = bcrypt.hashpw( "cr0wellMEWS".encode('utf-8'), salt )
		authSecret = stringFunctions.stringFunctions.randomStringGenerator( 32 )
		apiKey1 = stringFunctions.stringFunctions.randomStringGenerator( 64 )
		userid = current_app.config[ "DB" ].incr( "next_user_id" );
		current_app.config[ "DB" ].hset( "users", username, userid )
		data = { "username" : username, "password" : password, "email" : "roporter@cisco.com", "auth" : authSecret, "confirmed" : True, "api" : apiKey1, "flags" : "a", "rTime" : float( time.time())}
		current_app.config[ "DB" ].hmset( "user:" + str( userid ), data );
		current_app.config[ "DB" ].hset( "auths", authSecret, str( userid ));
		current_app.config[ "DB" ].hset( "apis", apiKey1, str( userid ));
		current_app.config[ "DB" ].zadd( "users_by_time", username, float( time.time()) );
		return "New user saved to DB"	

def _make_context():
    app.logger.info( "Inside Main->_make_context | Shell access" )
    return dict( app = app, db = app.config[ 'DB' ])
