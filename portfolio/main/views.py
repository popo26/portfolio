import datetime
from flask import render_template
from . import main_bp


@main_bp.context_processor
def base():
    YEAR = datetime.datetime.now().year
    return dict(year=YEAR) 


@main_bp.route("/")
def landing():
    return render_template('main/landing.html')

@main_bp.route('/index')
def index():
    return render_template("main/index.html")

@main_bp.route('/portfolio')
def portfolio():
    return render_template("main/portfolio.html")
