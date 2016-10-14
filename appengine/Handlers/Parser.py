import webapp2
import json
import cgi		
from Handlers import BDHandler #All the methods to access the DB

class JSON_parser(webapp2.RequestHandler):
	'''Receive the sensor JSON objects from gateway, parses them, call the comparator module and DB module'''
	def post(self):		
		try:		
			#Receive the object and decodes it
			jdata = json.JSONDecoder().decode(self.request.body)
			print(jdata["Tipo"])
			self.response.write(json.dumps(jdata))
		except (ValueError, TypeError):			
			self.error(415) #Using 415 UNSUPPORTED MEDIA TYPE
			self.response.write("Not a JSON object")
			
	def get(self):
		self.response.write('Hello, what are you doing here?')
