"""Main application and routing logic for twit v twit"""
from flask import Flask
from .models import DB

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @app.route('/')
    def root():
        return "Welcome to Twit_V_Twit"
    return app    
