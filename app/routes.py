from app import myobj
from flask import render_template, request


city_names = ['Paris','London', 'Rome', 'Tahiti']
name = 'Lisa'

@myobj.route('/')
def home():
    return render_template('home.html',
                           name = name,
                           city_names = city_names,
                           )

@myobj.route('/', methods=['POST'])
def home_post():
    text = request.form['text']

    return text
