from flask import Flask, redirect, url_for, render_template

# application name

app = Flask(__name__) # can be any given name or __name__ to reference the filename

# rendering a html file as a function

@app.route("/")
def homepage():
    return render_template("index.html")

# passing values and parameters between the back and frontend

@app.route("/values/<param>")
def values(param: str):
    return render_template("values.html", content=param) # content is specified in the html template and param will take its place when flask renders it
    # multiple values and parameters can be passed through this way

# in a html template flask interprets text in this format: {% foo %} as python code 
# you can even pass parameters and use them as variables in the python code inside the html

@app.route("/python/<value>")
def python_inside_html(value):
    return render_template("html_python.html", content=int(value))

# running the script

if __name__ == "__main__": # if this script is the main program we'll run the code
    app.run()
else:
    exit(1)