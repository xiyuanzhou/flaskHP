from app import myObject
from flask import render_template, request


city_names = ['Paris','London', 'Rome', 'Tahiti']
name = 'Lisa'

@myObject.route('/',methods = ['POST','GET'])
def home():
    return render_template('home.html',
                           name = name,
                           city_names = city_names,
                           )
