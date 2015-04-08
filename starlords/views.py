from starlords import app
from flask import Flask, render_template, url_for, g, request, session, redirect, abort, flash

from flask.ext.sqlalchemy import SQLAlchemy

app.config.from_object('config.TestConfig')
db = SQLAlchemy(app)
from models import *

########################################################
#                Root and information
########################################################

@app.route('/')
def indexpage():
    return render_template("index.html")

@app.route('/aboutus')
def aboutuspage():
    return render_template("aboutus.html") 






########################################################
#               Lists of categories
########################################################

#Lists all the families in our database
@app.route('/families')
def familiespage():
    query = family.query.all()
    return render_template("families.html", families = query)

#Lists all the constellations in our database
@app.route('/constellations')
def constellationspage():
    query = db.session.query(constellation, family).filter(constellation.fk_constellation_family == family.id).all()
    return render_template("constellations.html", constellations = query)

#Lists all the stars in our database
@app.route('/stars')
def starspage():
    query = db.session.query(star, constellation, family).filter(star.fk_constellation_star == constellation.id)\
                                                         .filter(constellation.fk_constellation_family == family.id).all()
    return render_template("stars.html", stars = query)

#Lists all the planets in our database
@app.route('/planets')
def planetspage():
    query = db.session.query(planet, star, constellation, family).filter(planet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
    print(query)
    return render_template("planets.html", planets = query)

#Lists all the moons in our database
@app.route('/moons')
def moonspage():
    query = db.session.query(moon, planet, star, constellation, family).filter(moon.fk_planet_moon == planet.id)\
                                                            .filter(planet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
    return render_template("moons.html", moons = query)

#Lists all the exoplanets in our database
@app.route('/exoplanets')
def exoplanetspage():
    query = db.session.query(exoplanet, star, constellation, family).filter(exoplanet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()

    return render_template("exoplanets.html", exoplanets = query)






########################################################
#               Dynamic page per object
########################################################

#renders an exoplanet page
@app.route('/exoplanets/<exoplanetVar>')
def exoplanetPage(exoplanetVar):
    return "Received request for exoplanet: " + exoplanetVar

#renders a family page
@app.route('/families/<familyVar>')
def familypage(familyVar):
    
    return render_template("bayer.html")

#renders a star page
@app.route('/stars/<starVar>')
def starPage(starVar):
    query = db.session.query(star, constellation, family).filter(star.name ==starVar).filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
    return render_template("star.html", stars = query)

#renders a planet page
@app.route('/planets/<planetVar>')
def planetPage(planetVar):
    query = db.session.query(planet, star, constellation, family).filter(planet.name == planetVar).filter(planet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).first()

    if(query != None):
        return render_template(
            "planet.html",
            planet = query,
            name = query[0].name,
            planet_photo = query[0].photo,
            distance_from_sun = query[0].distance_from_sun,
            orbital_period = query[0].orbital_period,
            volume = query[0].volume,
            mass = query[0].mass,
            density = query[0].density,
            surface_area = query[0].surface_area,
            semi_major_axis = query[0].semi_major_axis,
            gravity = query[0].gravity,
            length_of_day = query[0].length_of_day,
            surface_temperature = query[0].surface_temperature,
            moons = query[0].moons,
            planet_photo_link = query[0].photo_link,
            history = query[0].history,
            constellation_name = query[2].name,
            constellation_photo = query[2].photo,
            star_name = query[1].name,
            star_photo = query[1].photo
            )
    else:
        return "Invalid planet: " + planetVar

#renders a constellation page
@app.route('/constellations/<consVar>')
def constellationPage(consVar):
    return "Received request for constellation: " + consVar

#renders a moon page
@app.route('/moons/<moonVar>')
def moonPage(moonVar):
    return "Received request for moon: " + moonVar






"""    
@app.route('/home')
def homepage():
    return render_template("home.html")


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
