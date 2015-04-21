import urllib.request
import json

def getJson(val):
	response = urllib.request.urlopen(val)
	str_response = response.readall().decode('utf-8')
	obj = json.loads(str_response)
	return obj;

def getCharge(val):
	jsonObj = getJson("http://23.253.252.30/api/charge/" + str(val))
	crime = {}
	crime['crime'] = jsonObj['crime']['name']
	crime['description'] = jsonObj['description']
	return crime


def getCelebrity(val):
	jsonObj = getJson("http://23.253.252.30/api/celebrity/" + str(val))
	celebrity = {}

	celebrity['name'] = jsonObj['name']

	#print(jsonObj['charges'][0]['id'])
	charge = getCharge(jsonObj['charges'][0]['id'])

	celebrity['crime'] = charge['crime']
	celebrity['description'] = charge['description']

	celebrity['photo'] = jsonObj['picture_url']
	return celebrity







