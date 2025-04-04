from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("child.html") # "child.html" inherits everything from "father.html" and extends it by adding code/content to the declared blocks in "father.html"

if __name__ == "__main__":
    app.run(debug=True) # automatically updates the website without needing to rerun the server 
else:
    exit(1)