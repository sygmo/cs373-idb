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
	

