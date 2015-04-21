from unittest import main, TestCase
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import request
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, LargeBinary, Boolean

app = Flask(__name__)
db = SQLAlchemy(app)

#creates the database
db.reflect()
db.drop_all()
db.create_all()

class family(db.Model):
    __tablename__ = "family"
    id = db.Column(Integer, primary_key = True)
    name = db.Column(Text, nullable = False)
    description = db.Column(Text)

class tests(TestCase):

    def test_api_path1(self):
        with app.test_request_context('/planet'):
            assert request.path == '/planet'

    def test_api_path2(self):
        with app.test_request_context('/constellation'):
            assert request.path == '/constellation'

    def test_api_path3(self):
        with app.test_request_context('/family'):
            assert request.path == '/family'

    def test_api_path4(self):
        with app.test_request_context('/star'):
            assert request.path == '/star'

    def test_api_path5(self):
        with app.test_request_context('/moon'):
            assert request.path == '/moon'

    def test_api_path6(self):
        with app.test_request_context('/ExoPlanet'):
            assert request.path == '/ExoPlanet'

    def test_api_get(self):
        with app.test_request_context('/planet', method='GET'):
            assert request.method == 'GET'

if __name__ == "__main__":
    main()