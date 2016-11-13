##@file PhoneHandler.py
#@brief This module is an interface to cloud datastore to register a user phone number
from Database import Telefonos

##@brief Create's a new user phone number and store it in datastore
#@details This function is used to create a new user phone number on datastore, if the id passed as argument has an associated phone number the function update's the user phone number if not the function create's a new one and store it in datastore
#@param user_id: has the id of the user
#@param enabling: It's a boolean parameter that indicates if the phone is enable to receive sms alerts 
#@param phone: Is a string that have the user phone number
def set_new_userPhone(usr_id,enabling,phone):
	new_User = Telefonos.UserPhone.get_or_insert(usr_id)
	if new_User == None:
		new_User.set_userID(usr_id)
		new_User.set_userPhone(phone)
		new_User.enable_alerts(enabling)
		new_User.save_phone()
	else:
		new_User.set_userID(usr_id)
		new_User.set_userPhone(phone)
		new_User.enable_alerts(enabling)
		new_User.save_phone()

##@brief This function get a phone number of the datastore
#@details The function search the phone number using his id, once the number is getted the function return it
#@param usr_id: The user id related to the phone number
#@return The phone number is returned if excist, if not the function return False
def get_phoneNumber(usr_id):
	phone = Telefonos.UserPhone.get_by_key_name(usr_id)
	if phone:
		return phone.user_phone
	else:
		return False

##@brief Used to return a list of all the enabled user's phones
#@details This function get and return all the enabled phone number's stored in the cloud datastore
#@return The list of phone number's stored in cloud datastore
def get_allEnable_Phones():
	phones = Telefonos.UserPhone.all().filter('phone_enable =', True)
	return phones

##@brief Used to return a list of all user phones
#@details This function get and return all phone number's stored in the cloud datastore
#@return The list of phone number's stored in cloud datastores	
def get_all_Phones():
	phones = Telefonos.UserPhone.all()
	return phones
	
##@brief Searches for a phone_id and get's it's alert status
#@return the boolean status for this phone
def get_phone_alert_status(phone_id):
	return Telefonos.UserPhone().get_user_phone_by_id(phone_id).is_Disable()
