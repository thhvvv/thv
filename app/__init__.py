from flask import Flask
from flask_bootstrap import Bootstrap
from .config import config_options

# Initialize Bootstrap instance (no need to initialize app here)
bootstrap = Bootstrap()

# Function to create the app
def create_app(config_name):
    app = Flask(__name__)

    # Load configuration from the config_options dictionary
    app.config.from_object(config_options[config_name])

    # Initialize Bootstrap with the app instance
    bootstrap.init_app(app)

    # Register blueprints
    from .main import main_bp as main_blueprint
    app.register_blueprint(main_blueprint)

    # Import and initialize other components like models, etc.
    # from .models import db
    # db.init_app(app)

    return app

# Initialize the app with a default configuration (useful for scripts or shell)
app = create_app('development')
