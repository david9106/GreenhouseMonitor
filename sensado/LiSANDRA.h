/*
BY PHD L. AGUILAR
*/
#ifndef LISANDRA_h
#define LISANDRA_h 

/* LEDs */
void LEDs_Ini( void );
void LEDs_Red_On( void );
void LEDs_Red_Off( void );
void LEDs_Ylw_On( void );
void LEDs_Ylw_Off( void );
void LEDs_Grn_On( void );
void LEDs_Grn_Off( void );

/* LightSensor  */
void LightSensor_Ini( void ); 
uint16_t LightSensor_Read( void ); 

/* SHT Sensor */
void  HTsensor_Ini( void );
float HTsensor_ReadHumidity( void );
float HTsensor_ReadTemperatureC( void );
uint16_t HTsensor_ReadHumidityRAW( void );
uint16_t HTsensor_ReadTemperatureRAW( void );
   
/* RF module */
typedef struct{
   uint8_t dst;
   uint8_t src;
   uint8_t ptype;
      char data[8];
} RadioLT_DataPkt_t;

void    RadioLT_Ini( void );
void    RadioLT_SetDstAddr( uint8_t dst);
void    RadioLT_SetSrcAddr( uint8_t src);
void    RadioLT_SetNetAddr( uint32_t netkey );
void    RadioLT_NetIni( uint8_t *netkey, uint8_t src_addr, uint8_t dst_addr );
void    RadioLT_Send( char *msg );
void    RadioLT_GetDataPkt( char *msg );
void    RadioLT_GetPkt( RadioLT_DataPkt_t *pkt );
uint8_t RadioLT_AvailablePkt( void );
uint8_t RadioLT_GetSrcAddrPkt( RadioLT_DataPkt_t *pkt );
uint8_t RadioLT_GetDstAddrPkt( RadioLT_DataPkt_t *pkt );
uint8_t RadioLT_GetTypPkt( char *msg );   

/* RTC */
typedef struct {
  uint8_t hrs; 
  uint8_t min; 
  uint8_t seg;
}time_t;

void RTC_Ini( void );
void RTC_SetTime_Hr_Min_Seg( uint8_t hrs, uint8_t mins, uint8_t segs );
void RTC_SetTime( time_t tiempo );
void RTC_GetTime( time_t *tiempo );
void RTC_GetTimeStr( char *str );
void RTC_PrintTime( void );
void RTC_SleepCPU( void );

#endif
