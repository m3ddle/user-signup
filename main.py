# TODO: Restructure html/page layout. Centered box with proper divs no html tables.
# TODO: Make pages into proper html template structure


from flask import Flask, request, redirect, render_template
app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/validate", methods=["POST"])
def validate():

    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username == "":
        username_error = "Name cannot be blank. "
    elif len(username) < 3 or len(username) > 20:
        username_error = username_error + \
            "Username must be between 3 and 20 characters in length. "

    if password == "":
        password_error = "Password cannot be blank. "

    elif len(password) < 3 or len(password) > 20:
        password = ""
        verify = ""
        password_error = password_error + \
            "Password must be between 3 and 20 characters in length. "

    if verify == "":
        verify_error = "Password cannot be blank. "

    if " " in username:
        username_error = username_error + "Username cannot contain spaces. "

    if " " in password:
        password = ""
        verify = ""
        password_error = password_error + "Password cannot contain spaces. "

    if password != verify:
        password = ""
        verify = ""
        verify_error = verify_error + "Does not match password. "

    if email == "":
        pass
    elif "@" not in email or "." not in email or " " in email:
        email_error = email_error + "Please enter a valid email address. "

    if not username_error and not password_error and not email_error and not verify_error:
        return render_template("welcome.html", username=username)
    else:
        return render_template("index.html", username_error=username_error, password_error=password_error, email_error=email_error, verify_error=verify_error, username=username,
                               email=email)


@app.route("/welcome", methods=["POST"])
def welcome():
    username = request.form["username"]
    return render_template("welcome.html", username=username)


app.run()
