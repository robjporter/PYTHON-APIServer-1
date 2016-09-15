import os
from base64 import b64decode
BASE_DIR = os.path.abspath( os.path.dirname( __file__ ))

class baseConfig:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SSL_DISABLE = True
    IGNORE_DIR_FILES = [ ".DS_Store" ]
    THREADS_PER_PAGE = 8
    CSRF_ENABLED     = True
    RATE_LIMIT_WINDOW = 2
    TRAP_HTTP_EXCEPTIONS = True
    BCRYPT_LOG_ROUNDS = 12
    CACHE_TYPE = 'simple'
    APP_LOG_NAME = "logs/app.log"
    ACCESS_LOG_NAME = "logs/access.log"
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = "\xa2\xdf\xac\xba\xb6\x02uJI\xb3V3\x07\xa3\x04g&l\x80\xb6\xca\xed%\xc8\xd3\x1f1\xbd~ZRw"
    CSRF_SESSION_KEY = "\x95\x007\xd8'\x7f\xcdO\x0e\x03\xe3\x00V\x8e\xf1\x96\x92\x8b\xc8\xdek3\x96\x8c\xe8\xab\xff\xee\xcd\xb7\x1b\xaa"
    SECRET_KEY = "\xa2\xdf\xac\xba\xb6\x02uJI\xb3V3\x07\xa3\x04g&l\x80\xb6\xca\xed%\xc8\xd3\x1f1\xbd~ZRw"
    REDIS_URL = "redis://:cr0wellMEW$@localhost:6379/0"
    SESSION_LIFETIME = 60
    BOWER_TRY_MINIFIED = True
    BOWER_SUBDOMAIN = None
    BOWER_REPLACE_URL_FOR = False
    BOWER_QUERYSTRING_REVVING = True
    BOWER_KEEP_DEPRECATED = True
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
    RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
    RECAPTCHA_OPTIONS = {'theme': 'white'}
    DEFAULT_MODULES = [ 'auth', 'default', 'error', 'server' ]
    TRACKING_IGNORE_EXT = [ ".css", ".png", ".js", ".jpg", ".images", "bower/" ]
    HIDDEN_FILES_FOLDERS = [ '__pycache__', '.DS_Store','county' ]
    EXTENSION_URL_SUBSET = "" # Should finish with /
    EXTENSION_DIR_NAME = "extensions"
    CACHE_HTTP_HEADER = "no-cache"
    BEACON = b64decode('R0lGODlhAQABAIAAANvf7wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==')
    EXTENSION_NAMESPACE = "roporter.namespace"
    APP_POWERED_BY = "powered by Flask"
    BLOCKED_IP = [ ] # "127.0.0.1" ]
    RAISE_ERROR_ON_MISSING_FEATURES = True
    MINIFY_PAGE = False
    #app.config[ "REDIS_URL" ] = "redis://:cr0wellMEW$@pub-redis-19834.us-east-1-4.3.ec2.garantiadata.com:19834/0"

class DevConfig( baseConfig ):
    DEBUG = True
    TESTING = True
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get( "MAIL_USERNAME" )
    MAIL_PASSWORD = os.environ.get( "MAIL_PASSWORD" )
    TRAP_BAD_REQUEST_ERRORS = True
    TRAP_HTTP_EXCEPTIONS = True
    FEATURE_FLAGS = {
        'unfinished_feature' : True,
    }

class StageConfig( baseConfig ):
    TESTING = True
    RATE_LIMIT_WINDOW = 4

class ProdConfig( baseConfig ):
    TESTING = False
    DEBUG = False
    RATE_LIMIT_WINDOW = 12
    FEATURE_FLAGS = {
        'unfinished_feature' : False,
    }
    MINIFY_PAGE = True

config = {
    "development" : DevConfig,
    "staging" : StageConfig,
    "production" : ProdConfig,
    "default": DevConfig
}
