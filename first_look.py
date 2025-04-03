from flask import Flask, redirect, url_for

# application name

app = Flask(__name__) # can be any given name or __name__ to reference the filename

# homepage function

@app.route("/")
def homepage():
    return "Hello, this is the homepage! <h1>hello world</h1>"

# receiving parameters

@app.route("/<name>") # whatever we type in the url will be passed as a parameter to the function
def userpage(name: str):
    return f"Hello {name} how are you doing?"

# redirecting based on conditions

admin = False

@app.route("/admin")
def adminpage():
    if not admin:
        print("redirected to -> homepage")
        return redirect(url_for("homepage")) # function name we want to be redirected for
    else:
        return "Welcome to the admin page."

# redirecting and passing parameters

manager = False

@app.route("/manager")
def managerpage():
    if not manager:
        print("redirected to -> userpage/stranger")
        return redirect(url_for("userpage", name="stranger")) # ("function_name", parameter_name="parameter")
    else:
        return "Welcome to the manager page."

# running the script

if __name__ == "__main__": # if this script is the main program we'll run the code
    app.run()
else:
    exit(1)