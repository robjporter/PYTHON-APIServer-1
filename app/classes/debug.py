from flask import current_app

def setupDebug( app ):
    from flask_debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension( app )