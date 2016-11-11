##@file SensorParser.py
#@brief This file haves the function that handles the received data from the gateway and decodify it
import webapp2
import json
import cgi		
from Handlers import CensadoHandler #All the methods to access the DB
from Handlers import LimitHandler
from Handlers import Alertas
from Handlers import PhoneHandler

##@class JSON_sensor_parser
#@brief Receive the sensor JSON objects from gateway, parses them, call the comparator module and DB module
#@details This Function receive a JSON object and parse ir, then verify if the sensed data type excist in datastore, if not creates a new one entity in datastore if not updates the excisting one, then compares the receive data with the excisting limits in datastore
class JSON_sensor_parser(webapp2.RequestHandler):
	def post(self):		
		try:		
			#Receive the object and decodes it
			jdata = json.JSONDecoder().decode(cgi.escape(self.request.body))
			
			#Saves it on the database
			if not CensadoHandler.alta_sensor(str(jdata["Tipo"]),float(jdata["Valor"]), str(jdata["Ubicacion"])): ##Just for tests, real timestamp is given by DB
				print("Error saving on DB")			
			
			#Compares if new measure goes above/below the limits to send an sms message
			Alertas.compararLimites(jdata)
	
		except (ValueError, TypeError,KeyError):
			'''KeyError goes in case that the json ID doesn't exists, mainly ["Tipo"] but can be others'''			
			self.error(415) #Using 415 UNSUPPORTED MEDIA TYPE
			self.response.write("Not a JSON object")

			
	def get(self):
		self.response.write('Hello, what are you doing here?')
