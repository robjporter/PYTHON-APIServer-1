from app.main import app
import logging
from logging.handlers import RotatingFileHandler
from flask.ext.redis import FlaskRedis
from datetime import timedelta
from flask.ext.script import Manager

app.secret_key = "\xa2\xdf\xac\xba\xb6\x02uJI\xb3V3\x07\xa3\x04g&l\x80\xb6\xca\xed%\xc8\xd3\x1f1\xbd~ZRw"
handler = RotatingFileHandler( "error.log", maxBytes=10000, backupCount=1 )
handler.setLevel( logging.DEBUG )
app.logger.addHandler( handler )
app.config[ "REDIS_URL" ] = "redis://:cr0wellMEW$@localhost:6379/0"
#app.config[ "REDIS_URL" ] = "redis://:cr0wellMEW$@pub-redis-19834.us-east-1-4.3.ec2.garantiadata.com:19834/0"
app.config[ "redis_store" ] = FlaskRedis( app )
app.permanent_session_lifetime = timedelta( seconds=60 )
app.debug = True
manager = Manager( app )

#app.run()
manager.run()
