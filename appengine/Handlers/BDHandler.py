import datetime
from Database import Censado 


import random #Temporal import, to be able to generate random numbers to simulate measures

def alta_sensor(tipo_sensor,medicion,hora_sensado,id_LiSANDRA):
	"""Save entire sensor data on DB"""
	sensor = Censado.Censado()
	sensor.set_Type(tipo)
	sensor.set_Value(medicion)
	sensor.set_Time(hora_sensado)
	sensor.set_LiSANDRA(id_LiSANDRA)
	sensor.save_In_DB()
	
	
def get_this_year_measures(tipo_sensor):
	"""Get all the measures with that type of sensor, of this year"""
	list_from_database = [] #Simulates the iterator returned by GQLquery
	now = datetime.datetime.now() #Get today's full date
	for counter in range(0,25):		
		x = Censado.Censado() #Gets an instance of Censado class, to simulate a sensor
		
		x.set_Time(now) #One measure per day
		now += datetime.timedelta(days=1)
		x.set_Type(tipo_sensor)
		x.set_Value(round(random.uniform(29,39), 2)) #Simulates 2 decimal random btw 29 to 39
		x.set_LiSANDRA(str(random.randint(1,3)))
		list_from_database.append(x)
	return list_from_database
		
	
def get_today_measures(tipo_sensor):
	"""Get all the sensor measures of the day"""
	now = datetime.datetime.now() #Get today's full date
	year = now.year
	month = now.month
	day = now.day
	low_date_str = '{:0>4}-{:0>2}-{:0>2} 00:00:00'.format(year,month,day) #start of the day
	high_date_str = '{:0>4}-{:0>2}-{:0>2} 23:59:59'.format(year,month,day) #end of the day

	low_date = datetime.datetime.strptime(low_date_str, '%Y-%m-%d %H:%M:%S') #converts the day limits to date
	high_date = datetime.datetime.strptime(high_date_str, '%Y-%m-%d %H:%M:%S')
	return Censado.Censado().view_Date(low_date, high_date, tipo_sensor) #Gets sensor data btw dates, in this case everything from today


def get_this_week_measures(tipo_sensor):
	"""Get all the sensor measures of this week, today - 7 days"""
	now = datetime.datetime.now()#Get today's full date
	end_day = now - datetime.timedelta(days=7) #the day a week ago
	return Censado.Censado().view_Date(now, end_day, tipo_sensor) #Gets the week btw today and 7 days ago

	
def get_this_week_measures(tipo_sensor):
	"""Get all the sensor measures of the month, today - 28 days"""
	now = datetime.datetime.now()#Get today's full date
	end_day = now - datetime.timedelta(days=28) #the day aprox a month ago
	return Censado.Censado().view_Date(now, end_day, tipo_sensor) #Gets the week btw today and 28 days ago
	
def get_measures_between_dates(tipo_sensor, start_date, end_date):
	"""Get all the sensor measures between some dates"""
	#Depends on how the user inputs the dates, probably a jquery calendar, so checking it's output will give the formatting needed

def get_data_between_dates(date_1, date_2, sensor_type):
	"""Funcion para buscar censados entre fechas y tiempos"""
	censados = Censado.all().filter('when >',datetime.datetime(date_1.year, date_1.month, date_1.day, date_1.hour, date_1.minutes)).filter('when <',datetime.datetime(date_2.year, date_2.month, date_2.day, date_2.hour, date_2.minutes)).filter('type =',type).fetch(None)
	return censados
