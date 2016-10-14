import webapp2
from Handlers import BDHandler
import json

class CSV_provider(webapp2.RequestHandler):
	def get(self):
		sensor_type = self.request.get("sensor_type") #Retrieves the "sensor_type" parameter, from get request
		self.response.headers['Content-Type'] = 'text/csv' #Defines kind of data sent
		content_disp_str = "attachment; filename="+sensor_type+"_values.csv" #Adds the name to the file
		self.response.headers['Content-Disposition'] = str(content_disp_str) 
		self.response.write(self.form_csv(sensor_type)) #Send response to the client
		
		
	def form_csv(self,sensor_type):
		"""Extract data from objects and format it as CSV string"""
		this_year_measures = get_this_year_measures(sensor_type)
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
		this_year_measures = get_this_year_measures(sensor_type)
		obj_list = []
		for sensor_obj in this_year_measures:
			obj = {}
			obj['Tipo'] = '%s'%(sensor_obj.type)
			obj['Valor'] = '%s'%(sensor_obj.value)
			obj['Ubicacion'] = '%s'%(sensor_obj.id_LiSANDRA)
			obj['Fecha'] = '%s'%(sensor_obj.when)
			obj_list.append(obj)
		return obj_list
		

class Graph_display(webapp2.RequestHandler):
	def get(self):
		archivo_html = open('Templates/index.html','r')
		self.response.write(archivo_html.read())
