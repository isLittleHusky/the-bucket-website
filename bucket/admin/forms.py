from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired


class StockForm(FlaskForm):
	name = SelectField('Name of Item', choices=[('hat', 'Bucket Hat'), ('pants', 'Jeans')], validators=[DataRequired()])
	operation = RadioField('Operation', choices=[('add', 'Add'), ('subtract', 'Subtract'), ('reset', 'Reset')], validators=[DataRequired()])
	number = IntegerField('Amount of Stock', validators=[DataRequired()])
	submit = SubmitField('Change Stock Value')

class ProductForm(FlaskForm):
	name = StringField('Name of Product', validators=[DataRequired()])
	stock = IntegerField('Amount of Stock', validators=[DataRequired()])
	category = SelectField('')