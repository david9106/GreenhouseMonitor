#include "LiSANDRA.h"


#define LOCAL_ADDR  0x15
#define DEST_ADDR   0x20
#define NETKEY      {0xc0,0xd1,0xce}

char tiempo[20];
uint8_t trama[8];
uint16_t temp;
uint16_t hum;
uint16_t luz;
RadioLT_DataPkt_t mypkt;

void setup() {
	//Se inicializa todo lo nesesario para la comunicacion
 uint8_t net[3]=NETKEY;    
    delay(5000);
    Serial.begin(38400);
    Serial.println("UART0: Inicializado");  
    LEDs_Ini();    
    Serial.println("Leds: Inicializados");
    LightSensor_Ini(); 
    Serial.println("Light Sensor: Inicializado");
    HTsensor_Ini();
    Serial.println("H&T Sensor: Inicializado");
    RadioLT_NetIni( net, LOCAL_ADDR, DEST_ADDR );   
    Serial.println("Network: Inicializada");
    RTC_Ini();
    Serial.println("Real Tiempo Clock: Inicializado");  
    RadioLT_Ini(); 
    Serial.println("RF module: Inicializado");
}


int i=0;
int cnt =0;
void loop() { 
  
    /*Mediciones RAW*/
 
    temp=HTsensor_ReadTemperatureRAW();
    hum=HTsensor_ReadHumidityRAW();
    luz=LightSensor_Read();


    /*Mediciones normales para comparar*/

    
    Serial.print("Temp:");
    Serial.print( HTsensor_ReadTemperatureC() );   
    Serial.print(" C");
    Serial.print("  Hum:");
    Serial.print( HTsensor_ReadHumidity() ); 
    Serial.print(" %");
    Serial.print("  Luz:");
    Serial.println( LightSensor_Read() ); 
    
   Serial.println();
     /* conformar paquete */

     llenaTrama(trama,temp,hum,luz);
     
     /*Ver si la trama es correcta imprimiendo primero
     las mediciones en hex y despues cada pocision de la
     trama en hex tambien*/
     /*
     Serial.print("Paquete: ");
     Serial.println(cnt);
     cnt++;
     */
     /*
     Serial.println("RAW HEX:");
     Serial.print(temp,HEX);
     Serial.print(",");
     Serial.print(hum,HEX);
     Serial.print(",");
     Serial.println(luz,HEX);
     

     /*
     Serial.println("RAW DEC:");
     Serial.print(temp,DEC);
     Serial.print(",");
     Serial.print(hum,DEC);
     Serial.print(",");
     Serial.println(luz,DEC);
*/
   
   //Mostrar trama en hexadecimal
     Serial.println("TRAMA:");
     for(i=0;i<8;i++){
     Serial.print(trama[i],HEX);
     Serial.print(":");
      }
     
    /*enviar*/
     LEDs_Red_On();
     delay(5);
     LEDs_Red_Off();
    
     RadioLT_Send( trama ); 
     RTC_GetTimeStr(tiempo);
     Serial.println();
     Serial.println(tiempo);
     Serial.flush();
	 //Se duerme el micro
     RTC_SleepCPU();
    //Salto de linea
     Serial.println();

     

}


void llenaTrama(uint8_t *trama,uint16_t temp,uint16_t hum,uint16_t luz){
  /*recorremos el byte mas significativo y hacemos un cast a byte y solo hacemos cast
  para el byte menos significativo*/
  uint8_t i=0;
  for(i=0;i<3;i++){
    switch(i){
      case 0:
      trama[i]=uint8_t(temp>>8);
      trama[i+1]=uint8_t(temp);
      break;
      case 1:
      trama[i+1]=uint8_t(hum>>8);
      trama[i+2]=uint8_t(hum);
      break;
      case 2:
      trama[i+2]=uint8_t(luz>>8);
      trama[i+3]=uint8_t(luz);
      break;
      }
    }
    trama[6]=0xAA;
    trama[7]=0x55;
  }


  
