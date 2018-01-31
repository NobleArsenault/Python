from flask import Flask, render_template, request, session
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'noble'

@app.route('/', methods=['get','post'])
def index():
    session['state'] = None
    session['time'] = datetime.now()
    session['gold'] = 0
    session['addgold'] = 0
    session['building']= None
    if "all" not in session: 
        session['all']= []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def result():
    if request.form['building'] == 'farm':
        session['addgold'] = random.randint(10,20)
        session['gold'] += session['addgold']
        session['building'] = 'farm'
        message= "You entered the session['building'] and won session['addgold'] gold pieces on session['time']"
        session["all"].append(message)
    elif request.form['building'] == 'cave':
        session['addgold'] = random.randint(5,10)
        session['gold'] += session['addgold']
        session['building'] = 'cave'
        message= "You entered the session['building'] and won session['addgold'] gold pieces on session['time']"
        session["all"].append(message)
    elif request.form['building'] == 'house':
        session['addgold'] = random.randint(2,5)
        session['gold'] += session['addgold']
        session['building'] = 'house'
        message= "You entered the session['building'] and won session['addgold'] gold pieces on session['time']"
        session["all"].append(message)
    elif request.form['building'] == 'casino':
        session['addgold'] = random.randint(-50,50)
        session['gold'] += session['addgold']
        session['building'] = 'casino'
        message= "You entered the session['building'] and won session['addgold'] gold pieces on session['time']"
        session["all"].append(message)
    return render_template('index.html')

app.run(debug=True)




"""
from flask import Flask, render_template, request, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template('enterSomething.html')

@app.route('/result', methods=['POST'])
def result():
    vehicle = request.form.get('vehicle')
    year = request.form.get('year')
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    return render_template('results.html', vehicle=vehicle, year=year, firstname=firstname, lastname=lastname)

app.run(debug=True)
"""