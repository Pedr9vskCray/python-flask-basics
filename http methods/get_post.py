from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# when not defining which methods are allowed for a certain page, the default is a GET request

@app.route("/")
def homepage():
    return render_template("index.html")

# when defining methods, only the defined methods are allowed

@app.route("/login", methods=["POST", "GET"])
def loginpage():
    if request.method == "POST": # if clause based on which http method was used to get to this page
        usr = request.form["foo_data"] # receiving the submitted data by the user in the <form><input></form> declared in "login.html"
        # if have more than one input coming from a form, request.form["key"] works like accesing a dictionary, where the keys are the name on the <input> in the .html file
        return redirect(url_for("userpage", user=usr))
    else:
        return render_template("login.html")

@app.route("/<user>")
def userpage(user: str):
    return f"<h1>Hello {user}!</h1>"

# running the application

if __name__ == "__main__":
    app.run(debug=True)
else:
    exit(1)

# learn more about http methods:
# https://www.w3schools.com/tags/ref_httpmethods.asp