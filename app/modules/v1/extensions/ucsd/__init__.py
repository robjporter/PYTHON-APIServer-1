from flask import Blueprint

ucsd = Blueprint( 'ucsd',  __name__, template_folder = 'templates', static_folder = 'ucsd/static'  )
from . import views
