## @file conversor.py
# @brief This module is responsible for measure conversion.
# This module is used to convert the measures readed from serial port
# to real value using formuls taken from sensor datasheet.
# 

import math

## @brief The function "ajustarMediciones" receives a dictionary with a list of sensors.
# In a cycle sends every sensor of list to function "ajustar".
# @param "lista_sensores" dictionary with a list of sensors.
# @return None

def ajustarMediciones(lista_sensores):
        for sensor in lista_sensores:
                ajustar(sensor)


## @brief	The function "ajustar" receives a list that represents a sensor structure.
# From each sensor(Temperature,Humidity,Light) get the measure and aplicates a formul (from sensors datasheet)to get the real measure. 
# @param "sensor" array tha rerpresents a sensor structure
# @return None

def ajustar(sensor):
        if sensor['Tipo']=='Temperatura':
                d1 = -39.6  # @var value used to get the real temperature measure
                d2 = 0.01	# @var value used to get the real temperature
                sensor['Valor']= d1+d2*sensor['Valor']
                sensor['Valor'] =format(sensor['Valor'],'.2f')
                 
        if sensor['Tipo']=='Humedad':
                c1 = -2.0468	# @var value used to get the real humidity 
                c2 = 0.0367		# @var value used to get the real humidity 
                c3 = -1.5955e-6	# @var value used to get the real humidity 
                sensor['Valor'] = c1 + c2 * sensor['Valor'] + c3 * math.pow(sensor['Valor'],2)
                sensor['Valor'] =format(sensor['Valor'],'.2f')
                
        if sensor['Tipo']=='Luz':
                sensor['Valor'] = math.exp(3.3/(1024 * 0.56))*sensor['Valor']
                sensor['Valor'] =format(sensor['Valor'],'.2f')
              
        if sensor['Tipo']=='co2':
                sensor['Valor']=format(sensor['Valor'],'.2f')

