# -*- coding: utf-8 -*-
import webapp2
from BDHandler import *

class CSV_provider(webapp2.RequestHandler):
	def get(self):
		#Algo mas
		sensor_type = self.request.get("sensor_type")
		self.response.headers['Content-Type'] = 'text/csv'
		
		content_disp_str = "attachment; filename="+sensor_type+"_values.csv"
		self.response.headers['Content-Disposition'] = str(content_disp_str)
		
		self.response.write(self.form_csv(sensor_type))
		
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write("Responding with CSV file...")
		
	def form_csv(self,sensor_type):
		this_year_measures = get_this_year_measures(sensor_type)
		csv_string = ','.join(['Tipo_sensor','Valor','Fecha','id-LiSANDRA_(Ubicacion)']) #Title headers
		csv_string+='\n'
		for sensor_entity in this_year_measures:
			csv_string+= ','.join([sensor_entity.type, str(sensor_entity.value), str(sensor_entity.when), str(sensor_entity.id_LiSANDRA)])
			csv_string+='\n'
		return csv_string	

class Graph_display(webapp2.RequestHandler):
	def get(self):
		archivo_html = open('Templates/index.html','r')
		#self.response.write('Main graph page responding...')
		self.response.write(archivo_html.read())
