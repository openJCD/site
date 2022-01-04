from wtforms import BooleanField, SubmitField
from flask_wtf import FlaskForm
class FilterForm(FlaskForm) :
    red_tag = BooleanField('Red')
    submit = SubmitField('Submit')