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
db.session.add(family(name = "Ursa Major"))
db.session.add(family(name = "Zodiac"))
db.session.add(family(name = "Perseus"))
db.session.add(family(name = "Hercules"))
db.session.add(family(name = "Orion"))
db.session.add(family(name = "Heavenly Waters"))
db.session.add(family(name = "Bayer"))
db.session.add(family(name = "La Caille"))
db.session.add(family(name = "home"))
db.session.commit()

#insert constellation
db.session.add(constellation(name = "Solar System", fk_constellation_family = 9))
db.session.commit()

#stars
db.session.add(star(name = "Sun", fk_constellation_star = 1))
db.session.commit()
print("added")

#planets
db.session.add(planet(name = "Jupiter", fk_star_planet = 1))
db.session.add(planet(name = "Earth", fk_star_planet = 1))
db.session.add(planet(name = "mars"))

db.session.commit()





query = db.session.query(planet, star, constellation, family).filter(planet.fk_star_planet == star.id)\
															.filter(star.fk_constellation_star == constellation.id)\
															.filter(constellation.fk_constellation_family == family.id).all()
for x in query:
	print("planet: " + x[0].name + ", Star: " + x[1].name + ", constellation: " + x[2].name + ", family: " + x[3].name)





print(db.session.query(star).filter_by(name = "Sun").first().name)





#commit changes
db.session.commit()