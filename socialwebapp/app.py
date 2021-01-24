from flask import Flask, render_template, request

app = Flask(__name__)  #creates an instance of flask

@app.route('/')
def index():
    return render_template("index.html") #renders template from template folder

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/joinorg')
def joinorg():
    return render_template("joinorg.html")

@app.route('/hsorgs')
def hsorgs():
    return render_template("hsorgs.html")

@app.route('/corgs')
def corgs():
    return render_template("corgs.html")    


    
