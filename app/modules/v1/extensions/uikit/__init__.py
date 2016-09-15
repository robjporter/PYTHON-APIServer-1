from flask import Blueprint

uikit = Blueprint( 'uikit',  __name__, template_folder = 'templates', static_folder = 'static' )

from . import views
