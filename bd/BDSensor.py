import datatime

class Sensor(db.Model):
	tipo_sensor = db.StringProperty()
	medicion = db.FloatProperty()
	tiempo = db.DataTimeProperty()
	ID = db.StringProperty()
	
def find_By_Id(self,identificador)
	return db.Model.get(identificador)
	
def All(self)
	query_str = "SELECT * FROM Eventos"
    return db.GqlQuery(query_str)
