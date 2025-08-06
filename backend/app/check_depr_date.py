#check_depr_date.py
'''
Debugging script to verify the number of CPE entries with non-null deprecation dates.
'''
from app import create_app
from app.models import db, CPE

app = create_app()

with app.app_context():
    total_entries = CPE.query.count()
    non_null_22 = CPE.query.filter(CPE.cpe_22_deprecation_date.isnot(None)).count()
    non_null_23 = CPE.query.filter(CPE.cpe_23_deprecation_date.isnot(None)).count()

    print(f"Total entries: {total_entries}")
    print(f"Entries with non-null CPE 2.2 deprecation dates: {non_null_22}")
    print(f"Entries with non-null CPE 2.3 deprecation dates: {non_null_23}")
