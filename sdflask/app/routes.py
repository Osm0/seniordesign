from flask import render_template, request
from werkzeug.exceptions import BadRequest
from app import app

@app.route('/')

@app.route('/index')
def index():
    user = {'username':'Jisoo'}
    return render_template('home.html')#, title = 'Home', user = user)

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/patient_info.html')
def patient_info():
    return render_template('patient_info.html')

@app.route('/category.html')
def category():
    return render_template('category.html')

@app.route('/search_patient.html')
def search_patient():
    return render_template('search_patient.html')

@app.route('/results.html')
def results():
    return render_template('results.html')

@app.route('/camera.html', methods = ['GET','POST'])
def camera():
    return render_template('camera.html', type = 'multistix')

@app.route('/camera2.html',methods = ['GET','POST'])
def camera2():
    return render_template('camera.html',type = 'pregnancy')

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    print("bad request")
    return render_template('category.html', request = 'bad')

#app.register_error_handler(400, lambda e: 'bad request!')



