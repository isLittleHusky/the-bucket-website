from flask import Blueprint, render_template, url_for

bp = Blueprint('main', __name__)

@bp.route('/home')
@bp.route('/index')
@bp.route('/')
def home():
	return render_template('main/home.html')

@bp.route('/contact')
def contact():
	return render_template('main/contact.html')