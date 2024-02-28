from flask import Flask, render_template, request,send_file,url_for,redirect
import pandas as pd
from io import StringIO
import pickle
from keras.models import load_model
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'csv', 'xlsx','pdf','docx'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        file_contents = file.read()
        file.seek(0)  # Reset file pointer to the beginning
        print(file_contents)


if __name__ == "__main__":
    app.run(debug=True)