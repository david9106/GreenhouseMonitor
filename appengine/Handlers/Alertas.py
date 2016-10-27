import LimitHandler
from Handlers import PhoneHandler
import json
import webapp2
import sms

#It represents the type of sensor unit
unit =""

#function receives a dictionary
def compararLimites(data):
	#get a phone list from bd
	phoneList=PhoneHandler.get_allPhones()
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
	
	#compare whether the values are not within the established limits
	if data['Valor'] > limitMax:
		#build a message
		info= "La "+data["Tipo"] +" sobrepaso el limite establecido de "+ str(limitMax)+" "+unit
		#send message to every phone on phone list
		for phone in phoneList:
			sms.sendMsg(str(phone.user_phone),info)

	
	if data['Valor'] < limitMin:
		#build a message
		info= "La "+data["Tipo"] +" esta por debajo el limite establecido de"+ str(limitMin)+" "+unit
		#send message to every phone on phone list
		for phone in phoneList:
			sms.sendMsg(str(phone.user_phone),info)

	
