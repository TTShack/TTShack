from flask import Flask, render_template

app = Flask(__name__)  #creates an instance of flask

@app.route('/')
def index():
    return render_template("index.html") #renders template from template folder

@app.route('/about')
def about():
    return render_template("about.html")