## @file receptor.py
#This is the main module the raspberry receive all data from Lisradra_reciever via Serial



#importar librerias para la comunicacion serial y operaciones para ajustes
import serial
import parser
import conversor
import sendToServer
import sms

##This variable will receive and save the serial from lisandra
data = ''
##Bool to know if serial data is available
recibido = False
##This count the receive packages
cnt=0
##Dictionary take the Alerta type of the serial package from lisandra
alertaID = {}
##Dictionary that get the respose from the server 
json_dict = {}
##list of sernsor have the sensor type, value, location
lista_sensores = []
##This is init for Serial of Raspberry
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
                if  "BateriaBaja" in data:
                        print ("-----------------------ALERTA----------")
                        #mostramos la data recibida completa
                        print (data)
                        recibido=False
                        #llamamos la funcion sengMsg del script sms.py
                        alertaID=parser.parseID(data)
                        print (alertaID)
                        json_dict = sendToServer.getconfig(alertaID)
                        
                        data = '' #Vaciar el dato
                        
                elif "BateriaOK" in data:
                        print ("-----------------------OK----------")
                        #mostramos la data recibida completa
                        print (data)
                        recibido=False
                        #llamamos la funcion sengMsg del script sms.py
                        alertaID=parser.parseID(data)
                        print (alertaID)
                        json_dict = sendToServer.getconfig(alertaID)
                        print(json_dict)
                        data = '' #Vaciar el dato
                else:
                        
                        #mostramos el numero de paquete
                        print ("-------------------------------------------")
                        print ("paquete: "+str(cnt))
                        #mostramos la data recibida completa
                        print (data)
                        recibido=False
                        try:
                          #Llamamos a la funcion encargada de parsear la data recibida
                          lista_sensores=parser.parserSensorData(data)
                          #Llamamos a la funcion encargada de convertir la data a las mediciones correctas
                          conversor.ajustarMediciones(lista_sensores)
                          #Llamamos a la funcion encargada de enviar la informacion al servidor
                          sendToServer.send(lista_sensores)
                          cnt +=1
                          #vaciamos la variable
                          data = ''
                        except Exception as e:
                          print("DATO ERRONEO")
