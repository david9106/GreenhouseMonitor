from google.appengine.ext import db


class Censado(db.Model):
	id = db.StringProperty(required=True)
	grados = db.FloatProperty(required=True)
	luxes = db.FloatProperty(required=True)
	humedad = db.FloatProperty(required=True)
	#when = db.DateTimeProperty(auto_now_add=True)
	when = db.DateTimeProperty
	
	def addID(self, id):
		self.id = id
		
	def addLuxes(self, luxes):
		self.luxes = luxes
		
	def addGrados(self, grados)
		self.grados = grados
		
	def addHumedad(self, humedad)
		self.humedad = humedad
		
	def addTime(self, when)
		self.when = when
	
	
	
