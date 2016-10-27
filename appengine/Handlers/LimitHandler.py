from Database import Limites
	
def set_Max_Alert(sensor_type,valor_Max):
	"""This function verify if are a max alert of a sensor type on datastore, if it exist update
	the old one if not the function create's a new one as arguments it receive's the
	sensor_type: The type of the sensor alert
	valor_Max: The max limit of the sensor type alert"""
	sensor_aux = Limites.Alertas.get_or_insert(sensor_type)
	if sensor_aux == None:
		sensor_aux.set_type_sensor(sensor_type)
		sensor_aux.set_max(valor_Max)
		sensor_aux.save_alert()
	else:
		sensor_aux.set_type_sensor(sensor_type)
		sensor_aux.set_max(valor_Max)
		sensor_aux.save_alert()

def set_Min_Alert(sensor_type, valor_min):
	"""Funcion que verifica si ya existe una alerta de un valor minimo de un tipo de sensado, si existe la actualiza si no crea una nueva"""
	sensor_aux = Limites.Alertas.get_or_insert(sensor_type)
	if sensor_aux == None:
		sensor_aux.set_type_sensor(sensor_type)
		sensor_aux.set_min(valor_min)
		sensor_aux.save_alert()
	else:
		sensor_aux.set_type_sensor(sensor_type)
		sensor_aux.set_min(valor_min)
		sensor_aux.save_alert()
	
	
def get_Max_Value(sensor_type):
	"""Funcion que retorna el valor maximo del tipo de censado"""
	max_of = Limites.Alertas.get_by_key_name(sensor_type)
	if max_of:
		return max_of.max
	else:
		return False
	
def get_min_Value(sensor_type):
	"""Funcion que retorna el valor minimo del tipo de censado"""
	min_of = Limites.Alertas.get_by_key_name(sensor_type)
	if min_of:
		return min_of.min
	else:
		return False
	
def get_All_Alerts():
	"""Funcion que retorna todas las alertas en Base de Datos"""
	alerts = Limites.Alertas.all()
	return alerts
