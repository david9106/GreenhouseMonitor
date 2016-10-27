from Database import Telefonos

def set_new_userPhone(id,name,phone):
	new_User = Telefonos.UserPhone.get_or_insert(id)
	if new_User == None:
		new_User.set_userID(id)
		new_User.set_userName(name)
		new_User.set_userPhone(phone)
		new_User.save_phone()
	else:
		new_User.set_userID(id)
		new_User.set_userName(name)
		new_User.set_userPhone(phone)
		new_User.save_phone()

def get_phoneNumber(id):
	phone = Telefonos.UserPhone.get_by_key_name(id)
	if phone:
		return phone.user_phone

def get_allPhones():
	phones = Telefonos.UserPhone.all()
	return phones