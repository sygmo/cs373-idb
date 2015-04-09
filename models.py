import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, LargeBinary, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from __init__ import db

class family(db.Model):
    __tablename__ = "family"
    id = db.Column(Integer, primary_key = True)
    name = db.Column(Text, nullable = False)
    description = db.Column(Text)

class constellation(db.Model):
    __tablename__ = "constellation"
    id = db.Column(Integer, primary_key = True)
    name = db.Column(Text, nullable = False)
    stars_with_planets = db.Column(Integer)
    meaning = db.Column(Text)
    history = db.Column(Text)
    photo_link = db.Column(Text)
    photo = db.Column(Text)
    fk_constellation_family = db.Column(Integer, ForeignKey("family.id"))

class planet(db.Model):
    __tablename__ = "planet"
    id = db.Column(Integer, primary_key = True)
    name = db.Column(Text, nullable = False)
    distance_from_sun = db.Column(Float)
    orbital_period = db.Column(Float)
    volume = db.Column(Float)
    mass = db.Column(Float)
    density = db.Column(Float)
    radius = db.Column(Float)
    surface_area = db.Column(Float)
    semi_major_axis = db.Column(Float)
    gravity = db.Column(Float)
    length_of_day = db.Column(Float)
    surface_temperature = db.Column(Float)
    moons = db.Column(Integer)
    history = db.Column(Text)
    photo_link = db.Column(Text)
    photo = db.Column(Text)
    fk_star_planet = db.Column(Integer, ForeignKey("star.id"))

class star(db.Model):
    __tablename__ = "star"
    id = db.Column(Integer, primary_key = True)
    name = db.Column(Text, nullable = False)
    mass = db.Column(Float)
    radius = db.Column(Float)
    spectral_type = db.Column(Text)
    temperature = db.Column(Float)
    luminosity = db.Column(Float)
    stellar_distance = db.Column(Float)
    planetary_systems = db.Column(Integer)  
    photo_link = db.Column(Text)
    history = db.Column(Text)
    photo = db.Column(Text)
    fk_constellation_star = db.Column(Integer, ForeignKey("constellation.id"))

class moon(db.Model):
    __tablename__ = "moon"
    id = db.Column(Integer, primary_key = True)
    name = db.Column(Text, nullable = False)
    radius = db.Column(Float)
    mass = db.Column(Float)
    orbital_period = db.Column(Float)
    surface_gravity = db.Column(Float)
    history = db.Column(Text)
    photo_link = db.Column(Text)
    photo = db.Column(Text)
    fk_planet_moon = db.Column(Integer, ForeignKey("planet.id"))

class exoplanet(db.Model):
    __tablename__ = "ExoPlanet"
    id = db.Column(Integer, primary_key = True)
    name = db.Column(Text, nullable = False)
    discovered = db.Column(Text)
    orbital_period = db.Column(Float)
    semi_major_axis = db.Column(Float)
    discovery_method = db.Column(Text)
    history = db.Column(Text)
    photo_link = db.Column(Text)
    photo = db.Column(Text)
    fk_star_planet = db.Column(Integer, ForeignKey("star.id"))

    


