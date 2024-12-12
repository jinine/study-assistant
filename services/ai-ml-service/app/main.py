from flask import Flask
from app.routes import register_routes
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Register routes
register_routes(app)

@app.route('/')
@cross_origin(origins="http://localhost:3000")
def home():
    return {"message": "Welcome to the Smart Study Assistant API"}

if __name__ == "__main__":
    app.run(debug=True)