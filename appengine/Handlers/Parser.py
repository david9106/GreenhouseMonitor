import webapp2
import json
import cgi		
from Handlers import BDHandler #All the methods to access the DB
from Handlers import LimitHandler
from Handlers import Alertas
from Handlers import PhoneHandler

class JSON_parser(webapp2.RequestHandler):
	'''Receive the sensor JSON objects from gateway, parses them, call the comparator module and DB module'''
	def post(self):		
		try:		
			#Receive the object and decodes it
			jdata = json.JSONDecoder().decode(cgi.escape(self.request.body))
			
			#ajust values from data
			""""jdata['Tipo']=str(jdata['Tipo'])
			jdata['Valor']=float(jdata['Valor'])
			jdata['Ubicacion']=int(jdata['Ubicacion'])"""
			
			Alertas.compararLimites(jdata)
			#Saves it on the database
			if not BDHandler.alta_sensor(jdata["Tipo"].encode('utf-8'),jdata["Valor"].encode('utf-8'), jdata["Ubicacion"].encode('utf-8')): ##Just for tests, real timestamp is given by DB
				print("Error saving on DB")
		
			#Comparar si el valor esta fuera de los limites
			
			#if not Alertas.compararLimites(jdata["Tipo"],jdata["Valor"]):
			#Alertas.enviar_mensaje(jdata["Tipo"],jdata["Valor"])
				
			self.response.write(json.dumps(jdata))
		except (ValueError, TypeError):			
			self.error(415) #Using 415 UNSUPPORTED MEDIA TYPE
			self.response.write("Not a JSON object")

			
	def get(self):
		self.response.write('Hello, what are you doing here?')
