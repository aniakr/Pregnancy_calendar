from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import StringField
from wtforms.validators import DataRequired


class LmpInputForm(FlaskForm):
    lmp=DateField('lmp_input',format='%Y-%m-%d')

class BasicInput(FlaskForm):
    basic=StringField('basic_input',validators=[DataRequired()])