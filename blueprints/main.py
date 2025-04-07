from flask import Flask, render_template, url_for
from admin.second import bar

app = Flask(__name__)
app.register_blueprint(bar, url_prefix="/foo")

@app.route("/test")
def test1():
    return "<h1>Original Test</h1>"

@app.route("/")
def homepage():
    return ""

if __name__ == "__main__":
    app.run(debug=True)
else:
    exit(1)