##@file CensadoHandler.py
#@brief CensadoHandler is the interface to DB this particular file only takes care of the sensor measure DB part interface
#@details In order to be able to change of DB engine in the future if it's needed, this interface was implemented.
#So all the system uses these functions to acces DB instead of direct interaction with entity, which let to change the DB engine
#and all the changes will be need only within the functions of this module

#Above rules apply to all the modules in the Handlers directory.
import datetime
from Database import Censado 


##@brief Save entire sensor data on DB
#@details The Function instance's a new sensing obteined and pass all the properties of it, passes the measure and the id od the LiSANDRA module
#@param sensor_type: A string that have's the name of the type of sensor
#@param measure: This parameter have's the measure value of a sensor type
#@param id_LiSANDRA: The identification of the LiSANDRA module
def alta_sensor(sensor_type,medicion,id_LiSANDRA):
	sensor = Censado.Censado()
	if sensor.set_Type(sensor_type):
		if sensor.set_Value(medicion):
			if sensor.set_LiSANDRA(id_LiSANDRA):
				sensor.save_In_DB()
				return True
	return False

##@breif Interface to the get_Sensor_Types
#@details Retrieves the available sensor types on DB
def get_available_sensors():
	return Censado.Censado().get_Sensor_Types()

##@brief Get all the measures of a certain sensor type from the specified year
#@param a_year means the year where I want the measures
#@param tipo_sensor means the kind of sensor that I need
def get_year_measures(tipo_sensor, a_year):	
	low_date_str = '{:0>4}-01-01 00:00:00'.format(a_year) #Start of the year
	high_date_str = '{:0>4}-12-31 23:59:59'.format(a_year) #End of the year
	low_date = datetime.datetime.strptime(low_date_str, '%Y-%m-%d %H:%M:%S') #Converts string to datetime
	high_date = datetime.datetime.strptime(high_date_str, '%Y-%m-%d %H:%M:%S') 
	return Censado.Censado().get_Data(low_date, high_date, tipo_sensor)
	
##@brief Retrieves the count of all sensor of given type
#@param sensor_type Is the sensor type to be counted
#@details Interface for the entity's method of the same name
def get_sensor_count(sensor_type):
	return Censado.Censado().get_sensor_count(sensor_type)
	
##@brief Get all the measures with that type of sensor, of this year
#@details This function get's all the measures stored in a year, first get the todays date and then get the diference between that geted day and the past 12 months
#@param sensor_type: A string that have's the name of the type of sensor		
def get_this_year_measures(tipo_sensor):
	now = datetime.datetime.now() #Get today's full date
	year = now.year
	low_date_str = '{:0>4}-01-01 00:00:00'.format(year) #Start of the year
	high_date_str = '{:0>4}-12-31 23:59:59'.format(year) #End of the year
	
	low_date = datetime.datetime.strptime(low_date_str, '%Y-%m-%d %H:%M:%S') #Converts string to datetime
	high_date = datetime.datetime.strptime(high_date_str, '%Y-%m-%d %H:%M:%S') 
	
	return Censado.Censado().get_Data(low_date, high_date, tipo_sensor)
		
	
##@brief Get all the sensor measures of the day
#@details The first thig that this function does is get the todays date and then filter it in the query used to obtain the measures
#@param sensor_type: A string that have's the name of the type of sensor
#@return The function return the sensed data of todays date		
def get_today_measures(sensor_type):
	now = datetime.datetime.now() #Get today's full date
	year = now.year
	month = now.month
	day = now.day
	low_date_str = '{:0>4}-{:0>2}-{:0>2} 00:00:00'.format(year,month,day) #start of the day
	high_date_str = '{:0>4}-{:0>2}-{:0>2} 23:59:59'.format(year,month,day) #end of the day

	low_date = datetime.datetime.strptime(low_date_str, '%Y-%m-%d %H:%M:%S') #converts the day limits to date
	high_date = datetime.datetime.strptime(high_date_str, '%Y-%m-%d %H:%M:%S')
	return Censado.Censado().get_Data(low_date, high_date, sensor_type) #Gets sensor data btw dates, in this case everything from today

##@brief Get all the sensor measures of the week, today - 7 days
#@details This function gets all the measures stored in a week, first get the todays date and then the function get a difference between that date and the past 7 days	
#@param sensor_type: A string that have's the name of the type of sensor
#@return The function return a list with all the sensed data of a week ago
def get_this_week_measures(sensor_type):
	now = datetime.datetime.now()#Get today's full date
	end_day = now - datetime.timedelta(days=7) #the day a week ago
	return Censado.Censado().get_Data(now, end_day, sensor_type) #Gets the week btw today and 7 days ago

##@brief Get all the sensor measures of one month, today to 28 days
#@details This function gets all the measures stored in a month, first get the todays date and then the function get a difference between that date and the past 28 days	
def get_this_month_measures(sensor_type):
	now = datetime.datetime.now()#Get today's full date
	end_day = now - datetime.timedelta(days=28) #the day aprox a month ago
	return Censado.Censado().get_Data(now, end_day, sensor_type) #Gets the week btw today and 28 days ago
	
##@breif Get's the most recent measure of certain sensor type
#@details Just an interface to the DB
#@param sensor_type is the kind of sensor that I want the measure from
def get_last_value(sensor_type):
	return Censado.Censado().get_Last_Measure(sensor_type)

##@brief Funcion para buscar censados entre fechas y tiempos
#@details First the function filter the list of measure using the first date and apply another filter with the second date and finally applies a filter for a type of sensor
#@param sensor_type: A string that have's the name of the type of sensor
#@param date_1: A datetime object with a valid date in datastore
#@param date_2: A datetime object with a valid date in datastore
#@return The function return a list with all the sensed data between two dates
def get_data_between_dates(date_1, date_2, sensor_type):
	"""Funcion para buscar censados entre fechas y tiempos"""
	censados = Censado.all().filter('when >',datetime.datetime(date_1.year, date_1.month, date_1.day, date_1.hour, date_1.minutes)).filter('when <',datetime.datetime(date_2.year, date_2.month, date_2.day, date_2.hour, date_2.minutes)).filter('type =',type).fetch(None)
	return censados
