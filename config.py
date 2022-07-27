import os
from dotenv import load_dotenv

load_dotenv()

class Config():
    HTTPS_REDIRECT = False

    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    ACL = 'public-read'
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
    S3_REGION = os.getenv('S3_REGION') 
    S3_BUCKET_PATH = os.getenv('S3_BUCKET_PATH')

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_EMAIL = os.getenv("MAIL_EMAIL")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

        
    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(Config):
  
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        import logging
        from logging.handlers import SMTPHandler
        creds = None
        secure = None
        if getattr(cls, 'MAIL_EMAIL', None) is not None:
            creds = (cls.MAIL_EMAIL, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                # logging: to use TLS, must pass tuple (can be empty)
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.MAIL_SENDER,
            toaddrs=[cls.APP_ADMIN],
            subject=cls.APP_MAIL_SUBJECT_PREFIX + " Application Error",
            credentials=creds,
            secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

class HerokuConfig(ProductionConfig):
    # HTTPS_REDIRECT = True if os.environ.get('DYNO') else False
    HTTPS_REDIRECT = True if os.environ.get('HTTPS_REDIRECT') else False
    # HTTPS_REDIRECT = True
    # SECURE_SSL_REDIRECT=True if os.environ.get('SECURE_SSL_REDIRECT') else False
    # SECURE_SSL_REDIRECT=True

    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler
        file_handler.setLevel(file_handler, level=logging.INFO)
        app.logger.addHandler(file_handler)

        from werkzeug.middleware.proxy_fix import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

config ={"default":Config,
         'heroku': HerokuConfig}