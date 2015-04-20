from sqlalchemy_searchable import parse_search_query
from sqlalchemy_searchable import search
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

from __init__ import db
from sqlalchemy import or_

searchVal = "or earth sun"

if(" or " in searchVal):
	searchVal = searchVal.replace(" or ", " ")

query_family = db.session.query(family)
query_constellation = db.session.query(constellation)
query_star = db.session.query(star)
query_moon = db.session.query(moon)
query_planet = db.session.query(planet)
query_exoplanet = db.session.query(exoplanet)

print("and results")
query = search(query_family, searchVal)

for x in query.all():
    print (x.name)

query = search(query_constellation, searchVal)

for x in query.all():
    print (x.name)

query = search(query_star, searchVal)

for x in query.all():
    print (x.name)
	
query = search(query_exoplanet, searchVal)

for x in query.all():
    print (x.name)
	
query = search(query_planet, searchVal)

for x in query.all():
    print (x.name)
	
query = search(query_moon, searchVal)

for x in query.all():
    print (x.name)
	

print("or results")
or_results = searchVal.split(' ')
searchVal = or_results[0]
for i in range (1, len(or_results)):
	searchVal = searchVal + " or " + or_results[i]
	
query = search(query_planet, searchVal)

query = search(query_family, searchVal)

for x in query.all():
    print (x.name)

query = search(query_constellation, searchVal)

for x in query.all():
    print (x.name)

query = search(query_star, searchVal)

for x in query.all():
    print (x.name)
	
query = search(query_exoplanet, searchVal)

for x in query.all():
    print (x.name)
	
query = search(query_planet, searchVal)

for x in query.all():
    print (x.name)
	
query = search(query_moon, searchVal)

for x in query.all():
    print (x.name)