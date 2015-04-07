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
db.session.add(constellation(name = "Solar System", stars_with_planets = 1, meaning = "System of the Sun", history = "It's where we've lived all our lives.", photo_link = "http://solarsystem.nasa.gov/multimedia/display.cfm?Category=Planets&IM_ID=10164", photo = "images/solarsystem.jpg", fk_constellation_family = 9))
db.session.add(constellation(name = "Andromeda", stars_with_planets = 12, meaning = "Andromeda, the Chained Woman", history = "Andromeda is one of the original constellations listed by Ptolemy and still remains a constellation as one of the 88 modern constellations.", photo_link = "http://commons.wikimedia.org/wiki/File:AndromedaCC.jpg", photo = "images/andromeda.jpg", fk_constellation_family = 3))
db.session.commit()

#stars
db.session.add(star(name = "Sun", mass = 1, radius = 1, spectral_type = "G27", temperature = 5778, luminosity = 1, stellar_distance = 0.0000158, fk_constellation_star = 1, history = "The Sun is the center of our Solar System.", photo_link = "http://commons.wikimedia.org/wiki/File:The_Sun_in_extreme_ultraviolet.jpg", photo = "images/sun.jpg"))
db.session.add(star(name = "WASP-1", mass = 1.24, radius = 1.382, spectral_type = "F7V", temperature = 6200, luminosity = 2.4, stellar_distance = 1239, planentary_systems = 1, fk_constellation_star = 2, history = "WASP-1 is a metal-rich magnitude 12 star.", photo_link = "http://upload.wikimedia.org/wikipedia/commons/e/ed/WASP-1.jpg", photo = "images/wasp-1.jpg"))
db.session.commit()
print("added")

#exoplanets
db.session.add(exoplanet(name = "WASP-1b", discovered = "2006", orbital_period = 2.5199464, semi_major_axis = 0.0382, discovery_method = "Discovery method Transit", fk_star_planet = 2, history = "In recognition of the regional support given to the project on La Palma, the discoverers gave the planet the alternative designation Garafia-1.", photo_link = "http://upload.wikimedia.org/wikipedia/commons/thumb/3/36/WASP-1b.jpg/300px-WASP-1b.jpg", photo = "images/wasp-1b.jpg"))


