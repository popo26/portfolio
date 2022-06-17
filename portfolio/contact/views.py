from flask import render_template
import datetime
from portfolio.contact.forms import ContactForm
from . import contact_bp
from .forms import ContactForm
from flask import request
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MAIL_EMAIL= os.getenv("MAIL_EMAIL")
MAIL_PASSWORD= os.getenv("MAIL_PASSWORD")

YEAR = datetime.datetime.now().year

@contact_bp.route("/", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        name = request.form["name"]
        email = request.form['email']
        message = request.form['message']

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MAIL_EMAIL, MAIL_PASSWORD)
            connection.sendmail(
                from_addr= email, 
                to_addrs=MAIL_EMAIL, 
                msg=f"Subject:Received a message from Portfolio site\n\n{message}\nfrom: {name}")
        return "Successfully Submitted"

    return render_template('contact/contact.html', form=form, year=YEAR)
