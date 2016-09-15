from flask import Blueprint

country = Blueprint( 'country',  __name__, template_folder = 'templates', static_folder = 'country/static'  )

from . import views
