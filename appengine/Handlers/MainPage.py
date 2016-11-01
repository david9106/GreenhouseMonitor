import webapp2
from Handlers import BDHandler
import json
import cgi

class CSV_provider(webapp2.RequestHandler):
	def get(self):
		sensor_type = self.request.get("sensor_type") #Retrieves the "sensor_type" parameter, from get request
		self.response.headers['Content-Type'] = 'text/csv' #Defines kind of data sent
		content_disp_str = "attachment; filename="+sensor_type+"_values.csv" #Adds the name to the file
		self.response.headers['Content-Disposition'] = str(content_disp_str) 
		self.response.write(self.form_csv(sensor_type)) #Send response to the client
		
		
	def form_csv(self,sensor_type):
		"""Extract data from objects and format it as CSV string"""
		this_year_measures = BDHandler.get_this_year_measures(sensor_type)
		csv_string = ','.join(['Tipo_sensor','Valor','Fecha','id-LiSANDRA_(Ubicacion)']) #Title headers
		csv_string+='\n'
		for sensor_entity in this_year_measures:
			csv_string+= ','.join([sensor_entity.type, str(sensor_entity.value), str(sensor_entity.when), str(sensor_entity.id_LiSANDRA)])
			csv_string+='\n'
		return csv_string	
		
		
class JSON_provider(webapp2.RequestHandler):
	def get(self):
		sensor_type = self.request.get("sensor_type")		
		#self.response.headers['Content-Type'] = 'text/json'
		#content_disp_str = "attachment; filename="+sensor_type+"_values.json" #Forms the file
		#self.response.headers['Content-Disposition'] = str(content_disp_str)
		self.response.write(json.dumps(self.form_json(sensor_type)))
		
	def form_json(self, sensor_type):
		"""Extracts data from objects and forms the json like format string"""
		this_year_measures = BDHandler.get_this_year_measures(sensor_type)
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
			jdata = json.JSONDecoder().decode(cgi.escape(self.request.body))
			
			#Updates the current configured phone number on DB
			jdata["Telefono"] = '6645380095'
			
			#Answers it to client
			self.response.write(json.dumps(jdata))
		except (ValueError, TypeError):
			self.error(415) #Using 415 UNSUPPORTED MEDIA TYPE
			self.response.write("Not a JSON object")
			
	def get(self):
		self.response.write("You shouldn't be here...")

class Phone_Config(webapp2.RequestHandler):
	def post(self):
		#phone = PhoneHandler.set_new_userPhone('1',self.request.get('check_phone_0'),self.request.get('phone_0'))
		self.response.write(self.request.get('phone_0'))
	