from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

import threading
from flask import Flask, render_template, url_for, g, request, session, redirect, abort, flash
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object('config.TestConfig')
from models import *


#for this tests to work you need to have a postgres database 
#set up with the name testdb, no username, no password

class tests(TestCase):

    #setup the database
    def setUp(self):
       

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

        toRemove = db.session.query(constellation).filter(constellation.name == "delete").first()

        assert(toRemove != None)

        session.delete(toRemove);
        session.commit()

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
        print("***********************", query.spectral_type)
        assert (query is not None)
        assert (query.spectral_type == "G2V")
        

    """
    #Test deletion of a row in constellation
    def test_delete_star_row(self):
        self.lock.acquire()
        engine = create_engine('sqlite:///testdb.db')
        Session = sessionmaker(bind = engine)
        session = Session()

        db.session.add(star(name = "delete"))
        db.session.commit()

        toRemove = session.query(star).filter_by(name = "delete").first()

        assert(toRemove != None)

        session.delete(toRemove);
        session.commit()

        toRemove = session.query(star).filter_by(name = "delete").first()

        assert(toRemove == None)

        self.lock.release()
    """
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
        

    """    
    #Test deletion of a row in family
    def test_delete_planet_row(self):
        self.lock.acquire()
        engine = create_engine('sqlite:///testdb.db')
        Session = sessionmaker(bind = engine)
        session = Session()

        db.session.add(planet(name = "delete"))
        db.session.commit()

        toRemove = session.query(planet).filter_by(name = "delete").first()

        assert(toRemove != None)

        session.delete(toRemove);
        session.commit()

        toRemove = session.query(planet).filter_by(name = "delete").first()

        assert(toRemove == None)

        self.lock.release()
    """
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
        

    """    
    #Test deletion of a row in family
    def test_delete_exoplanet_row(self):
        self.lock.acquire()
        engine = create_engine('sqlite:///testdb.db')
        Session = sessionmaker(bind = engine)
        session = Session()

        db.session.add(exoplanet(name = "delete"))
        db.session.commit()

        toRemove = session.query(exoplanet).filter_by(name = "delete").first()

        assert(toRemove != None)

        session.delete(toRemove);
        session.commit()

        toRemove = session.query(exoplanet).filter_by(name = "delete").first()

        assert(toRemove == None)

        self.lock.release()
    """
    
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
        

"""    
    #Test deletion of a row in family
    def test_delete_moon_row(self):
        self.lock.acquire()
        engine = create_engine('sqlite:///testdb.db')
        Session = sessionmaker(bind = engine)
        session = Session()

        db.session.add(moon(name = "delete"))
        db.session.commit()

        toRemove = session.query(moon).filter_by(name = "delete").first()

        assert(toRemove != None)

        session.delete(toRemove);
        session.commit()

        toRemove = session.query(moon).filter_by(name = "delete").first()

        assert(toRemove == None)

        self.lock.release()
"""
if __name__ == "__main__":
    main()
