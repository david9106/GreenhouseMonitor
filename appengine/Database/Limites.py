from google.appengine.ext import db

class SensorLimits(db.Model):
	type_sensor = db.Key()
	max = db.FloatProperty()
	min = db.FloatProperty()
	disable_alerts = db.BooleanProperty()
	
	def __init__(self):
		self.disable_alerts = True
		self.max = 0.0
		self.min= 0.0
		
	def set_disable_alerts(self, new_status):
		if isinstance(new_status, bool):
			self.disable_alerts = new_status
		else:
			print("The new disable_alerts value isn't boolean")

	def set_type_sensor(self, sensor_type):
		try:
			self.type_sensor = str(sensor_type)
		except ValueError:
			print("The name of the sensor type must be a string")
			
	def set_max(self,max_Value):
		try:
			self.max = float(max_Value)
		except ValueError:
			print("Max value must be a floting point number")
	
	def set_min(self,min_Value):
		try:
			self.min = float(min_Value)
		except ValueError:
			print("Max value must be a floting point number")
			
	def save_alert(self):
		"""Guardar alerta creada en Base de Datos"""
		self.put()
		
	def get_max(self):
		return self.max
		
	def get_min(self):
		return self.min

	def get_disable_alerts_status(self):
		return self.disable_alerts
