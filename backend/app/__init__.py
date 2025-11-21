import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

from .extensions import db
from .controllers import all_blueprints

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL no está configurada.")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    for bp in all_blueprints:
        app.register_blueprint(bp)

    # Rutas globales
    @app.route("/")
    def index():
        return "¡El backend de Flask para IAM Manager está funcionando!"

    @app.route("/api/health")
    def health_check():
        return jsonify({"status": "ok", "message": "API is healthy"}), 200

    return app
