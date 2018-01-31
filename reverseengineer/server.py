from flask import Flask, render_template, request, redirect
# render_template looks for a folder called `templates`
# templates is to do the whole design of the page
app = Flask(__name__)
@app.route("/")
def index():
    print "I'm in the terminal... Mwahahahahahaha!!"
    return render_template("index.html")

@app.route ("/users", methods=['post'])
def projects():
    print "project baby 1K"
    name = request.form['name']
    email = request.form['email']

    return render_template("users.html")


@app.route ("/about")
def about():
    "Aboot this life"
    return render_template("about.html")

app.run(debug=True)

