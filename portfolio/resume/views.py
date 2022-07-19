import datetime
from flask import render_template, request, current_app, Response, redirect, url_for
from . import resume_bp
import boto3

YEAR = datetime.datetime.now().year

@resume_bp.route("/")
def resume():
    return render_template('resume/resume.html', year=YEAR)



@resume_bp.route('/download-resume')
def download_resume():

    s3 = boto3.client('s3',
                    aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
                    aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'])

    file = s3.get_object(Bucket=current_app.config['S3_BUCKET_NAME'], Key='resume.pdf')
    
    return Response(
        file['Body'].read(),
        mimetype='application/pdf',
        headers={'Content-Disposition':"inline"}
    )