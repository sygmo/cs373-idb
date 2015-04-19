class MySchema(SchemaClass):
	value = TEXT
	id = ID(stored = True, unique = True)
	cls = ID(stored = True)