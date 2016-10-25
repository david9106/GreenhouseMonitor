from google.appengine.ext import db

class Alertas(db.Model):
	"""This class have's the limit's for the alert to configure on the server
	these are the attributes:
	type_sensor: it describes the sensor typo of the value
	max: this attribute have the maximun limit value
	min: this attribute hace the minumun limit value"""
	type_sensor = db.Key()
	max = db.FloatProperty()
	min = db.FloatProperty()
	
	def set_type_sensor(self, sensor_type):
		"""This function is used to set the sensor type of the limit alert, it receive the sensor type as argument"""
		try:
			self.type_sensor = str(sensor_type)
		except ValueError:
			print("The name of the sensor type must be a string")
			
	def set_max(self,max_Value):
		"""This function is used to set the mas value of the limit alert
		the max_Value variable is passed as argument"""
		try:
			self.max = float(max_Value)
		except ValueError:
			print("Max value must be a floting point number")
	
	def set_min(self,min_Value):
		"""This function set the minimun limit value of a sensor type alert
		the minimun value is passed as an argument"""
		try:
			self.min = float(min_Value)
		except ValueError:
			print("Max value must be a floting point number")
			
	def save_alert(self):
		"""This function save's or update the created alert"""
		self.put()
		