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
    session["name"] = request.form.get("firstname") + " " + request.form.get("lastname")
    return render_template('results.html', vehicle=vehicle, year=year, firstname=firstname, lastname=lastname)

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