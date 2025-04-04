from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

# data stored in sessions are encrypted and the session itself is stored in the server
# to access the data in our session we need to define a "secret_key" which will be the 
# way the relevant data in the session will be decrypted or encrypted back again

app = Flask(__name__)
app.secret_key = "pedr9vskcray_secret" # any string can be a secret key but its wise to make it something complicated

# we can also define for how much time we want our session to last before it expires and the user has to login again
# this is how we make a session permanent and it changes the behaviour of our session to match the time defined

app.permanent_session_lifetime = timedelta(days=2) # after 2 days, this session will expire and all of its data will be cleared

# defining our pages

@app.route("/")
def homepage():
    return render_template("index.html")

# sessions are a way to store relevant data that needs to be reused by different pages throughtout our application
# sessions are server-sided, temporary and cease to exist when the browser is closed/exited and they are recreated when reloaded

@app.route("/login", methods=["POST", "GET"])
def loginpage():
    if request.method == "POST": 
        session.permanent = True # declaring this session as a permanent session
        usr = request.form["name"]
        session["usr"] = usr # sessions in flask are like a global dictionary, storing data in key -> value pairs that can be accessed by other pages
        return redirect(url_for("userpage"))
    else:
        if "usr" in session.keys(): # if "usr" is already logged in, redirect to the userpage
            return redirect(url_for("userpage"))
        else:
            return render_template("login.html")

@app.route("/user")
def userpage():
    if "usr" in session.keys(): # if "usr" is logged in the session, return his name
        user = session["usr"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("loginpage")) # else redirect to the loginpage

# to ensure that when someone logs out, their session and the information stored in it is deleted/cleared

@app.route("/logout")
def logout():
    user = session.pop("usr", default=None) # if the key "usr" exists in the session, it returns its value and removes it
    # the default parameter is for cases in which the key doesn't exist in the session, in this case it'll do nothing
    print(f"session ended: user -> {user} removed")
    return redirect(url_for("loginpage"))

# running the application

if __name__ == "__main__":
    app.run(debug=True)
else:
    exit(1)