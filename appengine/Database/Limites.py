from google.appengine.ext import db

class Alertas(db.Model):
	type = db.Key()
	max = db.FloatProperty()
	min = db.FloatProperty()
	
	def set_Valor_Max(tipo_sensor,valor_Max):
		"""Funcion que verifica si ya existe una alerta de un valor maximo de un tipo de sensado, si existe la actualiza si no crea una nueva"""
		sensor_aux = Alertas.get_or_insert(tipo_sensor)
		if sensor_aux == None:
			sensor_aux.max = valor_Max
			sensor_aux.put()
		else:
			sensor_aux.max = valor_Max
			sensor_aux.put()
		
	def set_Valor_Min(tipo_sensor,valor_min):
		"""Funcion que verifica si ya existe una alerta de un valor minimo de un tipo de sensado, si existe la actualiza si no crea una nueva"""
		sensor_aux = Alertas.get_or_insert(tipo_sensor)
		if sensor_aux == None:
			sensor_aux.max = valor_min
			sensor_aux.put()
		else:
			sensor_aux.max = valor_min
			sensor_aux.put()

	def save_alert(self):
		"""Guardar alerta creada en Base de Datos"""
		self.put()

	def get_Max_Value(type):
		"""Funcion que retorna el valor maximo del tipo de censado"""
		max_of = Alertas().all().filter('type =', type).fetch(1)
		return max_of
	
	def get_min_Value(type):
		"""Funcion que retorna el valor minimo del tipo de censado"""
		min_of = Alertas().all().filter('type =',type).fetch(1)
		return min_of
	
	def get_All_Alerts():
		"""Funcion que retorna todas las alertas en Base de Datos"""
		alerts = Alertas.all()
		return alerts
		