from flask import Blueprint

fun = Blueprint( 'fun',  __name__, template_folder = 'templates', static_folder = 'static' )

from . import views
