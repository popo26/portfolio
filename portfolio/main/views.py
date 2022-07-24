import datetime
from flask import render_template, current_app, redirect, url_for
from . import main_bp
import boto3


@main_bp.context_processor
def base():
    YEAR = datetime.datetime.now().year
    return dict(year=YEAR) 


@main_bp.route("/")
def landing():
    return render_template('main/landing.html')

@main_bp.route('/introduction')
def index():
    return render_template("main/index.html")

@main_bp.route('/portfolio')
def portfolio():
    return render_template("main/portfolio.html")

    #Serve image from S3
@main_bp.route('/download/<resource>')
def download_image(resource):
    """ resource: name of the file to download"""
    s3 = boto3.client('s3',
                      aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
                      aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'])

    url = s3.generate_presigned_url('get_object', Params = {'Bucket': current_app.config['S3_BUCKET_NAME'], 'Key': resource}, ExpiresIn = 100)
    return redirect(url, code=302)

