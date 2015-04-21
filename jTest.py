from getJson import getJson

obj = getJson("http://23.253.252.30/api/celebrity")

for x in obj:
	print(x["name"])