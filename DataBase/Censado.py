from google.appengine.ext import db
import datetime

class Censado(db.Model):
	id_LiSANDRA = db.StringProperty(required=True)
	type = db.StringProperty(required=True)
	#value = db.StringProperty(required=True)
	value = db.FloatProperty(required=True)
	when = db.DateTimeProperty(auto_now_add=True)

	def set_LiSANDRA(self, id_LiSANDRA):
	#Agregar nuevo id de Modulo LiSANDRA
		try:
			id_LiSANDRA = str(id_LiSANDRA)
			self.id_LiSANDRA = id_LiSANDRA
		except ValueError:
			print("ID de LiSANDRA no permitido")
	
	def set_Type(self, type):
	#Agregar tipo de la medicion hecha
		try:
			type = str(type)
			self.type = type
		except ValueError:
			print("Tipo de censado no permitido")

	def set_Value(self, value):
	"""Agregar el valor de la medicion realizada"""
		try:
			value = float(value)
			self.value = value
		except ValueError:
			print("Valor del sensor debe ser flotante")
			
	def save_In_DB(self):
	"""Funcion para guardar en Base de Datos"""
		self.put()
		
	def get_All(self):
	"""Funcion que muestra todo lo que esta"""
		query_str = "SELECT * FROM Censado"
		return db.GqlQuery(query_str)

	def get_Data(self, date_1, date_2, type):
		"""Funcion para buscar censados entre fechas y tiempos"""
		return Censado.all().filter('when >',datetime.datetime(date_1.year, date_1.month, date_1.day, date_1.hour, date_1.minutes)).filter('when <',datetime.datetime(date_2.year, date_2.month, date_2.day, date_2.hour, date_2.minutes)).filter('type =',type).fetch(None)
