from flask import Flask, render_template, request,url_for, flash
from Pregnancy_calendar.calculator.pregnancy_calendar import PregnancyCalendar
from Pregnancy_calendar.flask_pregnancy_app.forms import LmpInputForm, GivenWeekCalculation, GivenDateCalculation

app=Flask(__name__)
app.config['SECRET_KEY']='Secret'

news=({"author":"AniaK",
       "title":"How to use app",
       "date_posted":"July 20, 2019",
       "content":"not yet ready:P"
        },
      {"author":"AniaK",
       "title":"What else can be found",
       "date_posted":"July 21, 2019",
       "content":"neither ready"
    })

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", news=news)

@app.route("/about")
def about():
    return render_template("about.html",title="About the calendar")

@app.route("/calendar",methods=['GET','POST'])
def calendar():
    form=LmpInputForm()
    form2=GivenWeekCalculation()
    form3=GivenDateCalculation()
    if request.method=='POST':
        if form.validate_on_submit():
            my_pregnancy = PregnancyCalendar(form.lmp.data.strftime('%m/%d/%y'))
            flash(f'You are in {my_pregnancy.current_week()[0]} week and {my_pregnancy.current_week()[1]} day')
            flash(f'Your edd is {my_pregnancy.edd_calculator()}')
        if form2.validate_on_submit():
            my_pregnancy = PregnancyCalendar(form.lmp.data.strftime('%m/%d/%y'))
            flash(f'Week {form2.required_week.data} will start on '
                  f'{my_pregnancy.given_week_calculator(form2.required_week.data)}')
        if form3.validate_on_submit():
            my_pregnancy = PregnancyCalendar(form.lmp.data.strftime('%m/%d/%y'))
            flash(f'On {form3.required_date.data} you will be in '
                f'{my_pregnancy.week_at_given_date(form3.required_date.data.strftime("%m/%d/%y"))[0]} week and '
                f'{my_pregnancy.week_at_given_date(form3.required_date.data.strftime("%m/%d/%y"))[1]} day')
    return render_template("calendar.html", title='Calendar',form=form,form2=form2,form3=form3)

if __name__=="__main__":
    app.run(debug=True)