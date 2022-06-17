import os
from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv

load_dotenv()

bootstrap = Bootstrap()

def create_app(config_name = "default"):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.config["SECRET_KEY"]= os.getenv('SECRET_KEY')

    bootstrap.init_app(app)

    from .main import main_bp
    from .contact import contact_bp
    from .resume import resume_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(resume_bp)

    return app

    
