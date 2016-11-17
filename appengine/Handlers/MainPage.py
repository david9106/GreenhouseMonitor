##@file MainPage.py
#@brief This file handles all the main functions of the application
import webapp2
from Handlers import CensadoHandler,PhoneHandler,LimitHandler
from Database import Telefonos,Limites
import json
import cgi
import sms
import datetime #To calculate summer time, and convert UTC to local UTC+8/+7 TIME
import re #Regular expressions


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
			csv_string+= ','.join([sensor_entity.type, str(sensor_entity.value), str(sensor_entity.when - datetime.timedelta(hours=8)), str(sensor_entity.id_LiSANDRA)])
			csv_string+='\n'
		return csv_string	
		

##@class JSON_provider
#@brief Retrieves data form DB and gives it to user in JSON format
#@details Uses the same command format of the ConfigProvider class.
#A json request with a "Tipo" member that indicates the command and the command arbitrary named, but using CamelCase practice
#No parameters
#It inherits from webapp2.RequestHandler
class JSON_provider(webapp2.RequestHandler):
	##@breif Responds to a POST request that is redirected by URL to this class
	def post(self):
		try:
			#Receive the object and decodes it
			print(cgi.escape(self.request.body))
			jdata = json.JSONDecoder().decode(cgi.escape(self.request.body))
			if "GetSensorTypes" in jdata["Tipo"]: #!Asks for the available sensor types on database
				sensor_types = CensadoHandler.get_available_sensors()
				sensor_list = []
				for sensor in sensor_types:
					sensor_list.append(str(sensor.type))				
				self.response.write(json.dumps(sensor_list))
			elif "GetSensorYearMeasures" in jdata["Tipo"]:			
				year_measures = CensadoHandler.get_year_measures(jdata["SensorType"], jdata["Year"])				
				self.response.write(json.dumps(self.pack_json_sensor_measures(year_measures))) #Responds a json
			elif "GetSensorTodayMeasures" in jdata["Tipo"]:
				today_measures = CensadoHandler.get_today_measures(jdata["SensorType"])
				self.response.write(self.pack_json_sensor_measures(today_measures))
			elif "GetLastMeasure" in jdata["Tipo"]:
				last_measure = CensadoHandler.get_last_value(jdata["SensorType"])
				self.response.write(self.pack_json_sensor_measures(last_measure))
			
		except (ValueError, KeyError):
			'''KeyError goes in case that the json ID doesn't exists, mainly ["Tipo"] but can be others
				ValueError goes in case that the received package is not a correct formatted json
			'''
			self.error(415) #Using 415 UNSUPPORTED MEDIA TYPE
			self.response.write("Not a JSON object")
			
	##@brief Packs a dictionary with the sensor parameters as json excpets
	#@details Uses the ID's "Tipo","Valor","Fecha" and "Ubicacion" to create an json object array
	#In case that it needs to pack just one sensor measures, it doesn't iteates just adds one element to the list with those values
	#@param entity_list is the sensor list from where the values will be extracted
	#@return json_dictionary which is a json object formatted array
	def pack_json_sensor_measures(self,entity_list):
		obj_list = []
		if not hasattr(entity_list, '__iter__'): #Means it's just one Censado entity and won't be iterable			
			local_utc_p8 = self.utc_to_utc8(entity_list.when) #convert to utc+8
			obj = {}
			obj['Tipo'] = '%s'%(entity_list.type)
			obj['Valor'] = '%s'%(entity_list.value)
			obj['Ubicacion'] = '%s'%(entity_list.id_LiSANDRA)
			obj['Fecha'] = '%s'%(local_utc_p8.strftime('%Y-%m-%d %H:%M:%S')) #Strip the microseconds part
			obj_list.append(obj)
		else:
			for sensor_obj in entity_list:
				local_utc_p8 = self.utc_to_utc8(sensor_obj.when) #converts each entity date to utc+8
				obj = {}
				obj['Tipo'] = '%s'%(sensor_obj.type)
				obj['Valor'] = '%s'%(sensor_obj.value)
				obj['Ubicacion'] = '%s'%(sensor_obj.id_LiSANDRA)
				obj['Fecha'] = '%s'%(local_utc_p8.strftime('%Y-%m-%d %H:%M:%S')) #Strip the microseconds part
				obj_list.append(obj)
		return obj_list
		
	##@brief converts utc greenwhich time to local time utc+8, no summer time considered
	#@details Only substracts 8 hours from the date received as param.
	#@param utc_date It's the utc date to be converted
	#@return converted date in datetime format
	def utc_to_utc8(self,utc_date):
		return utc_date - datetime.timedelta(hours=8)
		
