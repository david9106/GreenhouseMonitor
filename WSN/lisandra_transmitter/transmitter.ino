#include "LiSANDRA.h"

#define T 1
#define LOCAL_ADDR  0x15
#define DEST_ADDR   0x20
#define NETKEY      {0xc0,0xd1,0xce}

char tiempo[20];
uint8_t trama[8];
uint16_t temp;
uint16_t hum;
uint16_t luz;
/*Valor de prueba para co2 (cambiara cuando se implemente el sensor)*/
uint16_t co2=0xAA55;
uint16_t SleepCnt=0;
uint8_t i=0;
RadioLT_DataPkt_t mypkt;
bool setAlarm = false;

void setup() {
 uint8_t net[3]=NETKEY;    
    delay(3000);
	//Inicializamos la comunicacion serial
    Serial.begin(38400);
	//Inicializamos los leds
    LEDs_Ini();    
	//Inicializamos el sensor de luz
    LightSensor_Ini(); 
	//Inicializamos de humedad y temperatura
    HTsensor_Ini();
	//Inicializamos el modulo de RF
	RTC_Ini(); 
    RadioLT_NetIni( net, LOCAL_ADDR, DEST_ADDR );   
    RadioLT_Ini(); 
}

void loop() { 
  
  if(readVcc() >= 500){
    char msg[9]={"BATL"};//mensaje de Bateria baja   
     Serial.print( msg );
     Serial.println();
     LEDs_Ylw_On();
     delay(5);
     LEDs_Ylw_Off();
      /*enviar*/
         RadioLT_Send( msg ); 
      /*Obtener tiempo*/
         RTC_GetTimeStr(tiempo);
       /*Mostrar tiempo por serial*/
         Serial.println(tiempo);
       /*Vaciar el buffer Serial*/
         Serial.flush();
    
       /*Ciclo para mantener dormido al micro durante 5min*/
      do{
    
        
           RTC_SleepCPU();
           SleepCnt++;
         /*blink solo para saber si esta trabajando no se usara y no es nesesario es de prueba solamente*/
           LEDs_Red_On();
         /*Importante el delay si es neseario, para que el micro tenga tiempo suficiente de despertar y volverse a dormir*/
           delay(5);
           LEDs_Red_Off();
        }while( SleepCnt<1);
        
  
  }
  
    	SleepCnt=0;
    
        /*Obtener Mediciones RAW*/
        temp=HTsensor_ReadTemperatureRAW();
        hum=HTsensor_ReadHumidityRAW();
        luz=LightSensor_Read();
    
         /* conformar paquete */
         llenaTrama(trama,temp,hum,luz);
    	/*Mostrar trama en hexadecimal*/
         for(i=0;i<8;i++){
         Serial.print(trama[i],HEX);
         Serial.print(" ");}
         Serial.println();
    	/*blink*/
         LEDs_Red_On();
         delay(5);
         LEDs_Red_Off();
    	 /*enviar*/
         RadioLT_Send( trama ); 
    	 /*Obtener tiempo*/
         RTC_GetTimeStr(tiempo);
    	 /*Mostrar tiempo por serial*/
         Serial.println(tiempo);
    	 /*Vaciar el buffer Serial*/
         Serial.flush();
    
    	 /*Ciclo para mantener dormido al micro durante 5min*/
      do{
    
        
           RTC_SleepCPU();
           SleepCnt++;
    	   /*blink solo para saber si esta trabajando no se usara y no es nesesario es de prueba solamente*/
           LEDs_Red_On();
    	   /*Importante el delay si es neseario, para que el micro tenga tiempo suficiente de despertar y volverse a dormir*/
           delay(5);
           LEDs_Red_Off();
        }while( SleepCnt<T);
        

  
}

/*Funcion encargada de empaquetar los bytes en la trama*/
void llenaTrama(uint8_t *trama,uint16_t temp,uint16_t hum,uint16_t luz){
  uint8_t i=0;
  for(i=0;i<4;i++){
    switch(i){
      case 0:
	  /*obtenemos el byte alto de la medicion se le hace cast y lo asignamos la pocision i de la trama*/
      trama[i]=uint8_t(temp>>8);
	  /*obtenemos el byte bajo de la medicion se le hace cast y lo asignamos la pocision i de la trama*/
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
      
	  case 4:
	  trama[i+3]=uint8_t(co2>>8);
      trama[i+4]=uint8_t(co2);
	  break;
    }
  }
}

//funcion para medir la carga de la pila
int readVcc() {
  int result;
  // Read 1.1V reference against AVcc
  //leer 1.1V en referencian contra Vcc-real
  ADMUX = _BV(REFS0) | _BV(MUX4) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1);
  delay(2);//esperar que se inialize bien
  ADCSRA |= _BV(ADSC); // Convertir
  
  while (bit_is_set(ADCSRA,ADSC));
  result = ADCL;
  result |= ADCH<<8;
  Serial.println( result );
 // result = 1125 / result;
   
  
  // regresar valor calculado
  return result;
}

  
