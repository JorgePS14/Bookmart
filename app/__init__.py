from flask import Flask, render_template, request
from app.dbHandler import setDatabaseEnv

def create_app():
    app = Flask(__name__)
    db = setDatabaseEnv(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
