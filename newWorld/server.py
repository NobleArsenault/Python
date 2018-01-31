from flask import Flask, render_template
# render_template looks for a folder called `templates`
# templates is to do the whole design of the page
app = Flask(__name__)
@app.route("/")
def index():
    print "in the terminal"
    return render_template("index.html")

@app.route ("/projects")
def projects():
    return render_template("myprojects.html")


@app.route ("/about")
def about():
    return render_template("about.html")

app.run(debug=True)
