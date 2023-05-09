/* 
 * This sketch shows how nicla can be used in standalone mode.
 * Without the need for an host, nicla can run sketches that 
 * are able to configure the bhi sensors and are able to read all 
 * the bhi sensors data.
*/
#include "Nicla_System.h"
#include "Arduino_BHY2.h"
#include <ArduinoBLE.h>

BLEService service("19b10000-0000-537e-4f6c-d104768a1214");
BLEFloatCharacteristic gestureCharacteristic("19b10000-2001-537e-4f6c-d104768a1214", BLERead | BLENotify);

// String to calculate the local and device name
String name = "NiclaSenseME-Hall-FDI";

float gestureValue = 10;

void setup()
{
  Serial.begin(115200);

  nicla::begin();
  nicla::leds.begin();
  nicla::leds.setColor(green);

  //Sensors initialization
  BHY2.begin(NICLA_STANDALONE);
  BLE.begin();

  BLE.setLocalName(name.c_str());
  BLE.setDeviceName(name.c_str());
  BLE.setAdvertisedService("19b10000-0000-537e-4f6c-d104768a1214");

  // Add all the defined Characteristics
  service.addCharacteristic(gestureCharacteristic);
  gestureCharacteristic.writeValue(0);

  BLE.addService(service);
  BLE.advertise();
  
}

void loop()
{
  static auto lastCheck = millis();

  BLE.poll();

  if (millis() - lastCheck >= 5000) {
    lastCheck = millis();
    gestureValue = random(0, 10);
    gestureCharacteristic.writeValue(gestureValue);
  }
  /*
  while (BLE.connected()){
    BHY2.update();
  }  
  */
}
