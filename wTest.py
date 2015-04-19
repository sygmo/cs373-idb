from sqlalchemy_searchable import parse_search_query
from sqlalchemy_searchable import search
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

from __init__ import db


query = db.session.query(family)
query = search(query, "zodiac")

print(query.first().name)