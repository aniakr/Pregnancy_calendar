from flask import Flask, render_template, request,url_for
from Pregnancy_calendar.flask_pregnancy_app.forms import LmpInputForm

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
    if request.method=='POST':
        if form.validate_on_submit():
            return "Success"
    return render_template("calendar.html", title='Calendar',form=form)

if __name__=="__main__":
    app.run(debug=True)