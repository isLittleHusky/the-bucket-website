from bucket import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	category = db.Column(db.String(64))
	color = db.Column(db.String(64))
	stock = db.Column(db.Integer)
	selling_price = db.Column(db.Float)
	
	def __repr__(self):
		return f'Product {self.name}'

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(128), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return f'User {self.email}'

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
	return User.query.get(int(id))