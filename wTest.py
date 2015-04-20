from sqlalchemy_searchable import parse_search_query
from sqlalchemy_searchable import search
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

from __init__ import db
from sqlalchemy import or_

searchVal = "family"

query_family = db.session.query(family)
query_constellation = db.session.query(constellation)
query_star = db.session.query(star)
query_moon = db.session.query(moon)
query_planet = db.session.query(planet)
query_exoplanet = db.session.query(exoplanet)

#query = db.session.query(family).filter(or_(family.name.like(searchVal), family.description.like(searchVal)))
#query = search(query, searchVal, vector=family.search_vector)

combined_search_vector = family.search_vector | constellation.search_vector
"""
query = (
    db.session.query(family, constellation).filter(constellation.fk_constellation_family == family.id)
)
"""
query = search(query_family, searchVal)

for x in query.all():
    print (x.name)

query = search(query_constellation, searchVal)

for x in query.all():
    print (x.name)
"""
for x in articles.all():
    print (x[0].name)
    print (x[1].name)

    #print (x[1].meaning)
    print()
"""