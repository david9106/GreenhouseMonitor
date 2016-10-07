from google.appengine.ext import db

class Censado(db.Model):
	id_LiSANDRA = db.StringProperty(required=True)
	type = db.StringProperty(required=True)
	value = db.FloatProperty(required=True)
	when = db.DateTimeProperty(required=True)

	def set_LiSANDRA(self, id_LiSANDRA):
	"""Agregar nuevo id de Modulo LiSANDRA """
		try:
			id_LiSANDRA = int(id_LiSANDRA)
			self.id_LiSANDRA = id_LiSANDRA
		except ValueError:
			print("ID de LiSANDRA no permitido")
	
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
			
	#Funcion para guardar en Base de Datos	
	def save_In_DB(self):
		self.put()
		
	def set_Time(self, when):
	""" Agregar Fecha y tiempo en que se realizo la medicion """		
		self.when = when

	def get_All(self):
	"""Funcion que muestra todo lo que esta """
		query_str = "SELECT * FROM Censado"
		return db.GqlQuery(query_str)

	#Funcion para buscar censados entre fechas
	def view_Date(self, type, value, date_1, date_2):
		#query_str = "SELECT * FROM Censado WHERE when >= DATETIME('-"+date_1+"') AND when <= DATETIME('-"+date_2+"')"
		query_str = "SELECT :type, :value FROM Censado WHERE when >= DATETIME(:date_1) AND when <= DATETIME(:date_2)"
		#SELECT * FROM Shout WHERE when >= DATETIME('2013-09-29T09:30:20.00002-08:00') AND when <= DATETIME('2016-09-29T09:30:20.00002-08:00')
		return db.GqlQuery(query_str, type, value, date_1, date_2)
