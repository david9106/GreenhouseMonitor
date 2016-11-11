##@file LisandraHandler.py
#@brief This file is an interface to cloud datastore to get or register a LiSANDRA module
from Database import Lisandra

##@brief Function that makes an interface with the cloud datastore
#@details Uses the same name function to retrieve the amount of LiSANDRA's
#@return All the LiSANDRA's stored in cloud datastore
def get_number_of_lisandras():
	return Lisandra.LisandraState().get_number_of_lisandras()

##@brief Register a new Lisandra in cloud datastore
#@param id_lisandra: Is the identification for the LiSANDRA module
#@param battery_status: This parameter has the status of the LiSANDRA module battery 
#@param time_stamp: Haves the time stamp of when the LiSANDRA module was register 
def register_lisandra(id_lisandra, battery_status, time_stamp):
	new_lisandra = Lisandra.LisandraState().get_or_insert(id_lisandra)
	new_lisandra.set_batt_status(battery_status)	
	new_lisandra.set_time_stamp(time_stamp)
	new_lisandra.save_state()
