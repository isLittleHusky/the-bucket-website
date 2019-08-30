from bucket import db
from bucket.models import User
from .forms import LoginForm, RegisterForm
from flask import render_template, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user
from . import bp


@bp.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('invalid username or password')
			return redirect(url_for('auth.login'))
		login_user(user)
		return redirect(url_for('main.home'))
	return render_template('auth/login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('congratulations you are now a registered user!')
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)

@bp.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.home'))