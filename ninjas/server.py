from flask import Flask, render_template, request, redirect

app = Flask(__name__)
@app.route("/")
def index():
    print "I'm in the terminal... Mwahahahahahaha!!"
    return render_template("index.html")

@app.route ("/ninjas")
def ninjas():
    print "Aboot this life"
    return render_template("ninjas.html")

@app.route ("/dojo")
def dojo():
    return render_template("dojo.html")

app.run(debug=True)