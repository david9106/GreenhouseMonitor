#include "LiSANDRA.h"
#define LOCAL_ADDR  0x15
#define DEST_ADDR   0x20
#define NETKEY      {0xc0,0xd1,0xce}

uint16_t luz;
uint16_t temp;
uint16_t hum;
uint16_t co2;
uint8_t c=',';
RadioLT_DataPkt_t mypkt;


void setup() {
  uint8_t net[3]=NETKEY;   
	/*Inicializamos la comunicacion serial*/
    Serial.begin(38400);
	/*Inicializamos los leds*/
    LEDs_Ini();    
	/*Inicializamos el sensor de luz*/
    LightSensor_Ini(); 
	/*Inicializamos el sensor de humedad y temperatura*/
    HTsensor_Ini();
	/*Inicializamos el modulo RF*/
    RadioLT_NetIni( net, LOCAL_ADDR, DEST_ADDR );  
    RadioLT_Ini(); 
	
	/*Encendemos led (solo para saber si esta funcionando)*/
	LEDs_Grn_On(); 
}


void loop() {
  /*Esperamos a recibir un paquete*/
 if( RadioLT_AvailablePkt() > 0 ){
     /*Obtenemos el paquete*/
           RadioLT_GetPkt( &mypkt );
           
     String str(mypkt.data);
     if(str.length()<5){
           Serial.println(mypkt.data);
           
         
     }
     else{
		   
		   /*Se envia al raspberry*/
           
           enviarSerieRPI(mypkt.data);
		   /*blink de recibido*/
           LEDs_Ylw_On();
           delay(5);
           LEDs_Ylw_Off();
     }
  }

}

/*Esta funcion se encarga de descomponer la trama recibida
en valores  enteros (16 bits ,2 bytes) para ser enviado a la rpi */
  void enviarSerieRPI(char * trama){
    uint8_t i=0;
    
      for(i=0;i<4;i++){
        switch(i){
			//Se obtiene  el byte alto (Nota: la trama lleva byte alto ,byte bajo,byte alto .....)
			//de la trama y se le hace un cast a 8bits para pasarlo a ala variable que representara ese datos
			//posteriormente se recorre 8bits esa misma variable para dejar libre los primeros 8 bits 
			// y asignarlo el byte bajo.
          case 0:
		  //byte alto
            temp=trama[i];
            temp=temp<<8;
			//byte bajo
            temp|= ((uint8_t)(trama[i+1]) );
            break;
          case 1:
            hum=trama[i+1];
            hum=hum<<8;
            hum|= ((uint8_t)(trama[i+2]));
            break;
          case 2:
            luz=trama[i+2];
            luz=luz<<8;
            luz|= ( (uint8_t)(trama[i+3]));
            break;

          case 3:
            co2=trama[i+3];
            co2=co2<<8;
            co2|= ( (uint8_t)(trama[i+4]));
            break;
          }
      }

			//Se envia los datos a la raspberry como valores enteros y no como bytes
			//ademas se incluye una coma entre cada valor para poder trabajarlos en la rpi
            
            Serial.print(temp);
            Serial.print(",");
            Serial.print(hum);
            Serial.print(",");
            Serial.print(luz);
            Serial.print(",");
            Serial.println(co2);
            

}


