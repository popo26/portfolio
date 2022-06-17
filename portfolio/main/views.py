import datetime
from flask import render_template
from . import main_bp

YEAR = datetime.datetime.now().year

@main_bp.route("/")
def landing():
    return render_template('main/landing.html', year=YEAR)

@main_bp.route('/index')
def index():
    return render_template("main/index.html", year=YEAR)

@main_bp.route('/portfolio')
def portfolio():
    return render_template("main/portfolio.html", year=YEAR)
