from flask import Flask, render_template

app=Flask(__name__)

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

if __name__=="__main__":
    app.run(debug=True)