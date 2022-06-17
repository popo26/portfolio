from flask import render_template

import datetime
from portfolio.contact.forms import ContactForm
from . import contact_bp
from .forms import ContactForm

YEAR = datetime.datetime.now().year

@contact_bp.route("/")
def contact():
    form = ContactForm()
    return render_template('contact/contact.html', form=form, year=YEAR)
