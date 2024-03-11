import os

class Config:
    # Secret key for CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

    # Database configuration (SQLite for development)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-WTF CSRF protection
    WTF_CSRF_ENABLED = True
