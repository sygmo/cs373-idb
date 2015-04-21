from flask import Flask, render_template, url_for, g, request, session, redirect, abort, flash
from flask.ext.sqlalchemy import SQLAlchemy
from models import *
from flask.ext.restless import APIManager
from subprocess import Popen, PIPE
from sqlalchemy_searchable import parse_search_query
from sqlalchemy_searchable import search
app = Flask(__name__)

from getJson import getJson
import getJson as getCeleb

import json



app.config.from_object('config.LocalConfig')
db = SQLAlchemy(app)
########################################################
#                Root and information
########################################################

@app.route('/')
def indexpage():
    return render_template("index.html")


@app.route('/search')
def searchPage():
    searchVal = request.args.get("val")
    query = db.session.query(family)
    query = search(query, searchVal)

    


    if (query.first() != None):
        return "Got string: "  + query.first().name
    else:
        return "Result does not exist: " + searchVal  

@app.route('/aboutus')
def aboutuspage():
    return render_template("aboutus.html")

@app.route('/darksideapi')
def darksideapipage():
    obj = getJson("http://23.253.252.30/api/celebrity")
    li = []
    #return "Length is " + str(len(li))
    for x in obj:
        celebrity = getCeleb.getCelebrity(x['id'])
        li.append(celebrity)



    return render_template("darksideapi.html", data = li)

