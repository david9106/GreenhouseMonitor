#funcion encargada de obtener las mediciones RAW de la trama recibida
def obtenerMediciones(serial):
	sensor=[]
	new_sensor={}
	list_sensor=[]
        try:
        	data=serial.split('/')
        	for index in data:
                        sensor.append(index.split(','))
                for counter in range(0,len(sensor)):
                        new_sensor['Tipo']=sensor[counter][0]
                        new_sensor['Valor']=float(sensor[counter][1])
                        new_sensor['Ubicacion']=int(sensor[counter][2])
                        list_sensor.append(dict(new_sensor))
                return list_sensor
        except ValueError as e:
                print(">>error:{%s}".format(e))

def parseID(serial):
        
        new_idBattery={}
        

        data=serial.split(',')
        
        
        new_idBattery['Ubicacion']=data[1]
        new_idBattery['Tipo'] = str(data[0])        
        return  new_idBattery
