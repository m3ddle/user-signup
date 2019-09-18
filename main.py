from flask import Flask, request, redirect, render_template
app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():

    return render_template("index.html")

app.run()
