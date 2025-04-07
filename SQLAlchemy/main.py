from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secret_key" 
app.permanent_session_lifetime = timedelta(days=2)

# SQLAlchemy is an easy way to wire your flask applications with a SQL database without needing to
# write SQL queries, it allows devs to access and manage a SQL database using a Pytonic domain language

# database config

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3' # users = table_name
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# setting up our database

db = SQLAlchemy(app)

# users is our table name!
class users(db.Model): # db.Model is our inheritance, it has some predefined methods and other things that indicates this class is a table

    _id = db.Column("id", db.Integer, primary_key=True) # creating the "id" column
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(150))

    # other data types in Flask-SQLAlchemy:
    # https://docs.sqlalchemy.org/en/20/core/type_basics.html#the-uppercase-datatypes

    def __init__(self, name, email):
        self.name = name
        self.email = email

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
        
        # here we'll verify if there's already an user with this name, if there isn't we'll create and add it to our database

        found_user = users.query.filter_by(name=usr).first()

        if found_user:
            session["email"] = found_user.email
            print(found_user.email, " - data stored")
        else:
            user = users(usr, None)
            db.session.add(user)
            db.session.commit()

        print(f"User {usr} logged in.")
        flash(f"Login successful!")
        return redirect(url_for("userpage"))
    else: # if request.method == "GET"
        if "usr" in session.keys():
            flash(f"You are already logged in.")
            return redirect(url_for("userpage"))
        else:
            return render_template("login.html")

# userpage

@app.route("/user", methods=["POST", "GET"])
def userpage():
    email = None
    if "usr" in session.keys():
        usr = session["usr"]
        if request.method == "GET":
            if "email" in session.keys():
                email = session["email"]
                return render_template("user.html", email=email, user=usr)
            else:
                return render_template("user.html", user=usr)
        else: # if request.method == "POST"
            if "logout" in request.form.keys():
                return redirect(url_for("logout"))
            else:
                email = request.form["email"]
                session["email"] = email
                found_user = users.query.filter_by(name=usr).first()
                found_user.email = email
                db.session.commit()
                flash("Email was saved!")
                print(found_user.email, " - new data")
                return render_template("user.html", email=email, user=usr)
    else:
        flash("You are not logged in.")
        return redirect(url_for("loginpage"))
    
# view all users in the database

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all()) # all the information in the users table

@app.route("/delete/<user>")
def delete(user: str):
    found_user = users.query.filter_by(name=user).first()
    if found_user:
        del_user = users.query.filter_by(name=user).delete()
        db.session.commit()
        flash(f"User {user} successfully deleted.")
        print(f"user {user} deleted.")
        return redirect(url_for("loginpage"))
    else:
        flash("This user does not exist.")
        return redirect(url_for("loginpage"))

# logout

@app.route("/logout")
def logout():
    if "usr" in session.keys(): 
        user = session.pop("usr", default=None)
        session.pop("email", default=None)
        flash(f"Session ended, {user} logged out.", "info")
        print(f"session ended: user -> {user} logged out")
        return redirect(url_for("loginpage"))
    else:
        flash("You weren't logged in, so you can't logout.")
        return redirect(url_for("loginpage"))

# running the application

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # creating our database if it don't exist
    app.run(debug=True)
else:
    exit(1)

# Flask-SQLAlchemy Guide:
# https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application