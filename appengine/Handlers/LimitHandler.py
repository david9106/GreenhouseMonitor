from Database import Limites
	
def set_Max_Alert(sensor_type,valor_Max):
	"""This function verify if there are a max limit alert of a sensor type on datastore, if it exist the function update
	the old one if not the function create's a new one, as arguments it receive's the
	sensor_type: The type of the sensor alert
	valor_Max: The max limit of the sensor type alert
	example: 
	set_Max_Alert('Temperature', 24.3)
	Alert:
	sensor_type='Temperature'
	max = 24.3
	"""
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
	"""This function verify if there are a min alert limit of a sensor type on datastore, if it exist the function update
	the old one if not the function create's a new one, as arguments it receive's the
	sensor_type: The type of the sensor alert
	valor_min: The max limit of the sensor type alert
	example: 
	set_min_Alert('Temperature', 10.3)
	Alert:
	sensor_type='Temperature'
	min = 10.3
	"""
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
	"""This functon get's the max limit value of a type of sensor and return's it, this function receive as argument the type of the sensor to verify
	if there's no limit value of that sensor the function return false"""
	max_of = Limites.Alertas.get_by_key_name(sensor_type)
	if max_of:
		return max_of.max
	else:
		return False
	
def get_min_Value(type):
	"""This functon get's the min limit value of a type of sensor and return's it, this function receive as argument the type of the sensor to verify
	if there's no limit value of that sensor the function return false"""
	min_of = Limites.Alertas.get_by_key_name(sensor_type)
	if min_of:
		return min_of.min
	else:
		return False
	
def get_All_Alerts():
	"""This function get's all the data of limit alerts in datastore and retun's it"""
	alerts = Limites.Alertas.all()
	return alerts
