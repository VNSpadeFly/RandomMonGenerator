from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialisieren der Datenbank
    db.init_app(app)

    # Routen importieren und registrieren
    from .routes import api
    app.register_blueprint(api)

    return app
