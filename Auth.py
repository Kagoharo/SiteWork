from flask import request, app, flash, session, url_for
from flask_login import login_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from Models import LoginCredentials
from UserLogin import UserLogin
from main import db


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        session.pop('_flashes', None)
        email = request.form.get('email')
        password = request.form.get('password')

        user = LoginCredentials.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')

    return True


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = db.getUserByEmail(request.form['email'])
        if user and check_password_hash(user['psw'], request.form['psw']):
            userlogin = UserLogin().create(user)
            login_user(userlogin)
            return redirect(url_for('main'))

        flash("Неверная пара логин/пароль", "error")

    return