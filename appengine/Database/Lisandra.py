import webapp2
from google.appengine.ext import db

##@class LisandraState
#@brief Defines the state of each LiSANDRA module
class LisandraState(db.Model):
	##@brief Indicates the LiSANDRAs ID, which could be related to a place in the greenhouse
	id_LiSANDRA = db.Key()
	##@brief Indicates the last battery level registered for that module
	batt_status = db.StringProperty()
	##@brief Indicates the moment when the status was registered
	time_stamp = db.DateTimeProperty()
	
	##@brief Used to set the identificator of the LiSANDRA module to register 
	#@param new_id: Haves the identification of the new LiSANDRA module to register 
	def set_id(self,new_id):
		self.id_LiSANDRA = str(new_id)
	
	##@brief This metod puts the status of the battery of the LiSANDRA module
	#@param batt_status: The status of the battery
	def set_batt_status(self, batt_status):
		self.batt_status = batt_status
	
	##@brief This metod set the time when the LiSANDRA module is going to be registered 
	#@param new_stamp: Haves a date time model that marks the time when the LiSANDRA module would be registered
	def set_time_stamp(self, new_stamp):
		self.time_stamp = new_stamp
	
	##@brief Used to get the time when the LiSANDRA was registered 
	def get_time_stamp(self):
		return self.time_stamp
	
	##@brief Gets the id of the LiSANDRA module registered 
	def get_id(self):
		return self.id_LiSANDRA
	
	##@brief Gets the status of the battery of the registered LiSANDRA module
	def get_batt_status(self):
		return self.batt_status
	
	##@brief Used to save in cloud datastore the new LiSANDRA module
	def save_state(self):
		"""
			If there's already a LisandraState object fullfilled
		"""
		self.put()
	
	##@brief Returns the number of all lisandras registered
	#@details It has a count limit of 60 lisandras and if the datastore doesn't respond in 5 seconds it throw's timeout error
	def get_number_of_lisandras(self):
		return LisandraState.all().count(deadline=5, limit=60)
		
