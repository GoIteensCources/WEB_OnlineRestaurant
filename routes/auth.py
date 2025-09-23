from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from models import User
from settings import Session

bp = Blueprint("auth", __name__)


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        hashed_password = generate_password_hash(password)  # type: ignore

        user = User(username=username, email=email, hash_password=hashed_password)
        with Session() as session:
            session.add(user)
            session.commit()

        flash("Registration successful")
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.get_by_username(username=username)  # type: ignore
        if user and check_password_hash(user.hash_password, password):  # type: ignore

            login_user(user)
            flash("Login successful")

            return redirect(url_for("index"))
        flash("Invalid username or password")

    return render_template("auth/login.html")


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout successful")
    return redirect(url_for("index"))
