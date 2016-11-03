#importar librerias para la comunicacion serial y operaciones para ajustes
import serial
import parser
import conversor
import sendToServer
import sms
#Variable que recibira la trama de datos
data = ''
#Bandera para saber si llego un paquete e imprimirlo
recibido = False
#contador par ael numero de paquete recibido
cnt=0

def compara(data):
        if data[0] == '#':
                #Ejecutar alerta
                print("LLamar alerta !!!")
                return data.replace('#','') 
        return data.replace('+','')
        
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
                        #print(json_dict["Telefono"])
                        #sms.sendMsg(json_dict["Telefono"])
                elif "BateriaOK" in data:
                        print ("-----------------------OK----------")
                        #mostramos la data recibida completa
                        print (data)
                        recibido=False
                        #llamamos la funcion sengMsg del script sms.py
                        alertaID=parser.parseID(data)
                        print (alertaID)
                        json_dict = sendToServer.getconfig(alertaID)
                        
                        data = '' #Vaciar el dato
                else:
                        #data=compara(data)
                        #mostramos el numero de paquete
                        print ("-------------------------------------------")
                        print ("paquete: "+str(cnt))
                        #mostramos la data recibida completa
                        print (data)
                        recibido=False
        		#Llamamos a la funcion encargada de parsear la data recibida
                        lista_sensores=parser.obtenerMediciones(data)
                        #Llamamos a la funcion encargada de convertir la data a las mediciones correctas
                        conversor.ajustarMediciones(lista_sensores)
                        #Llamamos a la funcion encargada de enviar la informacion al servidor
                        #sendToServer.send(lista_sensores)
                        cnt +=1
                        #vaciamos la variable
                        data = ''
