from Database import Limites

##@brief This function disable a alert stored on the database 
#@details Deshabilita la opacion de envio de alertas para ese tipo de sensor, si los valores sobrepasan los limites sera ignorado por el sistema
#@param sensor_type Is a string that has the name of type of sensor like "Temperature", "Humidity", "Luxes", etc
def disable_alerts(sensor_type):
	sensor_aux = Limites.SensorLimits.get_or_insert(sensor_type) #Get's the db instance of that sensor type
	if sensor_aux == None: #If it doesn't exist, creates one
		sensor_aux.set_type_sensor(sensor_type)
	sensor_aux.set_disable_alerts(False)
	sensor_aux.save_alert()

##@brief This function disable a alert stored on the database 
#@details Deshabilita la opacion de envio de alertas para ese tipo de sensor, si los valores sobrepasan los limites sera ignorado por el sistema
#@param sensor_type Is a string that has the name of type of sensor like "Temperature", "Humidity", "Luxes", etc	
def set_Max_Alert(sensor_type,valor_Max):
	sensor_aux = Limites.SensorLimits.get_or_insert(sensor_type)
	if sensor_aux == None:
		sensor_aux.set_type_sensor(sensor_type)
	sensor_aux.set_max(valor_Max)
	sensor_aux.save_alert()

##@brief Function used to set the minimun limit in a sensor type
#@details This function verify if there are a min alert limit of a sensor type on datastore, if it exist the function update the old one if not the function create's a new one, as arguments it receive's the
#@param sensor_type: The type of the sensor limit
#@param valor_min: The max limit of the sensor type alert
def set_Min_Alert(sensor_type, valor_min):
	sensor_aux = Limites.SensorLimits.get_or_insert(sensor_type)
	if sensor_aux == None:
		sensor_aux.set_type_sensor(sensor_type)
	sensor_aux.set_min(valor_min)
	sensor_aux.save_alert()
	
##@brief Function used to get the max limit value of type of sensor
#@details This functon get's the max limit value of a type of sensor and return's it, this function receive as argument the type of the sensor to verify if there's no limit value of that sensor the function return false
#@param sensor_type: The type of the sensor limit
#@return The max limit value of a type of sensor		
def get_Max_Value(sensor_type):
	max_of = Limites.SensorLimits.get_by_key_name(sensor_type)
	if max_of:
		return max_of.max
	else:
		return False

##@brief This function get the minimun limit of a sensor type
#@details This functon get's the min limit value of a type of sensor and return it
#@return If there's no limit value of that sensor the function return false else the function return the minum value			
def get_min_Value(sensor_type):
	min_of = Limites.SensorLimits.get_by_key_name(sensor_type)
	if min_of:
		return min_of.min
	else:
		return False

def isDisabled():
	"""Funcion para simular si estan habilitadas o deshabilitadas las alertas"""
	return False
