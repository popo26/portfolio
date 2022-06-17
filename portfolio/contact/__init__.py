from flask import Blueprint

contact_bp = Blueprint("contact_bp", __name__,
                        url_prefix="/contact",
                        template_folder="templates",
                        static_folder="static", 
                        static_url_path='/static',
                    )


from . import views