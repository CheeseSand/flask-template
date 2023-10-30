from flask import Blueprint, render_template

bp = Blueprint("errors", __name__)

@bp.app_errorhandler(404)
def handle_404():
    return render_template('errors/404.html')

@bp.app_errorhandler(500)
def handle_500():
    return render_template('errors/500.html')