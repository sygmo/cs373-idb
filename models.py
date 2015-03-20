import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class family(Base):
	__tablename__ = "family"
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)

class constellation(Base):
	__tablename__ = "constellation"
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	history = Column(String(500))
	photo_link = Column(String(250))
	area = Column(String(250))
	stars_with_planets = Column(Integer)
	brightest_star = Column(String(250))
	nearest_star = Column(String(250))
	fk_constellation_family = Column(Integer, ForeignKey("family.id"))

class planet(Base):
	__tablename__ = "planet"
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	radius = Column(Number)
	rings = Column(Integer)
	distance_from_sun = Column(Number)
	composition = Column(String(250))
	is_dwarf = Column(Boolean)
	days_of_revolution = Column(String(250))
	volume = Column(Number)
	mass = Column(Number)
	density = Column(Number)
	surface_area = Column(Number)
	gravity = Column(Number)
	length_of_day = Column(Number)
	length_of_year = Column(Number)
	surface_temperature = Column(Number)
	atmosphere = Column(String(250))
	number_of_moons = Column(Integer)
	history = Column(String(500))
	photo_link = Column(String(250))
	fk_star_planet = Column(Integer, ForeignKey("star.id"))

class star(Base):
	__tablename__ = "star"
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	mass = Column(Number)
	radius = Column(Number)
	age = Column(Number)
	temperature = Column(Number)
	stellar_distance = Column(Number)
	stellar_classification = Column(String(250))
	henry_draper_catalogue = Column(Integer)
	hipparcos_catalogue = Column(Integer)
	right_ascension = Column(String(250))
	declination = Column(String(250))
	apparent_magnitude = Column(Number)
	absolute_magnitude = Column(Number)
	luminosity = Column(String(250))
	photo_link = Column(String(250))
	history = Column(String(500))
	fk_constellation_star = Column(Integer, ForeignKey("constellation.id"))

class moon(Base):
	__tablename__ = "moon"
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	radius = Column(Number)
	volume = Column(Number)
	mass = Column(Number)
	distance_from_planet = Column(Number)
	orbital_period = Column(Number)
	surface_gravity = Column(Number)
	history = Column(String(500))
	photo_link = Column(String(250))
	fk_planet_moon = Column(Integer, ForeignKey("planet.id"))
	









