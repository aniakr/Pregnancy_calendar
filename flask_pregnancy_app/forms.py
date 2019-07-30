from flask_wtf import Form
from wtforms.fields.html5 import DateField
from wtforms import SubmitField, IntegerField,validators
from wtforms.validators import DataRequired

class LmpInputForm(Form):
    lmp=DateField('Date of the beginning of your last period', format='%Y-%m-%d',validators=[DataRequired()])
    calculations = SubmitField("Check your current week and edd")

class GivenWeekCalculation(Form):
    required_week=IntegerField('Week that interests you',[validators.number_range(min=1,max=40)])
    calculations = SubmitField("When that week will come")

class GivenDateCalculation(Form):
    required_date=DateField('Enter the date you would like to check', format='%Y-%m-%d')
    calculations = SubmitField("Which week will be at that date")