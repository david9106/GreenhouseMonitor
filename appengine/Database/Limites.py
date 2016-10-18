from google.appengine.ext import db

class Alertas(db.Model):
	type_sensor = db.Key()
	max = db.FloatProperty()
	min = db.FloatProperty()
	
	def set_type_sensor(self, sensor_type)
		try:
			self.type_sensor = str(sensor_type)
		except ValueError:
			print("The name of the sensor type must be a string")
			
	def set_max(self,max_Value)
		try:
			self.max = float(max_Value)
		except ValueError:
			print("Max value must be a floting point number")
	
	def set_min(self,min_Value)
		try:
			self.min = float(min_Value)
		except ValueError:
			print("Max value must be a floting point number")
			
	def save_alert(self):
		"""Guardar alerta creada en Base de Datos"""
		self.put()
		