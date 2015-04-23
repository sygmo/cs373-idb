from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy_searchable import search

import threading
from flask import Flask, render_template, url_for, g, request, session, redirect, abort, flash
from flask.ext.sqlalchemy import SQLAlchemy

#app = Flask(__name__)
#db = SQLAlchemy(app)
from models import *
from __init__ import unittests
unittests()



#for this tests to work you need to have a postgres database 
#set up with the name testdb, no username, no password

class tests(TestCase):

    #setup the database
    def setUp(self):
        db.configure_mappers()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    
    #Test that the table family is writable
    def test_write_family(self):

        query = family.query.all()
        startSize = len(query)

        db.session.add(family(name = "TESTWRITE", description="TEST"))
        db.session.commit()
        query = family.query.all()

        endSize = len(query)

        self.assertEqual(startSize + 1, endSize)    

    #Test that the table family is readable
    def test_read_family(self):

        db.session.add(family(name = "TESTREAD", description="TEST"))
        db.session.commit()

        query = family.query.all()
        found = False

        for x in query:
            if(x.name == "TESTREAD"):
                found = True

        assert(found)

    def test_read_family_attribute(self):

        db.session.add(family(name = "TESTATTR", description = "All the signs"))
        db.session.commit()

        query = db.session.query(family).filter(family.name == "TESTATTR").first()

        assert (query is not None)
        assert (query.description == "All the signs")
        


     
    #Test deletion of a row in family
    def test_delete_family_row(self):
        

        db.session.add(family(name = "delete"))
        db.session.commit()

        query = db.session.query(family).filter(family.name == "delete").first()

        assert(query != None)

        db.session.delete(query);
        db.session.commit()

        toRemove = db.session.query(family).filter(family.name == "delete").first()
        assert(toRemove == None)

       
    

    def test_write_constellation (self):

        query = db.session.query(constellation).all()
        startSize = len(query)
        #print(startSize)

        db.session.add(constellation(name = "TESTCONSTELLATION"))
        res = db.session.query(constellation).all()
        db.session.commit()

        query = db.session.query(constellation).all()
        endSize = len(query)

        self.assertEqual(startSize + 1, endSize)    

        #Test that the table constellation is readable
    def test_read_constellation(self):

        db.session.add(constellation(name = "Aries"))
        db.session.commit()

        query = db.session.query(constellation).all()
        found = False

        for x in query:
            if(x.name == "Aries"):
                found = True

        assert(found)

    def test_read_constellation_attribute(self):

        db.session.add(constellation(name = "TESTCATTR", stars_with_planets = 5))
        db.session.commit()

        query = db.session.query(constellation).filter(constellation.name == "TESTCATTR").first()

        assert (query is not None)
        assert (query.stars_with_planets == 5)
        
    
    #Test deletion of a row in constellation
    def test_delete_constellation_row(self):
        

        db.session.add(constellation(name = "delete"))
        db.session.commit()

        query = db.session.query(constellation).filter(constellation.name == "delete").first()

        assert(query != None)

        db.session.delete(query);
        db.session.commit()

        toRemove = db.session.query(constellation).filter(constellation.name == "delete").first()
        assert(toRemove == None)

        

   
    def test_write_star (self):

        query = db.session.query(star).all()
        startSize = len(query)
        #print(startSize)

        db.session.add(star(name = "Sol"))
        res = db.session.query(star).all()
        db.session.commit()

        query = db.session.query(star).all()
        endSize = len(query)

        self.assertEqual(startSize + 1, endSize)    

        #Test that the table constellation is readable
    def test_read_star(self):

        db.session.add(star(name = "And"))
        db.session.commit()

        query = db.session.query(star).all()
        found = False

        for x in query:
            if(x.name == "And"):
                found = True

        assert(found)

    def test_read_star_attribute(self):

        db.session.add(star(name = "Sun", spectral_type = "G2V"))
        db.session.commit()

        query = db.session.query(star).filter_by(name = "Sun").first()
       
        assert (query is not None)
        assert (query.spectral_type == "G2V")
        

    
    #Test deletion of a row in constellation
    def test_delete_star_row(self):
        db.session.add(star(name = "delete"))
        db.session.commit()

        query = db.session.query(star).filter(star.name == "delete").first()

        assert(query != None)

        db.session.delete(query);
        db.session.commit()

        toRemove = db.session.query(star).filter(star.name == "delete").first()
        assert(toRemove == None)
    
    def test_write_planet(self):

        query = db.session.query(planet).all()
        startSize = len(query)
        #print(startSize)

        db.session.add(planet(name = "Earth"))
        res = db.session.query(planet).all()
        db.session.commit()

        query = db.session.query(planet).all()
        endSize = len(query)

        self.assertEqual(startSize + 1, endSize)    

    #Test that the table family is readable
    def test_read_planet(self):

        db.session.add(planet(name = "Jupiter"))
        db.session.commit()

        query = db.session.query(planet).all()
        found = False

        for x in query:
            if(x.name == "Jupiter"):
                found = True

        assert(found)

    def test_read_planet_attribute(self):

        db.session.add(planet(name = "Mars", length_of_day = 345.0))
        db.session.commit()

        query = db.session.query(planet).filter(planet.name == "Mars").first()

        assert (query is not None)
        assert (query.length_of_day == 345.0)
        

    
    #Test deletion of a row in family
    def test_delete_planet_row(self):
        db.session.add(planet(name = "delete"))
        db.session.commit()

        query = db.session.query(planet).filter(planet.name == "delete").first()

        assert(query != None)

        db.session.delete(query);
        db.session.commit()

        toRemove = db.session.query(planet).filter(planet.name == "delete").first()
        assert(toRemove == None)
    
    def test_write_exoplanet(self):

        query = db.session.query(exoplanet).all()
        startSize = len(query)
        #print(startSize)

        db.session.add(exoplanet(name = "HD1461b"))
        res = db.session.query(exoplanet).all()
        db.session.commit()

        query = db.session.query(exoplanet).all()
        endSize = len(query)

        self.assertEqual(startSize + 1, endSize)    

    #Test that the table family is readable
    def test_read_exoplanet(self):

        db.session.add(exoplanet(name = "HD1461b"))
        db.session.commit()

        query = db.session.query(exoplanet).all()
        found = False

        for x in query:
            if(x.name == "HD1461b"):
                found = True

        assert(found)

    def test_read_exoplanet_attribute(self):

        db.session.add(exoplanet(name = "HD1461c", discovery_method = "radial velocity"))
        db.session.commit()

        query = db.session.query(exoplanet).filter_by(name = "HD1461c").first()

        assert (query is not None)
        assert (query.discovery_method == "radial velocity")
        

    
    #Test deletion of a row in family
    def test_delete_exoplanet_row(self):
        db.session.add(exoplanet(name = "delete"))
        db.session.commit()

        query = db.session.query(exoplanet).filter(exoplanet.name == "delete").first()

        assert(query != None)

        db.session.delete(query);
        db.session.commit()

        toRemove = db.session.query(exoplanet).filter(exoplanet.name == "delete").first()
        assert(toRemove == None)
    
    
    def test_write_moon(self):

        query = db.session.query(moon).all()
        startSize = len(query)
        #print(startSize)

        db.session.add(moon(name = "Moon"))
        res = db.session.query(moon).all()
        db.session.commit()

        query = db.session.query(moon).all()
        endSize = len(query)

        self.assertEqual(startSize + 1, endSize)    

    #Test that the table family is readable
    def test_read_moon(self):

        db.session.add(moon(name = "Titan"))
        db.session.commit()

        query = db.session.query(moon).all()
        found = False

        for x in query:
            if(x.name == "Titan"):
                found = True

        assert(found)

    def test_read_moon_attribute(self):

        db.session.add(moon(name = "Io", mass = 1.0))
        db.session.commit()

        query = db.session.query(moon).filter(moon.name == "Io").first()

        assert (query is not None)
        assert (query.mass == 1.0)
        

  
    #Test deletion of a row in family
    def test_delete_moon_row(self):
        db.session.add(moon(name = "delete"))
        db.session.commit()

        query = db.session.query(moon).filter(moon.name == "delete").first()

        assert(query != None)

        db.session.delete(query);
        db.session.commit()

        toRemove = db.session.query(moon).filter(moon.name == "delete").first()
        assert(toRemove == None)

    def test_search_family(self):
        db.session.add(family(name = "Zodiac", description="TEST"))
        db.session.commit()
        searchVal = "Zodiac"
        query_family = db.session.query(family)
        query = search(query_family, searchVal)
        assert(query != None)
        assert(query.count() > 0)
        for x in query.all():
            assert (x.name == "Zodiac")
            assert (x.description == "TEST")
            
    def test_search_constellation(self):
        db.session.add(constellation(name = "Puppis", meaning="TEST", history="TEST"))
        db.session.commit()
        searchVal = "Puppis"
        query_constellation = db.session.query(constellation)
        query = search(query_constellation, searchVal)
        assert(query != None)
        assert(query.count() > 0)
        for x in query.all():
            assert (x.name == "Puppis")
            assert (x.meaning == "TEST")
            assert (x.history == "TEST")
            
    def test_search_star(self):
        db.session.add(star(name = "Sun", spectral_type="TEST", history="TEST"))
        db.session.commit()
        searchVal = "Sun"
        query_star = db.session.query(star)
        query = search(query_star, searchVal)
        assert(query != None)
        assert(query.count() > 0)
        for x in query.all():
            assert (x.name == "Sun")
            assert (x.spectral_type == "TEST")
            assert (x.history == "TEST")
            
    def test_search_exoplanet(self):
        db.session.add(exoplanet(name = "WASP-1b", discovered="TEST", discovery_method="TEST", history="TEST"))
        db.session.commit()
        searchVal = "WASP-1b"
        query_exoplanet = db.session.query(exoplanet)
        query = search(query_exoplanet, searchVal)
        assert(query != None)
        assert(query.count() > 0)
        for x in query.all():
            assert (x.name == "WASP-1b")
            assert (x.discovered == "TEST")
            assert (x.discovery_method == "TEST")
            assert (x.history == "TEST")
            
    def test_search_planet(self):
        db.session.add(planet(name = "Earth", history="TEST"))
        db.session.commit()
        searchVal = "Earth"
        query_planet = db.session.query(planet)
        query = search(query_planet, searchVal)
        assert(query != None)
        assert(query.count() > 0)
        for x in query.all():
            assert (x.name == "Earth")
            assert (x.history == "TEST")
            
    def test_search_moon(self):
        db.session.add(moon(name = "Moon", history="TEST"))
        db.session.commit()
        searchVal = "Moon"
        query_moon = db.session.query(moon)
        query = search(query_moon, searchVal)
        assert(query != None)
        assert(query.count() > 0)
        for x in query.all():
            assert (x.name == "Moon")
            assert (x.history == "TEST")
    
if __name__ == "__main__":
    main()
