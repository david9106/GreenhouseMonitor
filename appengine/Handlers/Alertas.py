##@file Alertas.py
#@brief This file describes how to detect when a sensed data is surpassing the limits stablished by the user
import logging
import LimitHandler
from Handlers import PhoneHandler
import json
import webapp2
import sms

##@brief This function get new data and compares it to the limits located in datastore
#@details The function receive data from the gateway and verify if it surpass the limit stablish in datastore, if surpass it the function send a sms alert to all the the user phone numbers enabled to receive the message
#@param data This parameter have a dictionary with the data to compare with the limits in datastore
def compararLimites(data):
	#It represents the state of the limit
	isDisabled=False;
	#It represents the type of sensor unit
	unit =""
	#adjust values from data
	data['Tipo']=str(data['Tipo'])
	data['Valor']=float(data['Valor'])
	data['Ubicacion']=int(data['Ubicacion'])
	#get a phone list from bd
	phoneList=PhoneHandler.get_allEnable_Phones()
	#get max and min values from a type of sensor from bd
	limitMax=LimitHandler.get_Max_Value(data['Tipo'])
	limitMin=LimitHandler.get_min_Value(data['Tipo'])
	
	

	
	
	#adjust the unit based on the type of sensor
	if data['Tipo'] == 'temperatura':
		unit = "grados Centigrados"
	if data['Tipo'] == 'humedad':
		unit = "% humedad relativa"
	if data['Tipo'] == 'luz':
		unit = "luxes"
	if data['Tipo'] == 'co2':
		unit = "ppm"
	logging.info("Telefonos: ")
	for phone in phoneList:
		logging.info(phone.user_phone)
	logging.info("diccionario:")
	logging.info(data)
	logging.info("Limites- Tipo:"+str(type(limitMax))+" "+str(limitMax)+" ,Tipo: "+str(type(limitMin))+" "+str(limitMin))

	#get the state of disabled flag from limit
	isDisabled=LimitHandler.isDisabled(data['Tipo']);
	#logging.info("Temp: "+ data['Tipo']);
	logging.info(isDisabled);
	
	#compare whether the values are not within the established limits
	if data['Valor'] > limitMax and limitMax != None and limitMax != False and isDisabled != False:
		#build a message
		info= "La "+data["Tipo"] +" sobrepaso del limite establecido de "+ str(limitMax)+" "+unit+" Valor actual: "+str(data['Valor'])
		#send message to every phone on phone list
		for phone in phoneList:
			sms.sendMsg(str(phone.user_phone),info)


	if data['Valor'] < limitMin and limitMin != None and limitMin != False and isDisabled != False:
		#build a message
		info= "La "+data["Tipo"] +" esta por debajo del limite establecido de"+ str(limitMin)+" "+unit+" Valor actual: "+str(data['Valor'])
		#send message to every phone on phone list
		for phone in phoneList:
			sms.sendMsg(str(phone.user_phone),info)

	
