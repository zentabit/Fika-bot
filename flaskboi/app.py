from flask import Flask, request, render_template, redirect, session
from datetime import date

app = Flask(__name__)

from functools import wraps
from flask import Response

app.secret_key = "uniqueandsecret"


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if request.form['passkey'] == "123456":
            session['logged_in'] = True
            return redirect("/welcome/")
    else:
        return render_template("%s.html" % "index")

@app.route("/welcome/", methods=['GET'])
def welcome():
    if session['logged_in']:
        with open('../data.txt', encoding='utf8') as f:
            stri = f.read()
        things = eval(stri)

        week = date.today().isocalendar()[1]
        return render_template("%s.html" % "welcome", week=week, things=things)
    else:
        return redirect("/")

