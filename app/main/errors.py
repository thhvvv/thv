from flask import render_template
from . import main_bp  # Import the blueprint object for the 'main' module

# Example error handler for 404 Not Found error
@main_bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

# Example error handler for 500 Internal Server Error
@main_bp.app_errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

# Additional error handlers as needed for other HTTP errors
# For example, 403 Forbidden, 401 Unauthorized, etc.
