# default config

class BaseConfig(object):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:cs373@localhost/universe'

class TestConfig(object):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:cs373@localhost/testdb'

class LocalConfig(object):
	DEBUG = False	
	SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/universe'

class LocalTestConfig(object):
	DEBUG = False	
	SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/testdb'

class UnitTestConfig(object):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/unittest'

