#importar librerias para la comunicacion serial y operaciones para ajustes
import serial
import math
import json
import write
import time
import sendToServer

#Variable que recibira la trama de datos
data = ''
#Bandera para saber si llego un paquete e imprimirlo
recibido = False
#contador par ael numero de paquete recibido
cnt=0

#funcion encargada dee ajustar las mediciones a su valor segun la hoja de especificaciones
def ajustarMediciones(temp,hum,luz,co2):
#T = d1 + d2 * SOt
#SOt 14 bit---> d1(C) a 3 = -39.6  d2(C) = 0.01
	sensores = {}
	d1 = -39.6
	d2 = 0.01
	temp = d1+d2*temp
	print ("Temp: "),
	print ("%.2f" % temp),
	print (" C "),

	#RH = c1 + c2 * SOrh + c3 * (SOrh)^2 
	#SOrh 12 bit---> c1 = -2.0468 c2 = 0.0367 c3 = -1.5955E-6
	c1 = -2.0468
	c2 = 0.0367
	c3 = -1.5955e-6
	hum = c1 + c2 * hum + c3 * math.pow(hum,2)
	print ("Hum: "),
	print ("%.2f" % hum),
	print (" % "),
		
	luz = math.exp(3.3/(1024 * 0.56))*luz
	print ("Luz: "),
	print ("%.2f" % luz),
	print "luxs ",

	print ("CO2: "),
	print ("%.2f" % co2 ),
	print (" PPM ")

	temp=format(temp,'.2f')
	hum=format(hum,'.2f')
	luz=format(luz,'.2f')
	co2=format(co2,'.2f')

	#Lineas encargadas de escribir en el archivo measures.txt
	toWrite = str(temp)+" , "+str(hum)+" , "+str(luz)+" , "+str(co2)
	write.write(toWrite)
	
	#Codigo encargado de enviar los datos al servidor
	fecha = time.strftime('%d %b %y')
	hora = time.strftime('%H:%M:%S')
	sensores = {"temperatura":temp,"humedad":hum,"luz":luz,"CO2":co2,"fecha":fecha,"hora":hora} 
	sendToServer.sendJson(sensores)

#funcion encargada de obtener las mediciones RAW de la trama recibida
def obtenerMediciones(data):
	#Cortamos la trama recibidad de lisandra por comas
	mediciones=data.split(',')
	#Hacemos cast a INT de las mediciones para poder ajustarlas
	temp=int(mediciones[0])
	hum= int(mediciones[1])
	luz= int(mediciones[2])
	co2= int(mediciones[3])
	#llamamos a la funcion con los parametros obtenidos arriba
	print "Mediciones ajustadas:"
	ajustarMediciones(temp,hum,luz,co2)
        
#inicializamos puerto serial
comm = serial.Serial("/dev/ttyAMA0",38400,timeout=1)
print "Reading..."
#Ciclo principal
while True:
        #Verificamos si hay datos en el buffer de entrada del serial
        while comm.inWaiting() >0:
				#De haberlos se lee hasta que se encuentre un  fin de linea
                data = comm.readline()
                recibido=True
        if recibido:
                #mostramos el numero de paquete
                print ("-------------------------------------------")
                print ("paquete: "+str(cnt))
                #mostramos la data recibida completa
                print (data)
                recibido=False
				#Llamamos a la funcion encargada de obtener las mediciones en base a lo recibido
                obtenerMediciones(data)
                cnt +=1
                #vaciamos la variable
                data = ''