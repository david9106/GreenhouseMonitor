import webapp2
from google.appengine.ext import db

class LisandraState(db.Model):
	"""
	Defines the state of each LiSANDRA module
		ID -> Indicates the LiSANDRAs ID, which could be related to a place in the greenhouse
		Battery (OK | LOW) -> Indicates the last battery level registered for that module
		Timestamp of the last state update -> Indicates the moment when the status was registered
	"""
	id_LiSANDRA = db.StringProperty()
	batt_status = db.StringProperty()
	time_stamp = db.DateTimeProperty()
	
	def set_id(self,new_id):
		self.id_LiSANDRA = str(new_id);
		
	def set_batt_status(self, batt_status):
		self.batt_status = batt_status
	
	def set_time_stamp(self, new_stamp):
		self.time_stamp = new_stamp
		
	def get_time_stamp(self):
		return self.time_stamp
		
	def get_id(self):
		return self.id_LiSANDRA
		
	def get_batt_status(self):
		return self.batt_status
	
	def get_number_of_lisandras(self):
		
		
