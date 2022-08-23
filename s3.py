from flask import Flask, render_template, request
import boto3
app = Flask(__name__)
from werkzeug.utils import secure_filename

s3 = boto3.client(
    's3',
    aws_access_key_id="",
    aws_secret_access_key="",
    #aws_session_token=""
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


