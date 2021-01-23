from flask import Flask, render_template

app = Flask(__name__)  #creates an instance of flask

@app.route('/')
def index():
    title = "Act On It!"
    return render_template("index.html", title=title) #renders template from template folder

@app.route('/about')
def about():
    return render_template("about.html")

