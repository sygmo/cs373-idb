from sqlalchemy_searchable import parse_search_query
from sqlalchemy_searchable import search
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

from __init__ import db
from sqlalchemy import or_

searchVal = "Zodiac"
query = db.session.query(family)
#query = search(query, searchVal)

#query = db.session.query(family).filter(or_(family.name.like(searchVal), family.description.like(searchVal)))
query = search(query, searchVal, vector=family.search_vector)
'''
combined_search_vector = family.search_vector | constellation.search_vector

articles = (
    db.session.query(family, constellation)
    .filter(constellation.fk_constellation_family == family.id)
    .filter(
        combined_search_vector.match(
            parse_search_query(searchVal)
        )
    )
)
'''

for x in query.all():
    print (x.name)
    #print (x[1].name)

"""
for x in articles.all():
    print (x[0].name)
    print (x[1].name)

    #print (x[1].meaning)
    print()
"""