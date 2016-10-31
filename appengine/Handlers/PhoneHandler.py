from DataBase import Telefonos

def set_new_userPhone(id,phone,enabling):
	"""This function is used to create a new user phone number on datastore, if the id passed as argument has an associated phone number
	the function update's the user phone number if not the function create's a new one and store it in datastore,
	as argument the function receive the id of the phone, the name of the user and the phone number
	set_new_userPhone(1,True,6646663377)
	UserPhone:
	id = 1
	phone_enable = True
	phone number = 6646663377"""
	new_User = Telefonos.UserPhone.get_or_insert(id)
	if new_User == None:
		new_User.set_userID(id)
		new_User.set_userPhone(phone)
		new_User.set_enabling(enabling)
		new_User.save_phone()
	else:
		new_User.set_userID(id)
		new_User.set_userPhone(phone)
		new_User.set_enabling(enabling)
		new_User.save_phone()

def get_phoneNumber(id):
	"""This function return's a user phone number stored in datastore, if exist a phone associated to the id passed as argument
	the funtion return the phone number, if not the function return False"""
	phone = Telefonos.UserPhone.get_by_key_name(id)
	if phone:
		return phone.user_phone
	else:
		return False

def get_allPhones():
	"""This function is used to get all the user phone's stored in datastore and return's it in a iterating list"""
	phones = Telefonos.UserPhone.all()
	return phones