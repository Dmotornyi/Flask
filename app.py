from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    print(url_for('index') )
    return render_template("index.html")

@app.route('/hardware')
def about():
    print(url_for('about') )
    return render_template("hardware.html")

@app.route('/login')
def login():
    print(url_for('Login') )
    return render_template("Login.html")


if __name__ == "__main__":
    app.run()