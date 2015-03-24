from unittest import main, TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models import family
from difficulty import db




class tests(TestCase):
	engine = create_engine('postgresql://localhost/universe')
	#Creates session
	Session = sessionmaker(bind=engine)
	session = Session()
	res = session.query(family).all()

	def test_read_family_id(self):
		engine = create_engine('postgresql://localhost/universe')
		#Creates session
		Session = sessionmaker(bind=engine)
		session = Session()
		res = session.query(family).all()

		x = res[0]
		self.assertEqual(x.id, 1)


	def test_read_family_name(self):
		engine = create_engine('postgresql://localhost/universe')
		#Creates session
		Session = sessionmaker(bind=engine)
		session = Session()
		res = session.query(family).all()

		x = res[0]
		self.assertEqual(x.name, "Ursa Major")

	def test_read_id_second(self):
		engine = create_engine('postgresql://localhost/universe')
		#Creates session
		Session = sessionmaker(bind=engine)
		session = Session()
		res = session.query(family).all()

		x = res[1]
		self.assertEqual(x.id, 2)

	def test_read_name_second(self):
		engine = create_engine('postgresql://localhost/universe')
		#Creates session
		Session = sessionmaker(bind=engine)
		session = Session()
		res = session.query(family).all()

		x = res[1]
		self.assertEqual(x.name, "Zodiac")

if __name__ == "__main__":
	main()
