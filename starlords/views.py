from starlords import app
from flask import Flask, render_template, url_for, g, request, session, redirect, abort, flash

from flask.ext.sqlalchemy import SQLAlchemy

app.config.from_object('config.TestConfig')
db = SQLAlchemy(app)
from models import *

@app.route('/')
def indexpage():
    return render_template("index.html")

@app.route('/families')
def familiespage():
    query = family.query.all()
    return render_template("families.html", families = query)
  
@app.route('/constellations')
def constellationspage():
    return render_template("constellations.html")

@app.route('/stars')
def starspage():
    return render_template("stars.html")

@app.route('/planets')
def planetspage():
    query = db.session.query(planet, star, constellation, family).filter(planet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()




    return render_template("planets.html", planets = query)










@app.route('/moons')
def moonspage():
    return render_template("moons.html")
    
@app.route('/aboutus')
def aboutuspage():
    return render_template("aboutus.html")
    
@app.route('/exoplanets')
def exoplanetspage():
    return render_template("exoplanets.html")




@app.route('/families/<family>')
def familypage(family):
    return "Received request for faimily: " + family

@app.route('/home')
def homepage():
    return render_template("home.html")
"""    

@app.route('/bayer')
def bayerpage():
    return render_template("bayer.html")    


    
@app.route('/perseus')
def perseuspage():
    return render_template("perseus.html")

@app.route('/andromeda')
def andromedapage():
    return render_template("andromeda.html")
    
@app.route('/vulpecula')
def vulpeculapage():
    return render_template("vulpecula.html")
    
@app.route('/solarsystem')
def solarsystem_page():
    return render_template("solarsystem.html")

@app.route('/hd189733')
def hd189733page():
    return render_template("hd189733.html")
    
@app.route('/wasp-1')
def wasp1page():
    return render_template("wasp-1.html")
    
@app.route('/sun')
def solarsystempage():
    return render_template("sun.html")  

@app.route('/hd189733b')
def hd189733bpage():
    return render_template("hd189733b.html")
    
@app.route('/wasp-1b')
def wasp1bpage():
    return render_template("wasp-1b.html")
    
@app.route('/jupiter')
def jupiterpage():
    return render_template("jupiter.html")  
    
@app.route('/europa')
def europapage():
    return render_template("europa.html")
    
@app.route('/io')
def iopage():
    return render_template("io.html")
    
@app.route('/callistro')
def callistropage():
    return render_template("callistro.html")    

@app.route('/upsand')
def upsandpage():
    return render_template("upsand.html")

@app.route('/upsandb')
def upsandbpage():
    return render_template("upsandb.html")

@app.route('/mercury')
def mercury():
    return render_template("mercury.html")

@app.route('/venus')
def venus():
    return render_template("venus.html")
"""
