import os
from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

load_dotenv()

bootstrap = Bootstrap()
mail = Mail()
csrf = CSRFProtect()

def create_app(config_name = "default"):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app.config["SECRET_KEY"]= os.getenv('SECRET_KEY')

    bootstrap.init_app(app)
    csrf.init_app(app)

    from .main import main_bp
    from .contact import contact_bp
    from .resume import resume_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(resume_bp)

  
    if app.config['HTTPS_REDIRECT']:
        from flask_talisman import Talisman
        Talisman(app, content_security_policy={
                'default-src': [
                    "\'self\'", 
                    '*.googleapis.com',
                    '*.gstatic.com',
                    '*.fontawesome.com/',
                    'code.jquery.com',
                    'maxcdn.bootstrapcdn.com',   
                    'cdnjs.cloudflare.com',  
                    'cdn.fontawesome.com',
                    
                ],
                'img-src': '*',
            }
        )

    return app

    
