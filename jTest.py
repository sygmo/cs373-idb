from getJson import getJson
import getJson as getCeleb

obj = getJson("http://23.253.252.30/api/celebrity")


for x in obj:
	celebrity = getCeleb.getCelebrity(x['id'])
	print("Name: " + celebrity['name'])
	print("Crime: " + celebrity['crime'])
	print("Description: " + celebrity['description'])
	print("Photo URL" + celebrity['photo'])
	print()
