from Database import Telefonos

def set_new_userPhone(usr_id,name,phone):
	new_User = Telefonos.UserPhone.get_or_insert(usr_id)
	if new_User == None:
		new_User.set_userID(usr_id)
		new_User.set_userName(name)
		new_User.set_userPhone(phone)
		new_User.save_phone()
	else:
		new_User.set_userID(usr_id)
		new_User.set_userName(name)
		new_User.set_userPhone(phone)
		new_User.save_phone()

def get_phoneNumber(usr_id):
	phone = Telefonos.UserPhone.get_by_key_name(usr_id)
	if phone:
		return phone.user_phone

def get_allPhones():
	phones = Telefonos.UserPhone.all()
	return phones

def isDisabled():
"""Funcion para simular si estan habilitadas o deshabilitadas las alertas"""
	return False