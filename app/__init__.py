from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize SQLAlchemy and LoginManager only once
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind the SQLAlchemy instance and LoginManager to the app
    db.init_app(app)
    login_manager.init_app(app)

    # Import models and routes inside the create_app function to avoid circular imports
    from .models import User
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
