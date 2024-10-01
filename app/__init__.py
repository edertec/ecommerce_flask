from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.controller.home_controller import home_bp
from app.controller.cart_controller import cart_bp
from app.controller.product_controller import product_bp
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = 'supersecretkey'  # Change to a random secret key for production
    app.config.from_object(Config)
    
    # Initialize the database
    db.init_app(app)
    
    # Register Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(product_bp)
    
    # Create the database tables if they don't exist yet
    with app.app_context():
        db.create_all()
    
    return app
