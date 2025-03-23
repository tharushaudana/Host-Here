from flask import Flask
from routes.main import main_bp
from routes.file import file_bp

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object('config.Config')

    app.register_blueprint(main_bp)
    app.register_blueprint(file_bp)

    return app