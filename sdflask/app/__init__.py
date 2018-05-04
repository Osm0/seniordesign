from flask import Flask, render_template, request
from config import Config
from mancrop import cutImage

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
import os



UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    filename = file.filename
    
    # add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
    file.save(f)
    
    print(f)
    colors = cutImage(f)
    print("in app:{}".format(colors[2]))
    print("in app color len :{}".format(len(colors)))
    
    
    return render_template('results.html', results = colors)