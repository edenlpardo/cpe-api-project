#load_data.py
from . import create_app
from .models import db, CPE
from .xml_parser import parse_cpe_xml
from datetime import datetime

# Initialize Flask app
app = create_app()

def safe_date(date_str):
    """
    Safely convert a date string to a datetime.date object.
    Returns None if the string is not in the expected format.
    """
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None

def main():
    """
    Main function to parse CPE XML data and insert it into the database.
    """
    print("Starting CPE XML parsing...")

    xml_file_path = "official-cpe-dictionary_v2.3.xml"
    try:
        cpe_entries = parse_cpe_xml(xml_file_path)
        print(f"Parsed {len(cpe_entries)} CPE entries from XML.")
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return

    # Insert parsed CPE entries into the database with app context
    with app.app_context():
        try:
            for entry in cpe_entries:
                cpe = CPE(
                    cpe_title=entry.get('cpe_title', 'N/A'),
                    cpe_22_uri=entry.get('cpe_22_uri', 'N/A'),
                    cpe_23_uri=entry.get('cpe_23_uri', 'N/A'),
                    reference_links=entry.get('reference_links', []),
                    cpe_22_deprecation_date=safe_date(entry.get('cpe_22_deprecation_date')),
                    cpe_23_deprecation_date=safe_date(entry.get('cpe_23_deprecation_date'))
                )
                db.session.add(cpe)

            db.session.commit()
            print(f"Successfully inserted {len(cpe_entries)} CPE entries.")
        except Exception as e:
            db.session.rollback()
            print(f"Error inserting into DB: {e}")

if __name__ == '__main__':
    main()