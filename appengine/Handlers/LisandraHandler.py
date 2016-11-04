from Database import Lisandra

def get_number_of_lisandras():
	"""
		Just an interface to the DB
		uses the same name function to retrieve the amount of Lisandras
	"""
	return Lisandra.LisandraState().get_number_of_lisandras()

def register_lisandra(id_lisandra, battery_status, time_stamp):
	"""
		Register a new Lisandra to the database
		takes:
			id_lisandra
			battery_status
			time_stamp
		and saves it to the database
	"""
	new_lisandra = Lisandra.LisandraState().get_or_insert(id_lisandra)
	new_lisandra.set_batt_status(battery_status)	
	new_lisandra.set_time_stamp(time_stamp)
	new_lisandra.save_state()
	
