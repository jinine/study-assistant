from flask import Flask
from app.routes import register_routes
import os

app = Flask(__name__)

# Register routes
register_routes(app)

@app.route('/')
def home():
    return {"message": "Welcome to the Smart Study Assistant API"}

if __name__ == "__main__":
    app.run(debug=True)