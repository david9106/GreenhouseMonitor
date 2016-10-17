from google.appengine.ext import db

class Alertas(db.Model):
	name_type = db.Key()
	max = db.FloatProperty()
	min = db.FloatProperty()
	
	def set_Valor_Max(tipo_sensor,valor_Max):
		"""Funcion que verifica si ya existe una alerta de un valor maximo de un tipo de sensado, si existe la actualiza si no crea una nueva"""
		sensor_aux = Alertas.get_or_insert(tipo_sensor)
		if sensor_aux == None:
			sensor_aux.name_type = tipo_sensor
			sensor_aux.max = valor_Max
		else:
			sensor_aux.name_type = tipo_sensor
			sensor_aux.max = valor_Max

	def set_Valor_Min(tipo_sensor,valor_min):
		"""Funcion que verifica si ya existe una alerta de un valor minimo de un tipo de sensado, si existe la actualiza si no crea una nueva"""
		sensor_aux = Alertas.get_or_insert(tipo_sensor)
		if sensor_aux == None:
			sensor_aux.name_type = tipo_sensor
			sensor_aux.max = valor_min
		else:
			sensor_aux.name_type = tipo_sensor
			sensor_aux.max = valor_min

	def save_alert(self):
		"""Guardar alerta creada en Base de Datos"""
		self.put()
		