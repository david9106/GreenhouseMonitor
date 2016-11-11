##@file Limites.py
#@brief This module haves the model of the limits stablished for the sms alerts
from google.appengine.ext import db

##@class SensorLimits
#@brief This class haves the limit's for the alert to configure on the server
#@details With this entity the user would be able to store limit values for the sensed data in the greenhouse
class SensorLimits(db.Model):
	##@brief It describes the sensor typo of the value
	type_sensor = db.Key()
	##@brief This attribute have the maximun limit value
	max = db.FloatProperty()
	##@brief	This attribute hace the minumun limit value
	min = db.FloatProperty()
	##@brief A boolean property that advice if the limit value alert is enable
	disable_alerts = db.BooleanProperty()
	
	##@brief The funtion of this is to enable or diable the receive of alerts from the server
	#@param new_status: Has a boolean that says if the alert is goin to be enable or disable 
	def enabling_limits(self, new_status):
		if isinstance(new_status, bool):
			self.disable_alerts = new_status
		else:
			print("The new disable_alerts value isn't boolean")
	
	##@brief This function is used to set the sensor type of the limit alert
	#@param sensor_type: This parameter haves the type of sensed data that is going to have the limit alert
	def set_type_sensor(self, sensor_type):
		try:
			self.type_sensor = str(sensor_type)
		except ValueError:
			print("The name of the sensor type must be a string")

	##@brief This function is used to set the max value of the limit alert 		
	#@param max_Value: Haves a floting point number with the maximun limit value of the alert
	def set_max(self,max_Value):
		try:
			self.max = float(max_Value)
		except ValueError:
			print("Max value must be a floting point number")
	
	##@brief This function set the minimun limit value of a sensor type alert
	#@param min_Value: Haves a floting point number with the minimun limit value of the alert
	def set_min(self,min_Value):
		try:
			self.min = float(min_Value)
		except ValueError:
			print("Max value must be a floting point number")
	
	##@brief This function save's or update the created alert
	def save_alert(self):
		self.put()
		