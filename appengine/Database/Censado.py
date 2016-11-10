from google.appengine.ext import db
import datetime

class Censado(db.Model):
	"""The Censado class is a db model that have the value's of a sensor type
	and identify what type of sensor is
	it have's the next attribute's:
	id_LiSANDRA: it have the id of the LiSANDRA module allocated on the green house
	type: it have's the type of the sensor value
	value: is the value of the sensing parameter
	when: have's the date and time when the sensor detect's something"""
	id_LiSANDRA = db.StringProperty()
	type = db.StringProperty()
	value = db.FloatProperty()
	when = db.DateTimeProperty(auto_now_add=True)

	def set_LiSANDRA(self, id_LiSANDRA):
		"""This function add's the id of the LiSANDRA module to the Censado module, it have 
		id_LiSANDRA as an argument"""
		self.id_LiSANDRA = id_LiSANDRA
		return True
	
	def set_Type(self, type):
		""" This function add's wich type of sensing is the new Censado model
		it receive the type as argument"""		
		try:
			type = str(type)
			self.type = type
			return True
		except ValueError:
			print("Tipo de censado no permitido")
			return False

	def set_Value(self, value):
		"""Funciton used to set the value of the sensing to store
		the value is passed as argument"""		
		try:
			value = float(value)
			self.value = value
			return True
		except ValueError:
			print("Valor del sensor debe ser flotante")
			return False
			
	def save_In_DB(self):
		"""Function used to store the new Censado model to the datastore"""
		self.put()
		

	def get_Data(self, date_1, date_2, type):
		"""This function get's the sensing data between two date's if are present in datastore, if there are data the function return's it in a iterating list
		if not the function return False. As arguments the function receive two dates  and the type of the sensor to verify
		"""			
		if isinstance(date_1, datetime.datetime) and isinstance(date_2, datetime.datetime):
			return Censado.all().filter('when >',date_1).filter('when <',date_2).filter('type =',type).fetch(None)
		else:
			return None
		#return Censado.all().filter('when >',datetime.datetime(date_1.year, date_1.month, date_1.day, date_1.hour, date_1.minutes)).filter('when <',datetime.datetime(date_2.year, date_2.month, date_2.day, date_2.hour, date_2.minutes)).filter('type =',type).fetch(None)

	def get_Sensor_Tyes(self):
		"""
		Return a list of the available sensor types on the database
		Ex. if currently exists "Temperatura" and "Humedad", the function will return a listing both
		"""
		query_str = "SELECT DISTINCT type from Censado"
		return db.GqlQuery(query_str)
		
	
