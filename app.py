from flask import Flask, request, render_template, redirect, session
from datetime import date
import subprocess
from functools import wraps
from flask import Response
from schedule import schedule
import settings

app = Flask(__name__)
schedule()

app.secret_key = settings.secret_key

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if request.form['passkey'] == settings.passkey:
            session['logged_in'] = True
            return redirect("/welcome/")
    else:
        session['logged_in'] = False
        return render_template("%s.html" % "index")

@app.route("/welcome/", methods=['GET'])
def welcome():
    if session['logged_in']:
        if 'logout' in request.args.keys():
            session.clear()
            return redirect("/")

        with open(settings.database, encoding='utf8') as f:
            stri = f.read()
        things = eval(stri)

        week = date.today().isocalendar()[1]
        return render_template("%s.html" % "welcome", week=week, things=things)
    else:
        return redirect("/")

@app.route("/edit/", methods=['GET', 'POST'])
def edit():
    if session['logged_in']:
        if request.method == "POST":
            return redirect("/change/?week=%s" % request.form['sel'])
        else:
            with open(settings.database, encoding='utf8') as f:
                stri = f.read()
            things = eval(stri)
            return render_template("%s.html" % "edit", things=things)
    else:
        return redirect("/")

@app.route("/change/", methods=['GET', 'POST'])
def change():
    if session['logged_in']:
        if request.method == 'POST':
            with open(settings.database, encoding='utf8') as f:
                stri = f.read()
            things = eval(stri)
            things[int(request.args['week'])] = request.form['name']

            print(things)
            with open(settings.database, 'w', encoding='utf8') as f:
                f.write(str(things))
            
            return redirect("/welcome/")
        else:
            with open(settings.database, encoding='utf8') as f:
                stri = f.read()
            things = eval(stri)
            return render_template("%s.html" % "change", week=int(request.args['week']), things=things)
    else:
        return redirect("/")