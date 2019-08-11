from flask import Blueprint, render_template

bp = Blueprint('store', __name__)

@bp.route('/store')
def products():
	render_template('store/products.html')

@bp.route('/checkout')
def checkout():
	render_template('store/checkout.html')