# CPE Data Collection and API Development

This project parses a CPE XML dictionary, stores it in a SQLite database, and serves it via a RESTful Flask API.

## Getting Started:

### Prerequisites:

- Python 3.8+
- pip

### Installation:

1. Create a virtual environment (optional but recommended):

   --> bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

2. Install dependencies:

    --> bash
    pip install -r requirements.txt

3. Download the official-cpe-dictionary_v2.3.xml file and place it in the root directory:

4. Create the database:

    --> bash
    python create_db.py

5. Load the CPE data:

    --> bash
    python load_data.py

6. Run the API server:

    --> bash
    python run.py

- The API will be available at http://127.0.0.1:5000
    - Can be changed for production in run.py

## Project Structure:
- app/ : Flask app modules
- instance/ : SQLite DB will be created here
- create_db : Initializes database schema
- load_data.py : Parses XML and populates the DB
- run.py : Starts the API server