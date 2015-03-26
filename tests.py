from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models import family
from difficulty import db


#for this tests to work you need to have a postgres database 
#set up with the name testdb, no username, no password

class tests(TestCase):

	#setup the database
	def setUp(self):
		db.drop_all()
		db.create_all()

	#Test that the table family is writable
	def test_write_family(self):
		engine = create_engine('sqlite:///testdb.db')
		Session = sessionmaker(bind = engine)
		session = Session()

		query = session.query(family).all()
		startSize = len(query)

		db.session.add(family(name = "Ursa Major"))
		res = session.query(family).all()
		db.session.commit()

		query = session.query(family).all()
		endSize = len(query)

		self.assertEqual(startSize + 1, endSize)	

		

	#Test that the table family is readable
	def test_read_family_name(self):
		engine = create_engine('sqlite:///testdb.db')
		Session = sessionmaker(bind = engine)
		session = Session()

		db.session.add(family("Zodiac"))

		query = session.query(family).

		print(len(res))
		#x = res[0]
		#self.assertEqual(x.name, "Ursa Major")


	'''
	def test_read_id_second(self):
		res = self.session.query(family).all()

		x = res[1]
		self.assertEqual(x.id, 2)

	def test_read_name_second(self):
		res = self.session.query(family).all()

		x = res[1]
		self.assertEqual(x.name, "Zodiac")'''

if __name__ == "__main__":
	main()
