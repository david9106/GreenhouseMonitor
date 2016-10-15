from google.appengine.ext import db
import datetime

from dateutil import parser #Temporal, just for date parsing

class Censado(db.Model):
	id_LiSANDRA = db.StringProperty()
	type = db.StringProperty()
	value = db.FloatProperty()
	#when = db.DateTimeProperty(auto_now_add=True)
	when = db.DateTimeProperty()


	def set_Time(self, new_date):
		'''Temporal method to add dates, if it's not datetime, it tries to convert it'''
		if isinstance(new_date, datetime.datetime):
			self.when = new_date
			return True
		else:
			try:
				self.when = datetime.datetime.strptime(new_date, '%Y-%m-%d %H:%M:%S')
			except ValueError:
				print("Formato de fecha no valido, debe ser datetime o string")
				return False
	
	
	
	def set_LiSANDRA(self, id_LiSANDRA):
		"""Agregar nuevo id de Modulo LiSANDRA """
		try:
			self.id_LiSANDRA = int(id_LiSANDRA)
			return True
		except ValueError:
			print("id_LiSANDRA debe ser ENTERO")
			return False
	
	def set_Type(self, type):
		""" Agregar tipo de la medicion hecha """		
		try:
			type = str(type)
			self.type = type
			return True
		except ValueError:
			print("Tipo de censado no permitido")
			return False

	def set_Value(self, value):
		""" Agregar el valor de la medicion realizada"""		
		try:
			value = float(value)
			self.value = value
			return True
		except ValueError:
			print("Valor del sensor debe ser flotante")
			return False
			
	def save_In_DB(self):
		"""Funcion para guardar en Base de Datos"""
		self.put()
		
	def get_All(self):
		"""Funcion que muestra todo lo que esta """
		query_str = "SELECT * FROM Censado"
		return db.GqlQuery(query_str)

	def get_Data(self, date_1, date_2, type):
		"""Funcion para buscar censados entre fechas y tiempos"""
		return Censado.all().filter('when >',datetime.datetime(date_1.year, date_1.month, date_1.day, date_1.hour, date_1.minutes)).filter('when <',datetime.datetime(date_2.year, date_2.month, date_2.day, date_2.hour, date_2.minutes)).filter('type =',type).fetch(None)
