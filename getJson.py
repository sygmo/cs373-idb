import urllib.request
import json

def getJson(val):
	response = urllib.request.urlopen(val)
	str_response = response.readall().decode('utf-8')
	obj = json.loads(str_response)
	return obj;