#run.py
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Run the app in debug mode; change for production as needed
    app.run(host="127.0.0.1", port=5000, debug=True)
