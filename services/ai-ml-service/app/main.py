from flask import Flask
from app.routes import register_routes
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Register routes
register_routes(app)

@app.route('/')
def home():
    return {"message": "Welcome to the Smart Study Assistant API"}

if __name__ == "__main__":
    app.run(debug=True)