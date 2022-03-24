from app import myobj
from flask import render_template, request


city_names = ['Paris','London', 'Rome', 'Tahiti']
name = 'Lisa'
myobj.config['SECRET_KEY'] = '1234'

@myobj.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        text = request.form['text']
        return text

    return render_template('home.html',
                           name = name,
                           city_names = city_names,
                           )
