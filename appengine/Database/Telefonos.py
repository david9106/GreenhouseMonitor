from google.appengine.ext import db

class UserPhone(db.Model):
	user_usr_id = db.Key()
	user_name = db.StringProperty()
	user_phone = db.IntegerProperty()
	
	def set_userID(self, usr_id):
		try:
			self.user_usr_id = str(usr_id)
		except ValueError:
			print("ID no permitusr_ido")
	
	def set_userName(self, name):
		try:
			self.user_name = str(name)
		except ValueError:
			print("Nombre no permitusr_ido")
		
	def set_userPhone(self, phone):
		try:
			self.user_phone = int(phone)
		except ValueError:
			print("El telefono debe de estar conformado por numeros enteros")
	
	def get_userPhone(self):
		"""Returns the entittie's phone"""
		return self.user_phone
	
	def save_phone(self):
		self.put()
