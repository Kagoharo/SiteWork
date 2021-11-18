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
        data = request.get_json()
        email = data["email"]
        password = data["password"]
        password2 = data["password_confirmation"]
        user = User.query.get(data["email"])
        if email != user.email and password == password2:
            new_user = User(email=data["email"], password=data["password"])
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"msg": "Account successfully created"}), 200
        elif email != user.email:
            return jsonify({"msg": "Email already in use"}), 401
        elif password != password2:
            return jsonify({"msg": "Passwords don't match"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


@app.route("/login: Bearer <access_token>", methods=["POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        username = data["email"]
        password = data["password"]
        user = User.query.get(data["email"])
    if username != user.email or password != user.password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)
