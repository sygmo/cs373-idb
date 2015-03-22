from difficulty import db
from models import family

#creates the database
db.drop_all()
db.create_all()

#insert sample data
db.session.add(family(name = "Ursa Major"))
db.session.add(family(name = "Zodiac"))
db.session.add(family(name = "Perseus"))
db.session.add(family(name = "Hercules"))
db.session.add(family(name = "Orion"))
db.session.add(family(name = "Heavenly Waters"))
db.session.add(family(name = "Bayer"))
db.session.add(family(name = "La Caille"))
#commit changes
db.session.commit()