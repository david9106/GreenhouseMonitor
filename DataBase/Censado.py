from google.appengine.ext import db

class Censado(db.Model):
	id_LiSANDRA = db.StringProperty(required=True)
	type = db.StringProperty(required=True)
	value = db.FloatProperty(required=True)
	when = db.DateTimeProperty(auto_nos_add=True)

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
		
	def get_All(self):
	"""Funcion que muestra todo lo que esta """
		query_str = "SELECT * FROM Censado"
		return db.GqlQuery(query_str)

	#Funcion para buscar censados entre fechas
	def view_Date(self, date_1, date_2):
		return db.GqlQuery("SELECT * FROM Censado WHERE when >= DATE(:1) AND when <= DATE(:2)", date_1, date_2)
	
	#Funcion para buscar censados entre tiempo	
	def view_Time(self, date_1, time_1, time_2):
		return(db.GqlQuery("SELECT * FROM Censado WHERE when < DATETIME(':1 :2') AND when > DATETIME(':3 :4')"),date_1, time_1, date_1, time_2)