##@class Config_provider
#@brief Command interface to get configuration info from the server
#@details It has the following commands:
#'BateriaBaja' records a low batt state of some LiSANDRA module
#'BateriaOK' records a change of battery of some LiSANDRA module
#'Telefonos' asks for the list of saved phones
#'Limites' asks for the current sensor limits alert triggers
#@author Rafael Karosuo
class Config_provider(webapp2.RequestHandler):
	def post(self):
		try:
			#Read json object from cgi safe characters cleaned string
			jdata=json.JSONDecoder().decode(cgi.escape(self.request.body))
			if "BateriaBaja" in jdata["Tipo"]:
				phones = PhoneHandler.get_allEnable_Phones()
				if hasattr(phones,'__iter__'): #if it's more than one phone
					for ite in phones:
						sms.sendMsg(ite.user_phone,"BATERIA BAJA LiSANDRA:"+str(jdata["Ubicacion"]))			
				else:
					sms.sendMsg(phones.user_phone,"BATERIA BAJA LiSANDRA:"+str(jdata["Ubicacion"]))			
			elif "BateriaOK" in jdata["Tipo"]:
				#Guardar en DB el estado de la Lisandra
				jdata["Tipo"] = "Bateria RECIBIDA"
			elif "Telefonos" in jdata["Tipo"]:
				#~ Telefonos.UserPhone().DeleteAll()
				phones = PhoneHandler.get_all_Phones() #Fetches all the phones				
				if not hasattr(phones,'__iter__'): #If it's more than one
					jdata["phone_0"] = str(phones.get_userPhone())	
					jdata["check_phone_0"] = str(phones.isDisable())
				else:
					index = 0 #Phone index
					for phone in phones:
						jdata["phone_{!s}".format(index)] = phone.get_userPhone()						
						jdata["check_phone_{!s}".format(index)] = phone.isDisable()
						index = index +1
						
			elif "Limites" in jdata["Tipo"]:
				#~ Limites.SensorLimits().DeleteAll()
				hum_max = LimitHandler.get_Max_Value("Humedad")
				if hum_max: #Check if exists registered values					
					jdata["hum_max"] = hum_max
				else: #Or put the message
					jdata["hum_max"] = "No value"
					
				hum_min = LimitHandler.get_min_Value("Humedad")
				if hum_min:
					jdata["hum_min"] = hum_min
				else:
					jdata["hum_min"] = "No value"								
				jdata["check_hum"] = LimitHandler.isDisabled("Humedad")
						
				temp_max = LimitHandler.get_Max_Value("Temperatura")
				if temp_max:
					jdata["temp_max"] = temp_max
				else:
					jdata["temp_max"] = "No value"				
					
				temp_min = LimitHandler.get_min_Value("Temperatura")				
				if temp_min:
					jdata["temp_min"] = temp_min
				else:
					jdata["temp_min"] = "No value"
				jdata["check_temp"] = LimitHandler.isDisabled("Temperatura")							
				
				light_max = LimitHandler.get_Max_Value("Iluminacion")
				if light_max:
					jdata["light_max"] = light_max
				else:
					jdata["light_max"] = "No value"					
				
				light_min = LimitHandler.get_min_Value("Iluminacion")					
				if light_min:
					jdata["light_min"] = light_min
				else:
					jdata["light_min"] = "No value"					
				jdata["check_light"] = LimitHandler.isDisabled("Iluminacion")

			print(jdata)
			self.response.write(json.dumps(jdata)) ##Just to check what was received	
		except (ValueError, TypeError, KeyError) as e:
			'''KeyError goes in case that the json ID doesn't exists, mainly ["Tipo"] but can be others'''
			print("Error: {!s}".format(e))
			#self.error(415) #Using 415 UNSUPPORTED MEDIA TYPE
			#self.response.write("Not a JSON object")
			
	def get(self):
		self.response.write("You shouldn't be here...")

##@class Data_Config
#@details This class react's to a URL stablished in app engine, it saves or updates all the user phone numbers and saves or updates all the stablished limits in datastore
class Data_Config(webapp2.RequestHandler):
	def post(self):
		##@brief saves phones and their state
		for index in range(0,10):
			current_phone = self.request.get('phone_{!s}'.format(index))
			if re.match('^\d{10}$',current_phone,re.I) != None: #Check for 10 digit regex as a cell phone number, no case sensitive
				PhoneHandler.set_new_userPhone(str(index),self.request.get('check_phone_'+str(index)),str(current_phone))

		##@brief saves the enabled/disabled limits
		LimitHandler.set_alerts_status("Iluminacion",self.request.get('check_light'))
		LimitHandler.set_alerts_status("Temperatura",self.request.get('check_temp'))
		LimitHandler.set_alerts_status("Humedad",self.request.get('check_hum'))

		##@brief saves the limits
		if re.match('^[0-9]+(\.([0-9]+))*$',self.request.get('light_max')) != None: #Compares with a floating point simple regex
			LimitHandler.set_Max_Alert("Iluminacion",self.request.get('light_max'))	
		
		if re.match('^[0-9]+(\.([0-9]+))*$',self.request.get('light_min')) != None: #Compares with a floating point simple regex
			LimitHandler.set_Min_Alert('Iluminacion',self.request.get('light_min'))

		if re.match('^[0-9]+(\.([0-9]+))*$',self.request.get('temp_max')) != None: #Compares with a floating point simple regex
			LimitHandler.set_Max_Alert('Temperatura',self.request.get('temp_max'))
		
		if re.match('^[0-9]+(\.([0-9]+))*$',self.request.get('temp_min')) != None: #Compares with a floating point simple regex
			LimitHandler.set_Min_Alert('Temperatura',self.request.get('temp_min'))
		
		try:
			max_hum = float(self.request.get('hum_max'))
			if max_hum >= 0.0 and max_hum <= 100.0: #Only saves it if it's within range
				LimitHandler.set_Max_Alert('Humedad',"{!s}".format(max_hum))
		except ValueError as e:
			print("Error: {!s}".format(e))
			
		try:
			min_hum = float(self.request.get('hum_min'))
			if min_hum >= 0.0 and min_hum <= 100.0: #Only saves it if it's within range
				LimitHandler.set_Min_Alert('Humedad',min_hum)
		except ValueError as e:
			print("Error: {!s}".format(e))
		
		
		self.redirect('/Templates/configuracion.html')
		
	
