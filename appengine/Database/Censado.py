from google.appengine.ext import db
import datetime

class Censado(db.Model):
	id_LiSANDRA = db.StringProperty()
	type = db.StringProperty()
	value = db.FloatProperty()
	#when = db.DateTimeProperty(auto_now_add=True)
	when = db.DateTimeProperty()


	def set_Time(self, new_date):
		'''Temporal method to add different dates'''
		self.when = new_date

	def set_LiSANDRA(self, id_LiSANDRA):
		"""Agregar nuevo id de Modulo LiSANDRA """
		self.id_LiSANDRA = id_LiSANDRA
	
	def set_Type(self, type):
		""" Agregar tipo de la medicion hecha """		
		try:
			type = str(type)
			self.type = type
		except ValueError:
			print("Tipo de censado no permitido")

	def set_Value(self, value):
		""" Agregar el valor de la medicion realizada"""		
		try:
			value = float(value)
			self.value = value
		except ValueError:
			print("Valor del sensor debe ser flotante")
			
	def save_In_DB(self):
		"""Funcion para guardar en Base de Datos"""
		self.put()
		
	def get_All(self):
		"""Funcion que muestra todo lo que esta """
		query_str = Censado.all()
		return query_str

	def get_data_between_dates(date_1, date_2, type):
		"""Funcion para buscar censados entre fechas y tiempos"""
		censados = Censado.all().filter('when >',datetime.datetime(date_1.year, date_1.month, date_1.day, date_1.hour, date_1.minutes)).filter('when <',datetime.datetime(date_2.year, date_2.month, date_2.day, date_2.hour, date_2.minutes)).filter('type =',type).fetch(None)
		return censados
