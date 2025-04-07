from flask import Blueprint, render_template
import os

filename = os.path.basename(__file__).replace(".py", "")

bar = Blueprint(filename, __name__, static_folder="static", template_folder="templates")

@bar.route("/home")
@bar.route("/")
def homepage():
    return render_template("home.html")

@bar.route("/test")
def test2():
    return "<h1>Second Test</h1>"