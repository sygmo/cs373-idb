from difficulty import db
from models import family

#creates the database
print("about to drop")
db.drop_all()
print("dropped")
print("about to create")
db.create_all()
print("created")

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
db.session.add(family(name = "Home"))
#commit changes
db.session.commit()