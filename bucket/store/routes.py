from bucket import db
from bucket.models import Product
from .forms import CheckoutForm
from flask import render_template, redirect, url_for, flash
from flask_login import current_user
from . import bp

@bp.route('/products')
def products():
	pass