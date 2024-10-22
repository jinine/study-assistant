from flask import Flask
from database import db_session

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the AI-Powered Study Assistant!"

if __name__ == '__main__':
    app.run(debug=True)
