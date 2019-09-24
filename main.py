# TODO: Restructure html/page layout. Centered box with proper divs no html tables.
# TODO: Make pages into proper html template structure
# TODO: Add error handling for improper/blank fields

from flask import Flask, request, redirect, render_template
app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/welcome", methods=["POST"])
def welcome():
    username = request.form["username"]
    return render_template("welcome.html", username=username)


app.run()
