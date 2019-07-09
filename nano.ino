#include <BoltIoT-Arduino-Helper.h>

String getAnalogValues(String *data){
  String retval="";
  retval=retval+analogRead(A0)+",";
  retval=retval+analogRead(A1)+",";
  retval=retval+analogRead(A2)+",";
  retval=retval+analogRead(A3)+",";
  retval=retval+analogRead(A4)+",";
  return retval;
}

String pumpOn(String *data){
  String retVal="Pump switched On";
  digitalWrite(3,HIGH);
  return retVal;
}

String pumpOff(String *data){
  String retVal="Pump switched Off";
  digitalWrite(3,LOW);
  return retVal;
}

void setup(){
  boltiot.begin(Serial);
  boltiot.setCommandString("getAnalogValues",getAnalogValues);
  boltiot.setCommandString("pumpOn",pumpOn);
  boltiot.setCommandString("pumpOff",pumpOff);
}

void loop(){
  boltiot.handleCommand();
}
