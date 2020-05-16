from flask import Flask, render_template, url_for, request
from forms import log_form
import os
import models as dbHandler
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method=='POST':
        username = request.form['username']
        movement = request.form['movement']
        weight = request.form['weight']
        repetitions = request.form['repetitions']
        rpe = request.form['rpe']
        dbHandler.insertLog(username,
                movement,
                weight,
                repetitions,
                rpe)
        form = log_form()
        return render_template('log.html', title='Log', form=form)
    else:
        form = log_form()
        return render_template('log.html', title='Log', form=form)
