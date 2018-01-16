from flask import Flask, render_template
# render_template looks for a folder called `templates`
# templates is to do the whole design of the page
app = Flask(__name__)
@app.route("/")
def index():
    print "goodbye world"
    return render_template("index.html")

@app.route ("/test")
def function():
    return "test"


app.run(debug=True)
