from google.appengine.ext import db

class UserPhone(db.Model):
	"""Class UserPhone has the next attributes
	user_id: it have's the identification of the user phone number
	user_name: it contains the name of the user
	user_phone: this attribute have's the phone number of the user"""
	user_id = db.Key()
	user_name = db.StringProperty()
	user_phone = db.IntegerProperty()
	
	def set_userID(self, id):
		"""This function help us to set the user id on the UserPhone class model the function receive the id of the user as argument"""
		try:
			self.user_id = str(id)
		except ValueError:
			print("ID no permitido")
	
	def set_userName(self, name):
		"""This function put the name of the user phone
		the function receive the name of the user as argument"""
		try:
			self.user_name = str(name)
		except ValueError:
			print("Nombre no permitido")
		
	def set_userPhone(self, phone):
		"""This function put's the phone number on the user phone model
		the function reveive the phone number of the user as argument"""
		try:
			self.user_phone = int(phone)
		except ValueError:
			print("El telefono debe de estar conformado por numeros enteros")
	
	def save_phone(self):
		"""This function save's or update in datastore the created user phone"""
		self.put()