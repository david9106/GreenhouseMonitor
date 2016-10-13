from google.appengine.ext import db
import datetime

class Shout(db.Model):
	message = db.StringProperty(required=True)
	when = db.DateTimeProperty(auto_now_add=True)
	
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
	#Agregar el valor de la medicion realizada
		try:
			value = float(value)
			self.value = value
		except ValueError:
			print("Valor del sensor debe ser flotante")
			
	#Funcion para guardar en Base de Datos	
	def save_In_DB(self):
		self.put()
		
	def get_All(self):
	#Funcion que muestra todo lo que esta
		query_str = "SELECT * FROM Censado"
		return db.GqlQuery(query_str)

	#Funcion para buscar censados entre fechas y tiempos
	def view_Date(self, year, month, day, month_2, day_2, hr, min, hr_2, min_2, type):
		return Censado.all().filter('when >',datetime.datetime(year,month,day)).filter('when <',datetime.datetime(year,month_2,day_2)).filter('type =',type).fetch(None)
