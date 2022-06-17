from flask import Blueprint

main_bp = Blueprint("main_bp", __name__,
                    url_prefix="/",
                    template_folder="templates",
                    static_folder="static", 
                    static_url_path='/static',
                    )

from . import views