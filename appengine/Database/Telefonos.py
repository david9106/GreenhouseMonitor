##@file Telefonos.py
#@brief This file describes the model of a phone number stored in datastore
from google.appengine.ext import db

##@class UserPhone
#@brief An entity that haves all the properties needed to register user phone number
class UserPhone(db.Model):
	##@brief It have's the identification of the user phone number, it's based on the HTML tag where the phone will go
	user_id = db.Key()
	##@brief It contains the phone number
	user_phone = db.StringProperty()
	##@brief Indicates if the phone is receiving sms alerts
	phone_enable = db.BooleanProperty()
	
	##@brief This function help us to set the user id on the UserPhone class model
	#@param usr_id: Haves the id of the user phone number
	def set_userID(self, usr_id):
		try:
			self.user_id = str(usr_id)
		except ValueError:
			print("ID no permitido")
	
	##@brief This function set the phone number on the user phone model
	#@param phone: Is a string with the phone number of the user
	def set_userPhone(self, phone):
		try:
			self.user_phone = str(phone)
		except ValueError:
			print("El telefono debe de estar conformado por numeros")

	##@brief Enables or disables the receiving of the limit value alerts
	#@details Function used to eneble or disable the receiving permition of messages from the app to the user phone
	#@param enabling_prop: A boolean that marks if is enable or disable the take of alerts of the phone registered phone number
	def enable_alerts(self,enabling_prop):
		try:
			self.phone_enable = bool(enabling_prop)
		except ValueError:
			print("No boolean property received")
	
	##@brief Returns the entity phone number
	def get_userPhone(self):
		return self.user_phone
	
	##@brief This function save's or update in datastore the created user phone
	def save_phone(self):
		self.put()

	##@brief Check if alerts are disable for this phone
	def isDisable(self):
		return self.phone_enable
		
	##@brief ALERT!! Deletes all the UserPhone database
	#@details Must be used with extreme precausion since there's no roll back
	def DeleteAll(self):
		query_str = "SELECT * FROM UserPhone"
		db.delete(db.GqlQuery(query_str))
		
