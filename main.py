
#latest
from flask import Flask
from flask_restx import Api
from models import Notes, User
from exts import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from notes import notes_ns
from auth import auth_ns
from flask_cors import CORS
from config import DevConfig
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from config import ProdConfig


load_dotenv()

def create_app():
    app = Flask(__name__)

    # Determine environment (dev or prod)
    env = os.getenv("FLASK_ENV", "development")  # Default to 'development' if not set
    if env == "production":
        app.config.from_object(ProdConfig)
    else:
        app.config.from_object(DevConfig)

    CORS(app)

    db.init_app(app)
    migrate = Migrate(app, db)
    JWTManager(app)

    api = Api(app, doc="/docs")

    api.add_namespace(notes_ns)
    api.add_namespace(auth_ns)

    @app.route("/")
    def index():
        return "Welcome Home Flask"

    # Model (serializer)
    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "Notes": Notes, "User": User}

    return app
app=create_app()

# Run the application
if __name__ == '__main__':
    # Ensure the app runs on the appropriate host and port (useful for local dev)
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
