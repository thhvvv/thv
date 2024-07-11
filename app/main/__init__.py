from flask import Blueprint

# Create a blueprint named 'main'
main_bp = Blueprint('main', __name__, template_folder='templates', static_folder='static')

# Import views module to register routes
from . import views