#planets
db.session.add(planet(name = "Mercury", distance_from_sun = 0.307, semi_major_axis = 0.387, orbital_period = 0.2408418001989376, radius = 2439.7, surface_area = 0.147, volume = 0.056, mass = 0.055, density = 5.427, gravity = 3.7, length_of_day = 58.646, surface_temperature = 340, moons = 0, history = "Mercury is named after the messenger to the Gods. Mercury has almost no atmosphere to retain heat.", photo_link = "http://www.nasa.gov/mission_pages/messenger/multimedia/messenger_orbit_image20111129_1.html", photo = "images/mercury.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Venus", distance_from_sun = 0.718440, semi_major_axis = 0.723327, orbital_period = 0.6151870925724003, radius = 6051.8, surface_area = 0.902, volume = 0.866, mass = 0.815, density = 5.243, gravity = 8.87, length_of_day = -243.0185, surface_temperature = 737, moons = 0, history = "Venus is the second brightest natural object in the night sky - from the moon.", photo_link = "http://commons.wikimedia.org/wiki/File:Venus_globe.jpg", photo = "images/venus.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Earth", distance_from_sun = 0.98329, semi_major_axis = 1, orbital_period = 1.0, radius = 6371.0, surface_area = 1, volume = 1, mass = 1, density = 5.514, gravity = 9.807, length_of_day = 0.99726968, surface_temperature = 288, moons = 1, history = "Earth is the planet where all of humanity resides.", photo_link = "http://commons.wikimedia.org/wiki/File:The_Earth_seen_from_Apollo_17.jpg", photo = "images/earth.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Mars", distance_from_sun = 1.3814, semi_major_axis = 1.523679, orbital_period = 1.8808, radius = 3389.5, surface_area = 0.284, volume = 0.151, mass = 0.107, density = 3.9335, gravity = 3.711, length_of_day = 1.025957, surface_temperature = 210, moons = 2, history = "Mars, otherwise known as the red planet, is the second smallest planet in the solar system.", photo_link = "http://commons.wikimedia.org/wiki/File:Mars_23_aug_2003_hubble.jpg", photo = "images/mars.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Jupiter", distance_from_sun = 4.950429, semi_major_axis = 5.204267, orbital_period = 11.8618, moons = 67, radius = 69911, surface_area = 121.9, volume = 1321.3, mass = 317.8, density = 1.326, gravity = 24.79, length_of_day = 9.925, surface_temperature = 165, history = "Jupiter is a gas giant and lacks a well-defined solid surface.", photo_link = "http://commons.wikimedia.org/wiki/File:Jupiter_New_Horizons.jpg", photo = "images/jupiter.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Saturn", distance_from_sun = 9.04807635, semi_major_axis = 9.5820172, orbital_period = 29.4571, moons = 62, radius = 58232, surface_area = 83.703, volume = 763.59, mass = 95.152, density = 0.687, gravity = 10.44, length_of_day = 10.55, surface_temperature = 134, history =  "Saturn is known for its many rings.", photo_link = "http://commons.wikimedia.org/wiki/File:Saturn_Equinox_09212014.jpg", photo = "images/saturn.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Uranus", distance_from_sun = 18.283135, semi_major_axis = 19.189253, orbital_period = 84.016846, moons = 27, radius = 25362, surface_area = 15.91, volume = 63.086, mass = 14.536, density = 1.27, gravity = 8.69, length_of_day = 0.71833, surface_temperature = 76, history = "Uranus is different than the other planets because its axis of rotation is tilted.", photo_link = "http://commons.wikimedia.org/wiki/File:Uranus2.jpg", photo = "images/uranus.jpg", fk_star_planet = 1))
db.session.add(planet(name = "Neptune", distance_from_sun = 29.809946, semi_major_axis = 30.070900, orbital_period = 164.8, moons = 14, radius = 24622, surface_area = 14.98, volume = 57.74, mass = 17.147, density = 1.638, gravity = 11.15, length_of_day = 0.6713, surface_temperature = 72, history = "Neptune is the farthest major planet from the sun in our solar system.", photo_link = "http://commons.wikimedia.org/wiki/File:Neptune_Full.jpg", photo = "images/neptune.jpg", fk_star_planet = 1))
db.session.commit()

