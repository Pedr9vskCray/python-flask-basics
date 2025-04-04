from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "pedr9vskcray_secret" 
app.permanent_session_lifetime = timedelta(days=2)

# homepage

@app.route("/")
def homepage():
    return render_template("index.html")

# loginpage

@app.route("/login", methods=["POST", "GET"])
def loginpage():
    if request.method == "POST": 
        session.permanent = True 
        usr = request.form["name"]
        session["usr"] = usr
        flash(f"Login successful!") 
        return redirect(url_for("userpage"))
    else:
        if "usr" in session.keys():
            flash(f"You are already logged in.")
            return redirect(url_for("userpage"))
        else:
            return render_template("login.html")

# userpage

@app.route("/user")
def userpage():
    if "usr" in session.keys():
        user = session["usr"]
        return render_template("user.html", user=user)
    else:
        flash(f"You are not logged in.")
        return redirect(url_for("loginpage"))

# logout

@app.route("/logout")
def logout():
    if "usr" in session.keys(): # if we have a "usr" and we try to logout
        user = session.pop("usr", default=None)
        flash(f"Session ended, {user} have been logged out.", "info") # flashing a message to inform the user he have successfully logged out
        print(f"session ended: user -> {user} logged out")
        return redirect(url_for("loginpage")) # redirects back to the loginpage
    else:
        flash("You weren't logged in, so you can't logout.") # if we don't have a "usr" and we try to logout
        return redirect(url_for("loginpage"))

# running the application

if __name__ == "__main__":
    app.run(debug=True)
else:
    exit(1)