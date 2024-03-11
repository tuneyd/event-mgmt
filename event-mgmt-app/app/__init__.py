from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

# Create the Flask application instance
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# Initialize the database
db = SQLAlchemy(app)

# Initialize database migrations
migrate = Migrate(app, db)

# Initialize the login manager
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'  # Specify the login view

# Import routes and models (to avoid circular imports)
from app import routes, models