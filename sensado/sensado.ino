#include "LiSANDRA.h"


#define LOCAL_ADDR  0x15
#define DEST_ADDR   0x20
#define NETKEY      {0xc0,0xd1,0xce}

char tiempo[20];

void sleep_cpu_sec(uint8_t secs){
  int SleepCnt = 0;
    do{
       RTC_SleepCPU();
       SleepCnt++;
    }while( SleepCnt==secs); 
 }

/*by Rafael Karosuo
 * ****CONVERTS FLOAT TO STRING WITH 2 DEC VALUES
 * fstr -> float string, 4 spaces, {int val, point, dec val, null term}
 * function based on function made by Don Kinzer (http://www.arduino.cc/cgi-bin/yabb2/YaBB.pl?num=1207226548/11#11)
*/
char * get_string_float(float num, char fstr[4]){
  fstr = null;
  if(int(num) < 255){    
    fstr[0] = (char) int(num);
    fstr[1] = '.';  
    fstr[2] = (num - int(num))*100; //2 dec positions
  }
    return fstr;
 }

void setup() {
    uint8_t net[3]=NETKEY;    
    delay(3000);
    Serial.begin(38400);
    //Serial.println("UART0: Inicializado");
    
    LEDs_Ini();    
    //Serial.println("Leds: Inicializados");
    
    LightSensor_Ini(); 
    //Serial.println("Light Sensor: Inicializado");
    
    HTsensor_Ini();
    //Serial.println("H&T Sensor: Inicializado");
    
    RadioLT_NetIni( net, LOCAL_ADDR, DEST_ADDR );   
    //Serial.println("Network: Inicializada");
 
    RTC_Ini();
    //Serial.println("Real Tiempo Clock: Inicializado");
      
    RadioLT_Ini(); 
    //Serial.println("RF module: Inicializado");
    
}

void loop() {
  char msg[9]={"abcdefgh"};
  sleep_cpu_sec(300); //Sensar cada 5 mins

  /* sensar*/
  unint16_t light_value = LightSensor_Read();
  float heat_value = HTsensor_ReadTemperatureC();
  float rh_value = HTsensor_ReadHumidity();
  
     /* conformar paquete */
     /* enviar */
     LEDs_Red_On();
     delay(5);
     LEDs_Red_Off();
    
     RadioLT_Send( msg ); 
     RTC_GetTimeStr(tiempo);
     Serial.println(tiempo);
     Serial.flush();
}
