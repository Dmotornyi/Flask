import  sqlite3
import os
from flask import Flask, render_template, url_for, request, flash

DATABASE = '/tmp/database.db'
SECRET_KEY = 'WRFERGEBDFdfgvdfbrbgtrbg'


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path,'database.db')))

@app.route('/')
@app.route('/login')
def login():
#    print(url_for('login') )
    return render_template("login.html")

@app.route('/index')
def index():
#    print(url_for('index') )
    return render_template("index.html")

@app.route('/hardware')
def about():
#    print(url_for('about') )
    return render_template("hardware.html")

@app.route('/new_input', methods=["POST","GET"] )
def new_input():
    if request.method == 'POST':
        if len(request.form['tech_name']) > 2:
            flash('Форма заполнена')
        else:
            flash('Заполните указаную форму', category='success')
    print(request.form)
#        print(url_for('new_input') )
    return render_template("new_input.html", category='error')


@app.route('/db_change')
def db_change():
#    print(url_for('db_change') )
    return render_template("db_change.html")

@app.route('/db_search')
def db_search():
#    print(url_for('db_search') )
    return render_template("db_search.html")



if __name__ == "__main__":
    app.run()