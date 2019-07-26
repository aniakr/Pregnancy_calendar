from flask_wtf import Form
from wtforms.fields.html5 import DateField
from wtforms import SubmitField

class LmpInputForm(Form):
    lmp=DateField('Date of the beginning of your last period', format='%Y-%m-%d')
    submit = SubmitField("Submit")
