from bucket import db
from bucket.models import Product
from .forms import ProductForm
from flask import render_template, redirect, url_for, flash
from flask_login import current_user
from . import bp

@bp.route('/admin')
@bp.route('/admin/navigate')
def navigate():
	return render_template('admin/navigate.html')

@bp.route('/admin/product', methods=['GET', 'POST'])
def product():
	form = ProductForm()
	return render_template('admin/product.html', form=form)