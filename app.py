from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/hardware')
def about():
    return render_template("hardware.html")


@app.route('/')
def login():
    return render_template("Login.html")


if __name__ == "__main__":
    app.run()