@app.route('/unittest_results')
def unittest_resultspage():
    process = Popen(['python', 'tests.py'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return render_template("unittest_results.html", results=stderr)




def unittests():
    app.config.from_object('config.LocalTestConfig')
    db = SQLAlchemy(app)

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
    query = db.session.query(exoplanet, star, constellation, family).filter(exoplanet.name == exoplanetVar).filter(exoplanet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).first()

    if(query != None):
        return render_template(
            "exoplanet.html",
            exoplanet = query,
            exoplanetId = query[0].id,
            name = query[0].name,
            discovered = query[0].discovered,
            orbital_period = query[0].orbital_period,
            semi_major_axis = query[0].semi_major_axis,
            discovery_method = query[0].discovery_method,
            star_name = query[1].name,
            constellation_name = query[2].name
            )
    else:
        return "Invalid exoplanet: " + exoplanetVar

#renders a family page
@app.route('/families/<familyVar>')
def familypage(familyVar):
    query = db.session.query(family).filter(family.name == familyVar).first()
    if(query != None):
        query_moons = db.session.query(moon, planet, star, constellation, family).filter(family.name == familyVar).filter(moon.fk_planet_moon == planet.id).filter(planet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
        query_planets = db.session.query(planet, star, constellation, family).filter(family.name == familyVar).filter(planet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
        query_stars = db.session.query(star, constellation, family).filter(family.name == familyVar).filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
        query_exoplanets = db.session.query(exoplanet, star, constellation, family).filter(family.name == familyVar).filter(exoplanet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
        query_constellations = db.session.query(constellation, family).filter(family.name == familyVar).filter(constellation.fk_constellation_family == family.id).all()
        return render_template(
            "family.html",
            family = query,
            name = query.name,
            description = query.description,
            all_moons = query_moons,
            all_planets = query_planets,
            all_stars = query_stars,
            all_exoplanets = query_exoplanets,
            all_constellations = query_constellations
            )
    else:
        return "Invalid family: " + familyVar

#renders a star page
@app.route('/stars/<starVar>')
def starPage(starVar):
    query = db.session.query(star, constellation, family).filter(star.name ==starVar).filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).first()
    if(query != None):
        query_moons = db.session.query(moon, planet, star, constellation, family).filter(star.name == starVar).filter(moon.fk_planet_moon == planet.id).filter(planet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
        query_planets = db.session.query(planet, star, constellation, family).filter(star.name == starVar).filter(planet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
        query_exoplanets = db.session.query(exoplanet, star, constellation, family).filter(star.name == starVar).filter(exoplanet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
        return render_template(
            "star.html",
            star = query,
            name = query[0].name,
            mass = query[0].mass,
            radius = query[0].radius,
            spectral_type = query[0].spectral_type,
            temperature = query[0].temperature,
            luminosity = query[0].luminosity,
            stellar_distance = query[0].stellar_distance,
            planetary_systems = query[0].planetary_systems,
            photo_link = query[0].photo_link,
            history = query[0].history,
            photo = query[0].photo,
            constellation_name = query[1].name,
            constellation_photo = query[1].photo,
            all_moons = query_moons,
            all_planets = query_planets,
            all_exoplanets = query_exoplanets
            )
    else:
        return "Invalid star: " + starVar

#renders a planet page
@app.route('/planets/<planetVar>')
def planetPage(planetVar):
    query = db.session.query(planet, star, constellation, family).filter(planet.name == planetVar).filter(planet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).first()

    if(query != None):
        query_moons = db.session.query(moon, planet, star, constellation, family).filter(planet.name == planetVar).filter(moon.fk_planet_moon == query[0].id).filter(planet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
        return render_template(
            "planet.html",
            planet = query,
            planetId = query[0].id,
            name = query[0].name,
            planet_photo = query[0].photo,
            distance_from_sun = query[0].distance_from_sun,
            orbital_period = query[0].orbital_period,
            volume = query[0].volume,
            mass = query[0].mass,
            radius = query[0].radius,
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
            star_photo = query[1].photo,
            all_moons = query_moons
            )
    else:
        return "Invalid planet: " + planetVar

#renders a constellation page
@app.route('/constellations/<consVar>')
def constellationPage(consVar):
    query = db.session.query(constellation, family).filter(constellation.name == consVar).filter(constellation.fk_constellation_family == family.id).first()
    if(query != None):
        query_moons = db.session.query(moon, planet, star, constellation, family).filter(constellation.name == consVar).filter(moon.fk_planet_moon == planet.id).filter(planet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
        query_planets = db.session.query(planet, star, constellation, family).filter(constellation.name == consVar).filter(planet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
        query_stars = db.session.query(star, constellation, family).filter(constellation.name == consVar).filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
        query_exoplanets = db.session.query(exoplanet, star, constellation, family).filter(constellation.name == consVar).filter(exoplanet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
        return render_template(
            "constellation.html",
            constellation = query,
            name = query[0].name,
            stars_with_planets = query[0].stars_with_planets,
            meaning = query[0].meaning,
            history = query[0].history,
            photo_link = query[0].photo_link,
            photo = query[0].photo,
            family_name = query[1].name,
            all_moons = query_moons,
            all_planets = query_planets,
            all_stars = query_stars,
            all_exoplanets = query_exoplanets
            )
    else:
        return "Invalid constellation: " + consVar

#renders a moon page
@app.route('/moons/<moonVar>')
def moonPage(moonVar):
    query = db.session.query(moon, planet, star, constellation, family).filter(moon.name == moonVar).filter(moon.fk_planet_moon == planet.id).filter(planet.fk_star_planet == star.id)\
                                                            .filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).first()
    if(query != None):
        return render_template(
            "moon.html",
            moon = query,
            name = query[0].name,
            moon_photo = query[0].photo,
            radius = query[0].radius,
            mass = query[0].mass,
            orbital_period = query[0].orbital_period,
            surface_gravity = query[0].surface_gravity,
            moon_photo_link = query[0].photo_link,
            history = query[0].history,
            constellation_name = query[3].name,
            constellation_photo = query[3].photo,
            star_name = query[2].name,
            star_photo = query[2].photo,
            planet_name = query[1].name,
            planet_photo = query[1].photo
            )
    else:
        return "Invalid planet: " + planetVar



if __name__ == "__main__":
    api_manager = APIManager(app, flask_sqlalchemy_db=db)
    api_manager.create_api(family, methods=['GET'])
    api_manager.create_api(constellation, methods=['GET'])
    api_manager.create_api(planet, methods=['GET'])
    api_manager.create_api(star, methods=['GET'])
    api_manager.create_api(moon, methods=['GET'])
    api_manager.create_api(exoplanet, methods=['GET'])
    app.run(host='0.0.0.0', port=8080)
