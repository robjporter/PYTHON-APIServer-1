from flask import Blueprint

bing = Blueprint( 'bing',  __name__, template_folder = 'templates', static_folder = 'bing/static'  )

from . import views
