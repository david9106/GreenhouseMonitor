from google.appengine.ext import db

class UserPhone(db.Model):
	user_id = db.Key()
	user_name = db.StringProperty()
	user_phone = db.IntegerProperty()
	
	def set_userID(self, id):
		try:
			self.user_id = str(id)
		except ValueError:
			print("ID no permitido")
	
	def set_userName(self, name):
		try:
			self.user_name = str(name)
		except ValueError:
			print("Nombre no permitido")
		
	def set_userPhone(self, phone):
		try:
			self.user_phone = int(phone)
		except ValueError:
			print("El telefono debe de estar conformado por numeros enteros")
	
	def save_phone(self):
		self.put()