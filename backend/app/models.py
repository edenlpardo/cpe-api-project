#models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import JSON

# Initialize the SQLAlchemy ORM object
db = SQLAlchemy()

class CPE(db.Model):
    """
    Database model representing a CPE (Common Platform Enumeration) entry.
    Stores CPE title, URIs for versions 2.2 and 2.3, references, and deprecation dates.
    """
    __tablename__ = 'cpe_data'
    
    # Primary key for the CPE entry
    id = db.Column(db.Integer, primary_key=True)
    # Title of the CPE entry, indexed for faster search
    cpe_title = db.Column(db.VARCHAR, index=True, nullable=False)
    # CPE 2.2 URI, indexed for faster search
    cpe_22_uri = db.Column(db.Text, index=True, nullable=False)
    # CPE 2.3 URI, indexed for faster search
    cpe_23_uri = db.Column(db.Text, index=True, nullable=False)
    # Reference links associated with the CPE entry, stored as JSON
    reference_links = db.Column(db.JSON, nullable=False)
    # CPE 2.2 deprecation date, stored as a date type, indexed for faster search
    cpe_22_deprecation_date = db.Column(db.Date, index=True, nullable=True)
    # CPE 2.3 deprecation date, stored as a date type, indexed for faster search
    cpe_23_deprecation_date = db.Column(db.Date, index=True, nullable=True)
        
    def to_json(self):
        """
        Convert the CPE object into a JSON-serializable dictionary.
        Dates are returned as ISO-formatted strings or None if not available.
        """
        return{
            'id': self.id,
            'cpe_title': self.cpe_title,
            'cpe_22_uri': self.cpe_22_uri,
            'cpe_23_uri': self.cpe_23_uri,
            'reference_links': self.reference_links,
            'cpe_22_deprecation_date': self.cpe_22_deprecation_date.isoformat() if self.cpe_22_deprecation_date else None,
            'cpe_23_deprecation_date': self.cpe_23_deprecation_date.isoformat() if self.cpe_23_deprecation_date else None
        }
