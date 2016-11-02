from google.appengine.ext import db

class UserPhone(db.Model):
	"""Class UserPhone has the next attributes
	user_id: it have's the identification of the user phone number
	user_name: it contains the name of the user
	user_phone: this attribute have's the phone number of the user
	"""
	user_id = db.Key()
	user_phone = db.StringProperty()
	phone_enable = db.BooleanProperty()
	
	def set_userID(self, usr_id):
		"""This function help us to set the user id on the UserPhone class model
		the function receive the id of the user as argument"""
		try:
			self.user_id = str(usr_id)
		except ValueError:
			print("ID no permitido")

	def set_userPhone(self, phone):
		"""This function put's the phone number on the user phone model
		the function reveive the phone number of the user as argument"""
		try:
			self.user_phone = str(phone)
		except ValueError:
			print("El telefono debe de estar conformado por numeros")

	def enable_alerts(self,enabling_prop):
		"""Function used to eneble or disable the receiving permition of messages from the app to the user phone"""
		try:
			self.phone_enable = bool(enabling_prop)
		except ValueError:
			print("No boolean property received")
	
	def get_userPhone(self):
		"""Returns the entittie's phone"""
		return self.user_phone
	
	def save_phone(self):
		"""This function save's or update in datastore the created user phone"""
		self.put()

	def isDisable():
		"""Check if alerts are disable for this phone"""
		return False