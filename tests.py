from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models import family, constellation, planet, star, moon, ExoPlanet
from difficulty import db
import threading


#for this tests to work you need to have a postgres database 
#set up with the name testdb, no username, no password

class tests(TestCase):

	#setup the database
	def setUp(self):
		db.drop_all()
		db.create_all()

		self.lock = threading.Lock()

	
	#Test that the table family is writable
	def test_write_family(self):
		self.lock.acquire()
		engine = create_engine('sqlite:///testdb.db')
		Session = sessionmaker(bind = engine)
		session = Session()

		query = session.query(family).all()
		startSize = len(query)
		print(startSize)

		db.session.add(family(name = "Ursa Major"))
		res = session.query(family).all()
		db.session.commit()

		query = session.query(family).all()
		endSize = len(query)

		self.assertEqual(startSize + 1, endSize)	
		self.lock.release()	

	#Test that the table family is readable
	def test_read_family(self):
		self.lock.acquire()
		engine = create_engine('sqlite:///testdb.db')
		Session = sessionmaker(bind = engine)
		session = Session()

		db.session.add(family(name = "Zodiac"))
		db.session.commit()

		query = session.query(family).all()
		found = False

		for x in query:
			if(x.name == "Zodiac"):
				found = True

		assert(found)
		self.lock.release()

	
	#Test deletion of a row in family
	def test_delete_family_row(self):
		self.lock.acquire()
		engine = create_engine('sqlite:///testdb.db')
		Session = sessionmaker(bind = engine)
		session = Session()

		db.session.add(family(name = "delete"))
		db.session.commit()

		toRemove = session.query(family).filter_by(name = "delete").first()

		assert(toRemove != None)

		session.delete(toRemove);
		session.commit()

		toRemove = session.query(family).filter_by(name = "delete").first()

		assert(toRemove == None)

		self.lock.release()


if __name__ == "__main__":
	main()
