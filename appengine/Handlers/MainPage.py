##@file MainPage.py
#@brief This file handles all the main functions of the application
import webapp2
from Handlers import CensadoHandler,PhoneHandler,LimitHandler
from Database import Telefonos
import json
import cgi
import sms
import datetime #To hold the first value of the last_db_access var

##@brief Temporal variable, it holds the last DB access, currently not in use
last_db_access = datetime.datetime(month=1, year=1, day=1) #0001-01-01 00:00:00


##@class CSV_provider
#@brief Retrieves current year measuress from DB of specified sensor type and gives it to client in a CSV file
#@details Entity that inherits from webapp2.RequestHandler, it can receive requests and make responses from/to a client via HTTP
#Uses a GET parameter sensor_type to know which sensor type to fetch from DB and only gets current year measures
#No parameters
#In this case is used only it's "get" method which responds to a GET request
class CSV_provider(webapp2.RequestHandler):
	def get(self):
		sensor_type = self.request.get("sensor_type") #Retrieves the "sensor_type" parameter, from get request
		self.response.headers['Content-Type'] = 'text/csv' #Defines kind of data sent
		content_disp_str = "attachment; filename="+sensor_type+"_values.csv" #Adds the name to the file
		self.response.headers['Content-Disposition'] = str(content_disp_str) 
		self.response.write(self.form_csv(sensor_type)) #Send response to the client
		
		
	def form_csv(self,sensor_type):
		"""Extract data from objects and format it as CSV string"""
		this_year_measures = CensadoHandler.get_this_year_measures(sensor_type)
		csv_string = ','.join(['Tipo_sensor','Valor','Fecha','id-LiSANDRA_(Ubicacion)']) #Title headers
		csv_string+='\n'
		for sensor_entity in this_year_measures:
			csv_string+= ','.join([sensor_entity.type, str(sensor_entity.value), str(sensor_entity.when), str(sensor_entity.id_LiSANDRA)])
			csv_string+='\n'
		return csv_string	
		

##@class JSON_provider
#@brief Retrieves data form DB and gives it to user in JSON format
#@details Uses the same command format of the ConfigProvider class.
#A json request with a "Tipo" member that indicates the command and the command arbitrary named, but using CamelCase practice
#No parameters
#It inherits from webapp2.RequestHandler
class JSON_provider(webapp2.RequestHandler):
	def post(self):
		"""
			Responds to a POST request that is redirected by URL to this class
		"""
		try:
			#Receive the object and decodes it
			jdata = json.JSONDecoder().decode(cgi.escape(self.request.body))
			if "GetSensorTypes" in jdata["Tipo"]: #!Asks for the available sensor types on database
				sensor_types = CensadoHandler.get_available_sensors()
				sensor_list = []
				for sensor in sensor_types:
					sensor_list.append(str(sensor.type))				
				self.response.write(json.dumps(sensor_list))
			elif "GetSensorYearMeasures" in jdata["Tipo"]:			
				year_measures = CensadoHandler.get_year_measures(jdata["SensorType"], jdata["Year"])
				obj_list = []
				for sensor_obj in year_measures:
					obj = {}
					obj['Tipo'] = '%s'%(sensor_obj.type)
					obj['Valor'] = '%s'%(sensor_obj.value)
					obj['Ubicacion'] = '%s'%(sensor_obj.id_LiSANDRA)
					obj['Fecha'] = '%s'%(sensor_obj.when.strftime('%Y-%m-%d %H:%M:%S')) #Strip the microseconds part
					obj_list.append(obj)
				self.response.write(json.dumps(obj_list)) #Responds a json
			elif "GetSensorTodayMeasures" in jdata["Tipo"]:
				today_measures = CensadoHandler.get_today_measures(jdata["SensorType"])
				obj_list = []
				for sensor_obj in today_measures:
					obj_list
			
		except (KeyError):
			'''KeyError goes in case that the json ID doesn't exists, mainly ["Tipo"] but can be others'''
			self.error(415) #Using 415 UNSUPPORTED MEDIA TYPE
			self.response.write("Not a JSON object")
			
		##@brief Packs a dictionary with the sensor parameters as json excpets
		#@details Uses the ID's "Tipo","Valor","Fecha" and "Ubicacion" to create an json object array
		#@param entity_list is the sensor list from where the values will be extracted
		#@return json_dictionary which is a json object formatted array
		def pack_json_sensor_measures(entity_list):
			obj_list = []
			for sensor_obj in ent
			
class Config_provider(webapp2.RequestHandler):
	def post(self):
		try:
			#Read json object from cgi safe characters cleaned string
			jdata=json.JSONDecoder().decode(cgi.escape(self.request.body))
			if "BateriaBaja" in jdata["Tipo"]:
				phones = PhoneHandler.get_allEnable_Phones()
				for ite in phones:
					sms.sendMsg(ite.user_phone,"BATERIA BAJA LiSANDRA:"+str(jdata["Ubicacion"]))			
				#self.response.write(json.dumps(jdata))
			elif "BateriaOK" in jdata["Tipo"]:
				#Guardar en DB el estado de la Lisandra
				jdata["Tipo"] = "Bateria RECIBIDA"
			elif "Telefonos" in jdata["Tipo"]:
				pass
			elif "Limites" in jdata["Tipo"]:
				jdata["MaxHumedad"] = LimitHandler.get_Max_Value("Humedad")
				jdata["MinHumedad"] = LimitHandler.get_min_Value("Humedad")
				
				jdata["MaxTemperatura"] = LimitHandler.get_Max_Value("Temperatura")
				jdata["MinTemperatura"] = LimitHandler.get_min_Value("Temperatura")
				
				jdata["MaxIluminacion"] = LimitHandler.get_Max_Value("Iluminacion")
				jdata["MinIluminacion"] = LimitHandler.get_min_Value("Iluminacion")

			self.response.write(json.dumps(jdata)) ##Just to check what was received	
		except (ValueError, TypeError, KeyError):
			'''KeyError goes in case that the json ID doesn't exists, mainly ["Tipo"] but can be others'''
			self.error(415) #Using 415 UNSUPPORTED MEDIA TYPE
			self.response.write("Not a JSON object")
			
	def get(self):
		self.response.write("You shouldn't be here...")

##@class Data_Config
#@details This class react's to a URL stablished in app engine, it saves or updates all the user phone numbers and saves or updates all the stablished limits in datastore
class Data_Config(webapp2.RequestHandler):
	def post(self):
		for ite in range(0, 10):
			phone = PhoneHandler.set_new_userPhone(str(ite),self.request.get('check_phone_'+str(ite)),self.request.get('phone_'+str(ite)))
		

		light = LimitHandler.set_Max_Alert("Luz",self.request.get('light_max'))
		light_2 = LimitHandler.set_Min_Alert('Luz',self.request.get('light_min'))
		
		temp = LimitHandler.set_Max_Alert('Temperatura',self.request.get('temp_max'))
		temp_2 = LimitHandler.set_Min_Alert('Temperatura',self.request.get('temp_min'))
		
		hum = LimitHandler.set_Max_Alert('Humedad',self.request.get('hum_max'))
		hum_2 = LimitHandler.set_Min_Alert('Humedad',self.request.get('hum_min'))
		
		self.redirect('/Templates/configuracion.html')
		
