from Database import Limites

def new_Alert(sensor_type, max_value, min_value)
	limit = Limites.Alertas()
	limit.set_Valor_Max(sensor_type,max_value)
	limit.set_Valor_min(sensor_type,min_value)
	limit.save_alert()
	
def get_Max_Value(type):
	"""Funcion que retorna el valor maximo del tipo de censado"""
	max_of = Limites.Alertas.get_by_key_name(type)
	if max_of:
		return max_of.max
	else:
		return False
	
def get_min_Value(type):
	"""Funcion que retorna el valor minimo del tipo de censado"""
	min_of = Limites.Alertas.get_by_key_name(type)
	if min_of:
		return min_of.min
	else:
		return False
	
def get_All_Alerts():
	"""Funcion que retorna todas las alertas en Base de Datos"""
	alerts = Limites.Alertas.all()
	return alerts