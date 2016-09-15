from flask import Blueprint

default = Blueprint( 'default',  __name__, template_folder = 'templates', static_folder = 'static', static_url_path = 'default/static' )

from . import views
#views.setup()
