/**
* @file lisandra_receiver.c
* @author Gutierrez Martin,Blanco Erick V.,Gutierrez David F.,Islas Alejandro,G. Karosuo.
* @date 11 Nov 2016
* @brief Module used to receive frames from transmitter and transfer to gateway by serial port.
*
* @see https://github.com/david9106/IS-Repo-Equipo2/tree/master/WSN/lisandra_transmitter
* @see https://github.com/david9106/IS-Repo-Equipo2/tree/master/WSN/rpi
*/

#include "LiSANDRA.h"

#define LOCAL_ADDR  0x15
#define DEST_ADDR   0x20
#define NETKEY      {0xc0,0xd1,0xce}
#define SENSORS_AMOUNT 4 

uint16_t temp;	/**< Variable used to save a sensor RAW measure temperature */
uint16_t hum;	/**< Variable used to save a sensor RAW measure humidity */
uint16_t light;		/**< Variable used to save a sensor RAW measure light */
uint16_t co2=0xAA55;	/**< Variable used to save a sensor RAW measure carbon monoxide (CO2) */
uint8_t net[3]=NETKEY;   /**< Variable used to save a NETKEY */
RadioLT_DataPkt_t mypkt;	/**< Struct used to save receive data packet*/

/**@brief The setup() function is called when program starts. Is used to initialize functions.
* The setup function will only run once, after each powerup or reset of the Lisandra board.
* Initialize Serial,leds,sensors and radio.
* @param None.
*
* @return None.
*
*/
void setup() {  
	Serial.begin(38400);
	LEDs_Ini();    
	LightSensor_Ini(); 
	HTsensor_Ini();
	RadioLT_NetIni( net, LOCAL_ADDR, DEST_ADDR );  
	RadioLT_Ini(); 
	LEDs_Grn_On(); 
}

/**@brief The loop() function does precisely what its name suggests, and loops consecutively, 
* allowing your program to change and respond. 
* The function checks if the packet received is a battery packet,if is ,checks content
* if the content is battery low or battery good send a message to gateway(RPI) by serial port.
* In case of measures packet, first decode the packet data and then sends to gateway(RPI)
*
* @param None.
*
* @return None.
*
*/
void loop() {

if( RadioLT_AvailablePkt() > 0 )
{
	RadioLT_GetPkt( &mypkt );
	String str(mypkt.data);
     if(str == "BATL"){
           Serial.print("BateriaBaja");
           Serial.print(',');
           Serial.print(mypkt.src);
           Serial.println();
     }
     else if(str == "BATOK"){
           Serial.print("BateriaOK");
           Serial.print(',');
           Serial.print(mypkt.src);
           Serial.println();
     }
     else{   
		   RadioLT_GetPkt( &mypkt );
           decodeFrame(mypkt.data);
           sendToRpi(mypkt.src,temp,hum,light,co2);
           LEDs_Ylw_On();
           delay(5);
           LEDs_Ylw_Off();
     }
  }

}

/**@brief The decodeFrame() decodes the packet (array of bytes) and parses to 
* temperature,humidity,light co2 variables (each one of 2 bytes).
*
* @param Frame (packet received).
*
* @return None.
*
*/
void decodeFrame(char * frame){
    uint8_t i=0; 
      for(i=0;i<SENSORS_AMOUNT;i++){
        switch(i){

          case 0:
            temp=frame[i];
            temp=temp<<8;
            temp|= ((uint8_t)(frame[i+1]) );
            break;
          case 1:
            hum=frame[i+1];
            hum=hum<<8;
            hum|= ((uint8_t)(frame[i+2]));
            break;
          case 2:
            light=frame[i+2];
            light=light<<8;
            light|= ( (uint8_t)(frame[i+3]));
            break;

          case 3:
            co2=frame[i+3];
            co2=co2<<8;
            co2|= ( (uint8_t)(frame[i+4]));
            break;
          }
      }

}

/**@brief The sendToRpi() sends to gateway(RPI) all measures parsed from data
* packet, in an especified format,each sensor separate by '/'. and every data
* of sensor (source,type,measure) separate by ','.
* Is nessesary a ' \ n ' to finish the message.
*
* @param param1 Source ID of packet
* @param param2 RAW temperature measure from parsed packet.
* @param param3 RAW humidity measure from parsed packet.
* @param param4 RAW light measure from parsed packet.
* @param param5 RAW CO2 measure from parsed packet.
*
* @return None.
*
*/
void sendToRpi(uint16_t srcId,uint16_t temp,uint16_t hum,uint16_t light,uint16_t co2){
            
            Serial.print("Temperatura");
            Serial.print(',');
            Serial.print(temp);
            Serial.print(',');
            Serial.print(srcId);
            Serial.print('/');
            Serial.print("Humedad");
            Serial.print(',');
            Serial.print(hum);
            Serial.print(',');
            Serial.print(srcId);
            Serial.print('/');
            Serial.print("Luz");
            Serial.print(',');
            Serial.print(light);
            Serial.print(',');
            Serial.print(srcId);
            Serial.print('/');
            Serial.print("co2");
            Serial.print(',');
            Serial.print(co2);
            Serial.print(',');
            Serial.print(srcId);
            Serial.println();

  }
