from flask import Flask, render_template, url_for, g, request, session, redirect, abort, flash
from flask.ext.sqlalchemy import SQLAlchemy
from models import *

import os, os.path
from whoosh import index

ix = index.create_in("whoosh_index", family)

app = Flask(__name__)

app.config.from_object('config.LocalConfig')
db = SQLAlchemy(app)

if __name__ == "__main__":
	print("Testing Whoosh!")
	result = family.query.whoosh_search("home").all()

	for x in result:
		print(x.name)
	#print(result)


