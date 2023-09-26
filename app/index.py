from flask import Blueprint, render_template, request

bp = Blueprint("index", __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    user_input = None

    if request.method == 'POST':
        user_input = request.form.get('user_input')

    return render_template('index.html', user_input=user_input)
