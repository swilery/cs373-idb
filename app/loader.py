# ------------------
# Init application
# ------------------

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app_instance = Flask(__name__)
app_instance.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app_instance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app_instance.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Xx99582774@162.243.14.196/postgres'
db = SQLAlchemy(app_instance)

#import app