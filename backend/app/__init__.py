# app/__init__.py
from flask import Flask
from .models import db
from .views import api
import os

def create_app():
    """
    Factory function to create and configure the Flask app.
    Sets up SQLite database and registers API blueprint.
    Note: Can easily switch to postgres if more SQL features needed.
    """
    app = Flask(__name__)

    # Construct the full database path
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, "..", "instance", "cpe_data.db")
    
    # Configure the database URI and disable modification tracking
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Create database table within app context
    try:
        with app.app_context():
            db.create_all()
    except Exception as e:
        app.logger.error(f"Error creating the database: {e}")

    app.register_blueprint(api)

    return app
