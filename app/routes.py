from app import myobj
from flask import render_template, request,flash


city_names = ['Paris','London', 'Rome', 'Tahiti']
name = 'Lisa'
myobj.config['SECRET_KEY'] = '888888889'

@myobj.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        message1 = request.form['text']
        flash(message1)

    return render_template('home.html',
                           name = name,
                           city_names = city_names,
                           )
