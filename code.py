
from flask import Flask
import os

app = Flask(_name_)

@app.route("/")
def hello():
    """Return a friendly greeting."""
    return "Welcome to my Flask app!"

@app.route("/goodbye")
def goodbye():
    """Return a goodbye message."""
    return "Goodbye! See you next time."

if _name_ == "_main_":
    # Get host and port from environment variables or use defaults
    host = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_RUN_PORT", 8080))
    
    # Run the app with debug mode enabled for development
    app.run(host=host, port=port, debug=True)
