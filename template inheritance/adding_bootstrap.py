from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html") # inheriting base template with bootstrap

if __name__ == "__main__":
    app.run(debug=True)
else:
    exit(1)