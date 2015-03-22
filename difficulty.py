from flask import Flask, render_template, url_for, g, request, session, redirect, abort, flash
import os
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

#Creates the application object
app = Flask(__name__)

app.config.from_object('config.BaseConfig')

#creates the sqlalchemy object
db = SQLAlchemy(app)


@app.route("/")
def difficulty() :
    return "Hello World!"

if __name__ == "__main__" :

    app.run()