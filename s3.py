from flask import Flask, render_template, request
import boto3
app = Flask(__name__)
from werkzeug.utils import secure_filename

s3 = boto3.client(
    's3',
    aws_access_key_id="AKIA53NVE7A42R3NXLHD",
    aws_secret_access_key="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",
    #aws_session_token="FwoGZXIvYXdzEML//////////wEaDIorM30+m8cy3rh+oSLFAdLZVh6hCcTnq0BJrlJWUIPRB1w/Hxmh3iGzehlbMLzIxroNYedxHR/WFNBi4V+nuIaiextpotUG2YXP59y4dmZlLbGqpuKqMMDiUdPul3PO+R20BiKu2XS5TMKo0zOv+V70TVhHzi59ZLDh2GbuOAGXtBNJ/y09mhElSK9kW3sdYITya3kO1vp9D4vRuLuqD8DbuNeMb9LEcKT0XHR4EVQuxYjWTJ+EteWEc/bmrdLWKpsZ9pW+lMVKazC6N1MuQpk9XctFKKKR/ZcGMi0XcOWpa2fubVuIl0d//nizc2Og2hCl9IJv3u2j4BweoB0Ae6pPmvTRJsdrz/0="
)
BUCKET_NAME='test9959'

@app.route('/')  
def home():
    return render_template("index.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                msg = "Upload Done ! "

    return render_template("index.html",msg =msg)




if __name__ == "__main__":
    
    app.run(debug=True)


