import  sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, g, redirect
from FDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash


DATABASE = '/Users/dmotornyi/PycharmProjects/Flask/database.db'
SECRET_KEY = 'WRFERGEBDFdfgvdfbrbgtrbg'


app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path,'database.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/')
@app.route('/login')
def login():
#    print(url_for('login') )
    return render_template("login.html")

@app.route('/register', methods=["POST", "GET"])
def register():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        if len(request.form['firstname']) > 4 and len(request.form['email']) > 4 and len(request.form['psw']) > 4 and request.form['psw'] == request.form['psw2']:
            hash = generate_password_hash(request.form['psw'])
            res = dbase.addUser(request.form['firstname'], request.form['email'], hash)
            if res:
                flash("Success registration", "success")
                return redirect(url_for('login'))
            else:
                flash("Bad enter information", "error")
        else:
            flash("Bad enter information", "error")
    return render_template("register.html")



@app.route('/index')
def index():
#    print(url_for('index') )
    return render_template("index.html")

@app.route('/hardware')
def about():
    db = get_db()
    dbase = FDataBase(db)
#    print(url_for('about') )
    return render_template("hardware.html", hardware=dbase.getHardwareList())

@app.route('/new_input', methods=["POST","GET"] )
def new_input():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if len(request.form['tech_name']) > 2 and len(request.form['who_issue']) > 2 and len(request.form['tech_type']) > 2 and len(request.form['tech_sn']) > 2 and len(request.form['tech_in']) > 2:
            res = dbase.addTech(request.form['who_issue'], request.form['tech_type'], request.form['tech_name'], request.form['tech_sn'], request.form['tech_in'], request.form['for_whom'], request.form['tech_locate'], request.form['tech_buisnes'], request.form['input_date'], request.form['input_coment'])
            if not res:
                flash('Заполните указаную форму', category='error')
            else:
                flash('Форма заполнена', category='success')
        else:
            flash('Заполните указаную форму', category='error')
    print(request.form)
    return render_template("new_input.html")


@app.route("/hardware/<int:id_hardware>")
def showhardware(id_hardware):
    db = get_db()
    dbase = FDataBase(db)
    hardware_details = dbase.getHardwareId(id_hardware)

    return render_template('hardware_detail.html', details=hardware_details)


@app.route('/db_change')
def db_change():
#    print(url_for('db_change') )
    return render_template("db_change.html")

@app.route('/db_search')
def db_search():
#    print(url_for('db_search') )
    return render_template("db_search.html")

@app.teardown_appcontext
def close_db(error):
    '''Закрываем соединение с БД, если оно было установлено'''
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.errorhandler(404)
def pageNot(error):
    return render_template("404.html")



if __name__ == "__main__":
    app.run(debug=True)