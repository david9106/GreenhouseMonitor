import datetime

def alta(tipo_sensor,medicion,hora_sensado,ID):
	sensor = BSSensor.Sensor()
	sensor.tipo_sensor = tipo_sensor
	sensor.valor = medicion
	sensor.tiempo = hora_sensado
	sensor.ID = ID
	
def buscar_Por_Id(ID):
	return BDSensor.Sensor().find_By_Id(ID)
	
def buscar_Por_Tipo(tipo_sensor):
	return BDSensor.Sensor().find_By_Id(tipo_sensor)
	
def mostrar_Todo():
	return BDSensor.Sensor().All() 