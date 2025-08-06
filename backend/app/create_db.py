#create_db.py
"""
Script to create the database and tables using the app's configuration.
"""
from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    db.create_all()
    print("Database and tables created successfully.")