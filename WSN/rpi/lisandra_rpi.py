#importar librerias para la comunicacion serial y operaciones para ajustes
import serial
import math
 
#funcion encargada dee ajustar las mediciones a su valor segun la hoja de especificaciones
def ajustarMediciones(temp,hum,luz):
        #T = d1 + d2 * SOt
        #SOt 14 bit---> d1(C) a 3.5v = -39.7  d2(C) = 0.01
        d1 = -39.7
        d2 = 0.01
        temp = d1+d2*temp
        print temp,
        print " C"

        #RH = c1 + c2 * SOrh + c3 * (SOrh)^2 
        #SOrh 12 bit---> c1 = -2.0468 c2 = 0.0367 c3 = -1.5955E-6
        c1 = -2.0468
        c2 = 0.0367
        c3 = -1.5955e-6
        hum = c1 + c2 * hum + c3 * math.pow(hum,2)
        print hum,
        print " %"
		
        luz = math.exp(3.3/(1024 * 0.56))*luz
        print luz,
        print "luxs"
        print ""


#funcion encargada de obtener las mediciones RAW de la trama recibida
def obtenerMediciones(data):
		#Cortamos la trama recibidad de lisandra por comas
        mediciones=data.split(',')
        #Hacemos cast a INT de las mediciones para poder ajustarlas
        temp=int(mediciones[0])
        hum= int(mediciones[1])
        luz= int(mediciones[2])
        #llamamos a la funcion con los parametros obtenidos arriba
        print "Mediciones ajustadas:"
        ajustarMediciones(temp,hum,luz)
        
#inicializamos puerto serial
comm = serial.Serial("/dev/ttyAMA0",38400,timeout=1)
#Variable que recibira la trama de datos
data = ''
#Bandera para saber si llego un paquete e imprimirlo
recibido = False
#contador par ael numero de paquete recibido
cnt=0
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
                print "paquete: "+str(cnt)
                #mostramos la data recibida completa
                print data
                recibido=False
				#Llamamos a la funcion encargada de obtener las mediciones en base a lo recibido
                obtenerMediciones(data)
                cnt +=1
                #vaciamos la variable
                data = ''


