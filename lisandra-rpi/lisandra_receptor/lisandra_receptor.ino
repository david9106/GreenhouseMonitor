#include "LiSANDRA.h"


#define LOCAL_ADDR  0x15
#define DEST_ADDR   0x20
#define NETKEY      {0xc0,0xd1,0xce}

uint16_t luz;
uint16_t temp;
uint16_t hum;
uint8_t c=',';
RadioLT_DataPkt_t mypkt;


void setup() {
  
  uint8_t net[3]=NETKEY;   
    Serial.begin(38400);
    LEDs_Ini();    
    LightSensor_Ini(); 
    LEDs_Grn_On(); 
    HTsensor_Ini();
    RadioLT_NetIni( net, LOCAL_ADDR, DEST_ADDR );  
    RadioLT_Ini(); 

}


void loop() {
  
 if( RadioLT_AvailablePkt() > 0 ){
           RadioLT_GetPkt( &mypkt );
         
           /*Enviar trama a la RPI via serie*/
          enviarSerieRPI(mypkt.data);
         /* for(int i=0; i<8; i++){
            Serial.print((uint8_t )(mypkt.data[i]),HEX);
            Serial.print(':');
          }
          Serial.println();*/
          //Serial.print(mypkt.data);
           LEDs_Ylw_On();
           delay(5);
           LEDs_Ylw_Off();
       }

}

//Esta funcion se encarga de descomponer la trama recibida
//en valores  enteros (16 bits ,2 bytes)
  void enviarSerieRPI(char * trama){
  
    uint16_t temp=0;
    uint16_t hum=0;
    uint16_t luz=0;
    uint8_t i=0;
    
      for(i=0;i<3;i++){
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
          }
      }

			//Se envia los datos a la raspberry como valores enteros y no como bytes
			//ademas se incluye una coma entre cada valor para poder trabajarlos en la rpi
            
            Serial.print(temp);
            Serial.print(",");
            Serial.print(hum);
            Serial.print(",");
            Serial.println(luz);
            

}


