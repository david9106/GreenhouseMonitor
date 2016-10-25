from DataBase import Limites
	
def set_Max_Alert(sensor_type,valor_Max):
	"""Funcion que verifica si ya existe una alerta de un valor maximo de un tipo de sensado, si existe la actualiza si no crea una nueva"""
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
	
def get_min_Value(type):
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