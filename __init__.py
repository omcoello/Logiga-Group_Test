from flask import Flask
from .config import Config
from .database import SQLAlchemySingleton
from .views import main
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    db = SQLAlchemySingleton.get_instance(app)

    app.register_blueprint(main)
        
    with app.app_context():
        db.create_all()
    
    return app
