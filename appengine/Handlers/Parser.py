import webapp2
import json
import cgi		
from Handlers import CensadoHandler #All the methods to access the DB
from Handlers import LimitHandler
from Handlers import Alertas
from Handlers import PhoneHandler

class JSON_parser(webapp2.RequestHandler):
	'''Receive the sensor JSON objects from gateway, parses them, call the comparator module and DB module'''
	def post(self):		
		try:		
			#Receive the object and decodes it
			jdata = json.JSONDecoder().decode(cgi.escape(self.request.body))
			
			#Saves it on the database
			if not CensadoHandler.alta_sensor(str(jdata["Tipo"]),float(jdata["Valor"]), str(jdata["Ubicacion"])): ##Just for tests, real timestamp is given by DB
				print("Error saving on DB")			
			
			#Compares if new measure goes above/below the limits to send an sms message
			Alertas.compararLimites(jdata)
	
		except (ValueError, TypeError):			
			self.error(415) #Using 415 UNSUPPORTED MEDIA TYPE
			self.response.write("Not a JSON object")

			
	def get(self):
		self.response.write('Hello, what are you doing here?')
