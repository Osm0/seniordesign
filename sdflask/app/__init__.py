from flask import Flask, render_template, request
from config import Config
from mancrop import cutImage, delete_files, cut_pregnancy
from wtforms import Form, BooleanField, StringField, PasswordField, validators

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
import os



UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload', methods=['POST'])
def upload_file():

    file = request.files['image']
    print("out")
    print(file)


    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    filename = file.filename
    file.save(f)
    
    
    print(f)
    
    
    print("hi")
    if 'multistix' in request.form:
        colors = cutImage(f)
        files = os.listdir('./crop_test')
        print("in app:{}".format(colors[2]))
        print("in app color len :{}".format(len(colors)))
    
        if(len(colors) != 11):
            delete_files(files)
            return render_template('category.html',request = 'bad')
        
        delete_files(files)
        return render_template('results.html', results = colors)

    elif 'pregnancy' in request.form:
        print('pregnancy')
        color = cut_pregnancy(f)
        files = os.listdir('./crop_test')
        delete_files(files)
        
        return render_template('category.html',request = 'bad')
