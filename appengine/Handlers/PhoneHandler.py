from Database import Telefonos

def set_new_userPhone(usr_id,enabling,phone):
	"""This function is used to create a new user phone number on datastore, if the id passed as argument has an associated phone number
	the function update's the user phone number if not the function create's a new one and store it in datastore,
	as argument the function receive the id of the phone, the name of the user and the phone number
	set_new_userPhone(1,True,6646663377)
	UserPhone:
	id = 1
	phone_enable = True
	phone number = 6646663377"""
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

def get_phoneNumber(usr_id):
	phone = Telefonos.UserPhone.get_by_key_name(usr_id)
	if phone:
		return phone.user_phone
	else:
		return False

def get_allEnable_Phones():
	phones = Telefonos.UserPhone.all().filter('phone_enable =', true)
	return phones

def isDisabled():
	"""Funcion para simular si estan habilitadas o deshabilitadas las alertas"""
	return False