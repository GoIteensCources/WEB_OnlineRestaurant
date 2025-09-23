from flask import Blueprint, render_template

bp = Blueprint("error", __name__)


@bp.errorhandler(403)
def forbidden_error(error):
    return render_template("errors/403.html")
