from flask import Blueprint, render_template

main = Blueprint(import_name=__name__, name='main', url_prefix='/', template_folder='templates')


@main.route('')
def index():
    return render_template('index.html')
