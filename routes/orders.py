
from flask import render_template, request, redirect, url_for, flash
from models import Orders, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required
from settings import Session
from flask import Blueprint


bp = Blueprint('/orders', __name__)




@bp.route("/my_orders")
@login_required
def my_orders():
    with Session() as session:
        user = session.merge(current_user)
        orders = user.orders
        print(orders)

    return redirect(url_for("menu.menu_view"))