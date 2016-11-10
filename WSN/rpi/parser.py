## @file parser.py
# @brief This module parse the serial data to a list of dictionary or to a normal dictionary.


##@brief This function parse the serial data to a list of dictionary. 
#
# saving the sensor type,value and location in each dictionary.
#
# @param serial Serial data.       
def parserSensorData(serial):
       
        
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
##@brief This function parse the serial data to a dictionary 
#
# saving the sensor type,value and location in each dictionary.
#
# @param serial Serial data.
def parseID(serial):

        

        
        new_idBattery={}
        

        data=serial.split(',')
        
        
        new_idBattery['Ubicacion']=data[1]
        new_idBattery['Tipo'] = str(data[0])        
        return  new_idBattery
