#delete_db.py
"""
Script to drop all tables and delete the SQLite database file.
"""
import os
from app import create_app
from app.models import db

app = create_app()

with app.app_context():
    print("All tables dropped.")
    db.drop_all()

# Delete the actual SQLite file
db_path = os.path.join("instance", "cpe_data.db")
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Deleted database file at: {db_path}.")
else:
    print("Database file not found.")