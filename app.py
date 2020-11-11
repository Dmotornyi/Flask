from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
    print(url_for('login') )
    return render_template("login.html")

@app.route('/index')
def index():
    print(url_for('index') )
    return render_template("index.html")

@app.route('/hardware')
def about():
    print(url_for('about') )
    return render_template("hardware.html")

@app.route('/new_input')
def new_input():
    print(url_for('new_input') )
    return render_template("new_input")



if __name__ == "__main__":
    app.run()