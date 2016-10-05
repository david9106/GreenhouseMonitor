from google.appengine.ext import db


class Censado(db.Model):
	id = db.StringProperty(required=True)
	type = db.StringProperty(required=True)
	value = db.FloatProperty(required=True)
	#when = db.DateTimeProperty(auto_now_add=True)
	when = db.DateTimeProperty(required=True)
	
	def addID(self, id):
		self.id = id
		
	def addType(self, type):
		self.type = type
		
	def addValue(self, value)
		self.value = value
		
	def addTime(self, when)
		self.when = when
		
	def viewDate(self, day, month, year)
		query_str = "SELECT * FROM Censado WHERE when >= DATE(-"+str(year)+",-"+str(month)+",-"+str(day)+")"
		return db.GqlQuery(query_str)
	
	def viewTime(self, hour, minute, second)
		query_str = "SELECT * FROM Censado WHERE when >= DATE(-"+str(hour)+",-"+str(minute)+",-"+str(second)+")"
		return db.GqlQuery(query_str)