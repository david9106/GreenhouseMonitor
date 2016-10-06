from google.appengine.ext import db

class Censado(db.Model):
	id = db.StringProperty(required=True)
	id_LiSANDRA = db.StringProperty(required=True)
	type = db.StringProperty(required=True)
	value = db.FloatProperty(required=True)
	when = db.DateTimeProperty(required=True)
	
	""" Agregar nuevo id de sensor """
	def set_ID(self, id):
		try:
			id = str(id)
			self.id = id
		except ValueError:
			print("No es un ID permitido")

	"""Agregar nuevo id de Modulo LiSANDRA """
	def set_LiSANDRA(self, id_LiSANDRA):
		try:
			id_LiSANDRA = int(id_LiSANDRA)
			self.id_LiSANDRA = id_LiSANDRA
		except ValueError:
			print("ID de LiSANDRA no permitido")
	
	""" Agregar tipo de la medicion hecha """
	def set_Type(self, type):
		try:
			type = str(type)
			self.type = type
		except ValueError:
			print("Tipo de censado no permitido")

	""" Agregar el valor de la medicion realizada"""
	def set_Value(self, value):
		try:
			value = float(value)
			self.value = value
		except ValueError:
			print("Valor del sensor debe ser flotante")
			
	#Funcion para guardar en Base de Datos	
	def set_In_DB(self):
		self.put()
	""" Agregar Fecha y tiempo en que se realizo la medicion """
	def set_Time(self, when):
		self.when = when
		self.put()

	"""Funcion que muestra todo lo que esta """
	def All(self):
		query_str = "SELECT * FROM Eventos"
		return db.GqlQuery(query_str)

	#Funcion para buscar censados entre fechas
	def view_Date(self, date_1, date_2):
		query_str = "SELECT * FROM Censado WHERE when >= DATETIME('-"+date_1+"') AND when <= DATETIME('-"+date_2+"')"
		#SELECT * FROM Shout WHERE when >= DATETIME('2013-09-29T09:30:20.00002-08:00') AND when <= DATETIME('2016-09-29T09:30:20.00002-08:00')
		return db.GqlQuery(query_str)
