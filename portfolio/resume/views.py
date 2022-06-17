import datetime
from flask import render_template
from . import resume_bp

YEAR = datetime.datetime.now().year

@resume_bp.route("/")
def resume():
    return render_template('resume/resume.html', year=YEAR)