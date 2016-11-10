from google.appengine.ext import db
import datetime

##@class Censado
#@brief A entity that haves all the properties of a sensing value from the sensor
#@details The Censado class is a db model that have the value's of a sensor type and identify what type of sensor is
class Censado(db.Model):
	##@brief It have the id of the LiSANDRA module allocated on the green house
	id_LiSANDRA = db.StringProperty()
	##@brief It have's the type of the sensor value
	type = db.StringProperty()
	##@brief value: Is the value of the sensing parameter
	value = db.FloatProperty()
	##@brief when: have's the date and time when the sensor detect's something
	when = db.DateTimeProperty(auto_now_add=True)
	
	##@brief This metod set the id of the LiSANDRA module in the entity
	#@param id_LiSANDRA: Haves a string with the id of the LiSANDRA module to store in cloud datastore
	def set_LiSANDRA(self, id_LiSANDRA):
		self.id_LiSANDRA = id_LiSANDRA
		return True
	
	##@brief This metod used to set the type of the sensed data received
	#@details The metod add's wich type of sensing is the new Censado model
	#@param type: determine the type of sensed data received from the gateway
	def set_Type(self, type):		
		try:
			type = str(type)
			self.type = type
			return True
		except ValueError:
			print("Tipo de censado no permitido")
			return False

	##@brief This metod set the value of the sensed data received from the gateway
	#@param value: Haves the value of the sensed data, the value must be a floating point number
	def set_Value(self, value):	
		try:
			value = float(value)
			self.value = value
			return True
		except ValueError:
			print("Valor del sensor debe ser flotante")
			return False
	
	##@brief The function of this metod is save the new Censado model to the cloud datastore
	def save_In_DB(self):
		self.put()
		
	##@brief This function get's the sensing data between two date's
	#@details If the two dates are present in datastore the model returns all the consulted data
	#@param date_1: First date to compare
	#@param date_2: Second date to compare
	#@param type: The type of the sensed data stored in cloud datastore
	#@return All the data between the consulted dates in cloud datastore 
	def get_Data(self, date_1, date_2, type):		
		if isinstance(date_1, datetime.datetime) and isinstance(date_2, datetime.datetime):
			return Censado.all().filter('when >',date_1).filter('when <',date_2).filter('type =',type).fetch(None)
		else:
			return None
