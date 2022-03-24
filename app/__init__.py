from flask import Flask

myObject = Flask(__name__)

from app import routes
