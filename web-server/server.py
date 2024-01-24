from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")
def index(): 
    return render_template("index.html")


@app.route("/index.html")
def backhome():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/blog.html")
def blog():
    return render_template("blog.html")