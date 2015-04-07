from starlords.views import db
from models import family, constellation, planet, star, moon, exoplanet

#creates the database
print("about to drop")
db.drop_all()
print("dropped")
print("about to create")
db.create_all()
print("created")


#NOTE:
#if you don't see all the data being displayed check your foreign keys


#insert sample data
#families
db.session.add(family(name = "Ursa Major", description="This family is composed of 10 constellations and is known for the Big Dipper."))
db.session.add(family(name = "Zodiac", description="This family is composed of 12 constellations that have zodiac signs."))
db.session.add(family(name = "Perseus", description="This family is composed of 9 constellations. Six of the constellations are named for figures in the Perseus myth."))
db.session.add(family(name = "Hercules", description="This family is composed of 19 constellations. It is the largest constellation family."))
db.session.add(family(name = "Orion", description="This family is composed of 5 constellations. It represents Orion and his dogs."))
db.session.add(family(name = "Heavenly Waters", description="The constellations in this family are associated with lakes, rivers, sea creatures, and ships."))
db.session.add(family(name = "Bayer", description="This family is composed of 11 constellations. The constellations are all based off of animals."))
db.session.add(family(name = "La Caille", description="This family is composed of 13 constellations. The constellations were introduced by Nicolas Louis de Lacaille"))
db.session.add(family(name = "Home", description="This is the family composed of our Sun and Solar System"))
db.session.commit()

#insert constellation
db.session.add(constellation(name = "Solar System", fk_constellation_family = 9))
db.session.add(constellation(name = "Andromeda", fk_constellation_family = 3))
db.session.commit()

#stars
db.session.add(star(name = "Sun", fk_constellation_star = 1))
db.session.add(star(name = "WASP-1b", fk_constellation_star = 2))
db.session.commit()
print("added")

#exoplanets
db.session.add(exoplanet(name = "WASP-1b", fk_star_planet = 2))

#planets
db.session.add(planet(name = "Mercury", distance_from_sun = 0.307, semi_major_axis = 0.387, orbital_period = 0.2408418001989376, radius = 2439.7, surface_area = 0.147, volume = 0.056, mass = 0.055, density = 5.427, gravity = 3.7, length_of_day = 58.646, surface_temperature = 340, moons = 0, history = "Mercury is named after the messenger to the Gods. Mercury has almost no atmosphere to retain heat. It is in the <a href=\"/home\">Home</a> family.", photo_link = "http://www.nasa.gov/mission_pages/messenger/multimedia/messenger_orbit_image20111129_1.html", photo = "images/mercury.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Venus", distance_from_sun = 0.718440, semi_major_axis = 0.723327, orbital_period = 0.6151870925724003, radius = 6051.8, surface_area = 0.902, volume = 0.866, mass = 0.815, density = 5.243, gravity = 8.87, length_of_day = -243.0185, surface_temperature = 737, moons = 0, history = "Venus is the second brightest natural object in the night sky - from the moon. It is in the <a href=\"/home\">Home</a> family.", photo_link = "http://commons.wikimedia.org/wiki/File:Venus_globe.jpg", photo = "images/venus.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Earth", distance_from_sun = 0.98329, semi_major_axis = 1, orbital_period = 1.0, radius = 6371.0, surface_area = 1, volume = 1, mass = 1, density = 5.514, gravity = 9.807, length_of_day = 0.99726968, surface_temperature = 288, moons = 1, history = "Earth is the planet where all of humanity resides. It is in the <a href=\"/home\">Home</a> family.", photo_link = "http://commons.wikimedia.org/wiki/File:The_Earth_seen_from_Apollo_17.jpg", photo = "images/earth.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Mars", distance_from_sun = 1.3814, semi_major_axis = 1.523679, orbital_period = 1.8808, radius = 3389.5, surface_area = 0.284, volume = 0.151, mass = 0.107, density = 3.9335, gravity = 3.711, length_of_day = 1.025957, surface_temperature = 210, moons = 0, history = "Mars, otherwise known as the red planet, is the second smallest planet in the solar system. It is in the <a href=\"/home\">Home</a> family.", photo_link = "http://commons.wikimedia.org/wiki/File:Mars_23_aug_2003_hubble.jpg", photo = "images/mars.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Jupiter", distance_from_sun = 4.950429, semi_major_axis = 5.204267, orbital_period = 11.8618, moons = 67, radius = 69911, surface_area = 121.9, volume = 1321.3, mass = 317.8, density = 1.326, gravity = 24.79, length_of_day = 9.925, surface_temperature = 165, history = "Jupiter is a gas giant. Jupiter lacks a well-defined solid surface. It is in the <a href=\"/home\">Home</a> family.", photo_link = "http://commons.wikimedia.org/wiki/File:Jupiter_New_Horizons.jpg", photo = "images/jupiter.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Saturn", distance_from_sun = 9.04807635, semi_major_axis = 9.5820172, orbital_period = 29.4571, moons = 62, radius = 58232, surface_area = 83.703, volume = 763.59, mass = 95.152, density = 0.687, gravity = 10.44, length_of_day = 10.55, surface_temperature = 134, history =  "Saturn is known for its many rings. It is in the <a href=\"/home\">Home</a> family.", photo_link = "http://commons.wikimedia.org/wiki/File:Saturn_Equinox_09212014.jpg", photo = "images/saturn.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Uranus", distance_from_sun = 18.283135, semi_major_axis = 19.189253, orbital_period = 84.016846, moons = 27, radius = 25362, surface_area = 15.91, volume = 63.086, mass = 14.536, density = 1.27, gravity = 8.69, length_of_day = 0.71833, surface_temperature = 76, history = "Uranus is different than the other planets because its axis of rotation is tilted.  It is in the <a href=\"/home\">Home</a> family.", photo_link = "http://commons.wikimedia.org/wiki/File:Uranus2.jpg", photo = "images/uranus.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Neptune", distance_from_sun = 29.809946, semi_major_axis = 30.070900, orbital_period = 164.8, moons = 14, radius = 24622, surface_area = 14.98, volume = 57.74, mass = 17.147, density = 1.638, gravity = 11.15, length_of_day = 0.6713, surface_temperature = 72, history = "Neptune is the farthest major planet from the sun in our solar system. It is in the <a href=\"/home\">Home</a> family.", photo_link = "http://commons.wikimedia.org/wiki/File:Neptune_Full.jpg", photo = "images/neptune.jpg", fk_star_planet = 1))

#moons
db.session.add(moon(name = "Io", fk_planet_moon = 5))
db.session.commit()





query = db.session.query(planet, star, constellation, family).filter(planet.fk_star_planet == star.id)\
															.filter(star.fk_constellation_star == constellation.id)\
															.filter(constellation.fk_constellation_family == family.id).all()
for x in query:
	print("planet: " + x[0].name + ", Star: " + x[1].name + ", constellation: " + x[2].name + ", family: " + x[3].name)

query1 = db.session.query(star, constellation, family).filter(star.fk_constellation_star == constellation.id)\
															.filter(constellation.fk_constellation_family == family.id).all()
for x in query1:
	print("Star: " + x[0].name + ", constellation: " + x[1].name + ", family: " + x[2].name)

query2 = db.session.query(constellation, family).filter(constellation.fk_constellation_family == family.id).all()

for x in query2:
	print("constellation: " + x[0].name + ", family: " + x[1].name)


print(db.session.query(star).filter_by(name = "Sun").first().name)





#commit changes
db.session.commit()