from flask import Blueprint

psc = Blueprint( 'psc',  __name__, template_folder = 'templates', static_folder = 'psc/static'  )

from . import views
