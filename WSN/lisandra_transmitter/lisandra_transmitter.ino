
/**
* @file lisandra_transmitter.ino
* @author Gutierrez Martin,Blanco Erick V.,Gutierrez David F.,Islas Alejandro,G. Karosuo.
* @date 11 Nov 2016
* @brief Module used to sends frames with the sensors measures to gateway.
*
* @see https://github.com/david9106/IS-Repo-Equipo2/tree/master/WSN/lisandra_receiver
* @see https://github.com/david9106/IS-Repo-Equipo2/tree/master/WSN/rpi
*/

#include "LiSANDRA.h"

#define T 60
#define LOCAL_ADDR  0x15
#define DEST_ADDR   0x20
#define NETKEY      {0xc0,0xd1,0xce}

static uint16_t SleepCnt=0; 	/**< Variable used to count how many times lisandra fall asleep */
uint8_t battery_state[9];		/**< Variable used to represent a state of battery */			
uint8_t  f[8];				/**< Variable used to package sensors RAW measures */
uint16_t temp;					/**< Variable used to save a sensor RAW measure temperature */
uint16_t hum;					/**< Variable used to save a sensor RAW measure humidity */
uint16_t light;					/**< Variable used to save a sensor RAW measure light */
uint16_t co2=0xAA55;			/**< Variable used to save a sensor RAW measure carbon monoxide (CO2) */
bool batOK=true;				/**< Flag used to know if battery was read and was in a good state */
uint8_t net[3]=NETKEY;   		/**< Variable used to save a NETKEY */
RadioLT_DataPkt_t mypkt;		/**< Struct used to send colected sensors data */

/**@brief The setup() function is called when program starts. Use it to initialize functions.
* The setup function will only run once, after each powerup or reset of the Lisandra board.
* Initialize Serial,leds,sensors and radio.
*
* @param None.
*
* @return None.
*
*/
void setup() { 
    delay(3000);
    Serial.begin(38400);
    LEDs_Ini();    
    LightSensor_Ini(); 
    HTsensor_Ini();
	RTC_Ini(); 
    RadioLT_NetIni( net, LOCAL_ADDR, DEST_ADDR );   
    RadioLT_Ini(); 
}

/**@brief The loop() function does precisely what its name suggests, and loops consecutively, 
* allowing your program to change and respond. 
* First check the state of battery, then takes sensors measures, fetch the frame with the colected
* measures, an finally sends to gateway.
*
* @param None.
*
* @return None.
*
*/
void loop() { 
    battery_check(battery_state);
	temp=HTsensor_ReadTemperatureRAW();
	hum=HTsensor_ReadHumidityRAW();
	light=LightSensor_Read();
	fetchFrame(f,temp,hum,light,co2);
	printFrame(f);
	RadioLT_Send( f );
	sleep();
}

/**@brief The fetchFrame() function puts the sensors measures splitted in bytes in array of bytes.
* Each measure has 2 bytes length, to put in array is nessesary split in two bytes, high an low,
* to do that, first shift right the bits of variable 8 positions (high byte) and saves, then only do a cast 
* of variable and saves in array
*
* @param param1 Array of bytes.
* @param param2 RAW temperature measure.
* @param param2 RAW humidity measure.
* @param param2 RAW light measure.
* @param param2 RAW CO2 measure.
* 
* @return None.
*
*/
void fetchFrame(uint8_t *fram,uint16_t temp,uint16_t hum,uint16_t light,uint16_t co2){
  uint8_t i=0;
  for(i=0;i<4;i++){
    switch(i){
      case 0:
      fram[i]=uint8_t(temp>>8);
      fram[i+1]=uint8_t(temp);
      break;
      case 1:
      fram[i+1]=uint8_t(hum>>8);
      fram[i+2]=uint8_t(hum);
      break;
      case 2:
      fram[i+2]=uint8_t(light>>8);
      fram[i+3]=uint8_t(light);
      break;
	  case 3:
	  fram[i+3]=uint8_t(co2>>8);
	  fram[i+4]=uint8_t(co2);
	  break;
    }
  }
}


/**@brief The readVC() function measures the battery level.
*
* The battery level measure is taken by the adc (Analog Digital Converter).
* Read 1.1V reference against a Vcc
* @param None.
*
* @return ADC measure.
*
*/
int readVcc() {
	int result;	/**< Variable used to save result measure */
	ADMUX = _BV(REFS0) | _BV(MUX4) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1);
	delay(2);
	ADCSRA |= _BV(ADSC); 
	while (bit_is_set(ADCSRA,ADSC));
	result = ADCL;
	result |= ADCH<<8;
	return result;
}

/**@brief The blink() function blinks a led.
*
* @param None.
*
* @return None.
*
*/
void blink(){
	LEDs_Ylw_On();
	delay(5);
	LEDs_Ylw_Off();	
}

/**@brief The sleep() function sleeps Lisandra by 5 minutes (using 5 seconds microsleeps).
*
* @param None.
*
* @return None.
*
*/  
void sleep(){
	do{
		RTC_SleepCPU();
		SleepCnt++;
		LEDs_Red_On();
		delay(5);
		LEDs_Red_Off();
	}while( SleepCnt<T);
	SleepCnt=0;
}

/**@brief The printFrame() function prints the created frame using serial port.
*
* @param None.
*
* @return None.
*
*/ 
void printFrame(uint8_t *fra){
  uint8_t i=0;
	for(i=0;i<8;i++){
		Serial.print(fra[i],HEX);
		Serial.print(" ");}
		Serial.println();
		Serial.flush();
}

/**@brief The battery_check() function checks if battery level is under 2.2v and sends battery alert message (low battery)
* if not sends an alert battery message (good battery).
*
* @param None.
*
* @return None.
*
*/
void battery_check(char *battery_state){
  uint16_t adc=readVcc();
  Serial.println();
  Serial.print("adc battery: ");
  Serial.println(adc);
  
	if(adc >= 500)
	{
		battery_state[9]={"BATL"};
		RadioLT_Send( battery_state ); 
		blink();
		batOK=true;
		Serial.println(battery_state);
	}
	else if((adc <= 410) && batOK){
		battery_state[9]={"BATOK"}; 
		RadioLT_Send( battery_state ); 
		blink();
		batOK=false;
		Serial.println(battery_state);
	}
}