#moons
db.session.add(moon(name = "Moon", radius = 0.273, mass = 0.012300, orbital_period = 27.321582, surface_gravity = 1.622, history = "The Moon is Earth's only natural satellite.", photo_link = "http://commons.wikimedia.org/wiki/File:FullMoon2010.jpg", photo = "images/moon.jpg", fk_planet_moon = 3))
db.session.add(moon(name = "Phobos", radius = 0.00176941, mass = 0.00000000178477, orbital_period = 0.31891023, surface_gravity = 0.0057, history = "Phobos is the largest satellite that orbits Mars. It was discovered in 1877.", photo_link = "http://www.nasa.gov/mission_pages/MRO/multimedia/pia10368.html", photo = "images/phobos.jpg", fk_planet_moon = 4))
db.session.add(moon(name = "Io", radius = 0.286, mass = 0.015, orbital_period = 16.6890184, surface_gravity = 1.769137786, history = "With over 400 active volcanoes, Io is the most geologically active object in the Solar System.", photo_link = "http://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Io_highest_resolution_true_color.jpg/520px-Io_highest_resolution_true_color.jpg", photo = "images/io.jpg", fk_planet_moon = 5))
db.session.add(moon(name = "Callisto",radius = 0.378, mass = 0.018, orbital_period = 16.6890184, surface_gravity = 1.235, history = "It is the third-largest moon in the Solar System.", photo_link = "http://upload.wikimedia.org/wikipedia/commons/e/e9/Callisto.jpg", photo = "images/callisto.jpg", fk_planet_moon = 5))
db.session.add(moon(name = "Europa", radius = 0.245, mass = 0.008, orbital_period = 3.551181, surface_gravity = 1.314, history = "Europa was discovered in 1610 by Galileo Galilei.", photo_link = "http://en.wikipedia.org/wiki/File:Europa-moon.jpg", photo = "images/europa.jpg", fk_planet_moon = 5))
db.session.add(moon(name = "Ganymede", radius = 0.413, mass = 0.025, orbital_period = 7.15455296, surface_gravity = 1.428, history = "Ganymede is the largest moon for Jupiter and in the Solar System.", photo_link = "http://en.wikipedia.org/wiki/File:Ganymede_g1_true_2.jpg", photo = "images/ganymede.jpg", fk_planet_moon = 5))
db.session.add(moon(name = "Mimas", radius = 0.0311, mass = 0.0000063, orbital_period = 0.942, surface_gravity = 0.064, history = "It was discovered in 1789 by William Herschel.", photo_link = "http://en.wikipedia.org/wiki/File:Mimas_Cassini.jpg", photo = "images/mimas.jpg", fk_planet_moon = 6))
db.session.add(moon(name = "Enceladus", radius = 0.1451, mass = 0.000018, orbital_period = 1.370218, surface_gravity = 0.114, history = "It was discovered in 1789 by William Herschel.", photo_link = "http://en.wikipedia.org/wiki/File:PIA08409_North_Polar_Region_of_Enceladus.jpg", photo = "images/enceladus.jpg", fk_planet_moon = 6))
db.session.add(moon(name = "Tethys", radius = 0.083, mass = 0.000103, orbital_period = 1.887802, surface_gravity = 0.147, history = "It was discovered in 1684 by G. D. Cassini.", photo_link = "http://en.wikipedia.org/wiki/File:PIA07738_Tethys_mosaic_contrast-enhanced.jpg", photo = "images/tethys.jpg", fk_planet_moon = 6))
db.session.add(moon(name = "Dione", radius = 0.088, mass = 0.000328, orbital_period = 2.73691, surface_gravity = 0.233, history = "It was discovered in 1684 by G. D. Cassini.", photo_link = "http://en.wikipedia.org/wiki/File:Dione3_cassini_big.jpg", photo = "images/dione.jpg", fk_planet_moon = 6))
db.session.add(moon(name = "Rhea", radius = 0.1, mass = 0.00039, orbital_period = 4.518212, surface_gravity = 0.265, history = "It is the second largest moon of Saturn.", photo_link = "http://en.wikipedia.org/wiki/File:PIA07763_Rhea_full_globe5.jpg", photo = "images/rhea.jpg", fk_planet_moon = 6))
db.session.add(moon(name = "Titan", radius = 0.404, mass = 0.0225, orbital_period = 15.945, surface_gravity = 1.352, history = "It is the largest moon of Saturn., photo_link = "http://en.wikipedia.org/wiki/File:Titan_in_natural_color_Cassini.jpg", photo = "images/titan.jpg", fk_planet_moon = 6))
db.session.add(moon(name = "Miranda", radius = 0.03697, mass = 0.00001103, orbital_period = 1.413479, surface_gravity = 0.079, history = "The smallest of Uranus's five round satellites.", photo_link = "http://en.wikipedia.org/wiki/File:Miranda.jpg", photo = "images/miranda.jpg", fk_planet_moon = 7))
db.session.add(moon(name = "Ariel", radius = 0.0908, mass = 0.000226, orbital_period = 2.520, surface_gravity = 0.27, history = "It is the fourth-largest moon of Uranus.", photo_link = "http://en.wikipedia.org/wiki/File:Ariel_(moon).jpg", photo = "images/ariel.jpg", fk_planet_moon = 7))
db.session.add(moon(name = "Triton", radius = 0.2122, mass = 0.00359, orbital_period = -5.876854, surface_gravity = 0.779, history = "It is Neptune's largest moon and was discovered in 1846.", photo_link = "http://en.wikipedia.org/wiki/File:Triton_moon_mosaic_Voyager_2_(large).jpg", photo = "images/triton.jpg", fk_planet_moon = 8))
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

query3 = db.session.query(star, constellation, family).filter(star.name == "Sun").filter(star.fk_constellation_star == constellation.id)\
                                                            .filter(constellation.fk_constellation_family == family.id).all()
for x in query3:
	print("star: " + x[0].name + ", constellation: " + x[1].name + ", family: " + x[2].name)


print(db.session.query(star).filter_by(name = "Sun").first().name)





#commit changes
db.session.commit()