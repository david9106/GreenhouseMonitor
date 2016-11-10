import webapp2
from Handlers import DBHandler,PhoneHandler,LimitHandler
from Database import Telefonos
import json
import cgi
import sms
import datetime #To hold the first value of the last_db_access var

last_db_access = datetime.datetime(month=1, year=1, day=1) #0001-01-01 00:00:00

class CSV_provider(webapp2.RequestHandler):
	def get(self):
		sensor_type = self.request.get("sensor_type") #Retrieves the "sensor_type" parameter, from get request
		self.response.headers['Content-Type'] = 'text/csv' #Defines kind of data sent
		content_disp_str = "attachment; filename="+sensor_type+"_values.csv" #Adds the name to the file
		self.response.headers['Content-Disposition'] = str(content_disp_str) 
		self.response.write(self.form_csv(sensor_type)) #Send response to the client
		
		
	def form_csv(self,sensor_type):
		"""Extract data from objects and format it as CSV string"""
		this_year_measures = DBHandler.get_this_year_measures(sensor_type)
		csv_string = ','.join(['Tipo_sensor','Valor','Fecha','id-LiSANDRA_(Ubicacion)']) #Title headers
		csv_string+='\n'
		for sensor_entity in this_year_measures:
			csv_string+= ','.join([sensor_entity.type, str(sensor_entity.value), str(sensor_entity.when), str(sensor_entity.id_LiSANDRA)])
			csv_string+='\n'
		return csv_string	
		
		
class JSON_provider(webapp2.RequestHandler):
	def post(self):
		try:
			#Receive the object and decodes it
			jdata = json.JSONDecoder().decode(cgi.escape(self.request.body))
			if "SensorTypes" in jdata["Tipo"]: #!Asks for the available sensor types on database
				
		except (ValueError, TypeError):
			self.error(415) #Using 415 UNSUPPORTED MEDIA TYPE
			self.response.write("Not a JSON object")
			
	def get(self):
		sensor_type = self.request.get("sensor_type")		
		#self.response.headers['Content-Type'] = 'text/json'
		#content_disp_str = "attachment; filename="+sensor_type+"_values.json" #Forms the file
		#self.response.headers['Content-Disposition'] = str(content_disp_str)
		self.response.write(json.dumps(self.form_json(sensor_type)))
		
	def form_json(self, sensor_type):
		"""Extracts data from objects and forms the json like format string"""
		this_year_measures = DBHandler.get_this_year_measures(sensor_type)
		obj_list = []
		for sensor_obj in this_year_measures:
			obj = {}
			obj['Tipo'] = '%s'%(sensor_obj.type)
			obj['Valor'] = '%s'%(sensor_obj.value)
			obj['Ubicacion'] = '%s'%(sensor_obj.id_LiSANDRA)
			obj['Fecha'] = '%s'%(sensor_obj.when.strftime('%Y-%m-%d %H:%M:%S')) #Strip the microseconds part
			obj_list.append(obj)
		return obj_list
		
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
		except (ValueError, TypeError):
			self.error(415) #Using 415 UNSUPPORTED MEDIA TYPE
			self.response.write("Not a JSON object")
			
	def get(self):
		self.response.write("You shouldn't be here...")

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
		
