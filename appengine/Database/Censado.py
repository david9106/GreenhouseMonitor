from google.appengine.ext import db

class Censado(db.Model):
	#type = db.StringProperty(required=True)
	#value = db.FloatProperty(required=True)
	#id_LiSANDRA = db.StringProperty(required=True)
	#when = db.DateTimeProperty(auto_now_add=True)
	type = db.StringProperty()
	value = db.FloatProperty()
	id_LiSANDRA = db.StringProperty()
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
			
	#Funcion para guardar en Base de Datos	
	def save_In_DB(self):
		self.put()
		
	def get_All(self):
		"""Funcion que muestra todo lo que esta """
		query_str = "SELECT * FROM Censado"
		return db.GqlQuery(query_str)

	#Funcion para buscar censados entre fechas
	def view_Date(self, date_1, date_2, time_1, time_2):
		return db.GqlQuery("SELECT * FROM Censado WHERE when >= DATETIME(':1 :2') AND when < DATETIME(':3 :4'", date_1, date_2, time_1, time_2)
		#return db.GqlQuery("SELECT * FROM Censado WHERE when >= DATE(:1) AND when <= DATE(:2)", date_1, date_2)
		#"SELECT * FROM Shout WHERE when > DATETIME('2016-08-06 15:30:03') AND when < DATETIME('2016-10-06 22:00:00'
