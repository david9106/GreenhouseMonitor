from google.appengine.ext import db


class Censado(db.Model):
	id = db.StringProperty(required=True)
	id_LiSANDRA = db.StringProperty(required=True)
	type = db.StringProperty(required=True)
	value = db.FloatProperty(required=True)
	when = db.DateTimeProperty(required=True)
	
	def addID(self, id):
		self.id = id
	def addIDLiSANDRA(self, id_LiSANDRA)
		self.id_LiSANDRA = id_LiSANDRA
	
	def addType(self, type):
		self.type = type
		
	def addValue(self, value)
		self.value = value
		
	def addTime(self, when)
		self.when = when
		
	#Funcion para buscar censados entre fechas	
	def viewDate(self, day, month, year, day_2, month_2, year_2)
		query_str = "SELECT * FROM Censado WHERE when >= DATE(-"+str(year)+",-"+str(month)+",-"+str(day)+")"
		return db.GqlQuery(query_str)
	
	#Funcion para buscar censados en horas
	def viewTime(self, hour, minute, second)
		query_str = "SELECT * FROM Censado WHERE when >= TIME(-"+str(hour)+",-"+str(minute)+",-"+str(second)+")"
		return db.GqlQuery(query_str)