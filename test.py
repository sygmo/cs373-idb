from flask import Flask, render_template, url_for, g, request, session, redirect, abort, flash
import os
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models import family
from difficulty import db

engine = create_engine('postgresql://localhost/universe')

#Creates session
Session = sessionmaker(bind=engine)
session = Session()


res = session.query(family).all()
for x in res:
	print (x.id)