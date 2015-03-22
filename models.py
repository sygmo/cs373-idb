import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, LargeBinary, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from difficulty import db
 

class family(db.Model):
	__tablename__ = "family"
	id = db.Column(Integer, primary_key = True)
	name = db.Column(String(250), nullable = False)

class constellation(db.Model):
	__tablename__ = "constellation"
	id = db.Column(Integer, primary_key = True)
	name = db.Column(Text, nullable = False)
	area = db.Column(Float)
	stars_with_planets = db.Column(Integer)
	brightest_star = db.Column(Text)
	nearest_star = db.Column(Text)
	history = db.Column(Text)
	photo_link = db.Column(Text)
	photo = db.Column(LargeBinary)
	fk_constellation_family = db.Column(Integer, ForeignKey("family.id"))


class planet(db.Model):
	__tablename__ = "planet"
	id = db.Column(Integer, primary_key = True)
	name = db.Column(Text, nullable = False)
	radius = db.Column(Float)
	rings = db.Column(Integer)
	distance_from_sun = db.Column(Float)
	composition = db.Column(Text)
	is_dwarf = db.Column(Boolean)
	orbital_period = db.Column(Float)
	volume = db.Column(Float)
	mass = db.Column(Float)
	density = db.Column(Float)
	surface_area = db.Column(Float)
	gravity = db.Column(Float)
	length_of_day = db.Column(Float)
	length_of_year = db.Column(Float)
	surface_temperature = db.Column(Float)
	atmosphere = db.Column(Text)
	number_of_moons = db.Column(Integer)
	history = db.Column(Text)
	photo_link = db.Column(Text)
	photo = db.Column(LargeBinary)
	fk_star_planet = db.Column(Integer, ForeignKey("star.id"))

class star(db.Model):
	__tablename__ = "star"
	id = db.Column(Integer, primary_key = True)
	name = db.Column(Text, nullable = False)
	mass = db.Column(Float)
	radius = db.Column(Float)
	temperature = db.Column(Float)
	luminosity = db.Column(Float)
	surface_gravity = db.Column(Float)
	stellar_distance = db.Column(Float)
	stellar_classification = db.Column(Text)
	henry_draper_catalogue = db.Column(Integer)
	hipparcos_catalogue = db.Column(Integer)
	apparent_magnitude = db.Column(Float)
	absolute_magnitude = db.Column(Float)
	parallax = db.Column(Float)	
	photo_link = db.Column(Text)
	history = db.Column(Text)
	photo = db.Column(LargeBinary)
	fk_constellation_star = db.Column(Integer, ForeignKey("constellation.id"))

class moon(db.Model):
	__tablename__ = "moon"
	id = db.Column(Integer, primary_key = True)
	name = db.Column(Text, nullable = False)
	radius = db.Column(Float)
	volume = db.Column(Float)
	mass = db.Column(Float)
	distance_from_planet = db.Column(Float)
	orbital_period = db.Column(Float)
	surface_gravity = db.Column(Float)
	history = db.Column(Text)
	photo_link = db.Column(Text)
	photo = db.Column(LargeBinary)
	fk_planet_moon = db.Column(Integer, ForeignKey("planet.id"))
	









