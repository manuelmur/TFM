/* 
 * This sketch shows how nicla can be used in standalone mode.
 * Without the need for an host, nicla can run sketches that 
 * are able to configure the bhi sensors and are able to read all 
 * the bhi sensors data.
*/
#include "Nicla_System.h"
#include "Arduino_BHY2.h"
#include <ArduinoBLE.h>

#define BLE_SENSE_UUID(val) ("19b10000-" val "-537e-4f6c-d104768a1214")

const int VERSION = 0x00000000;

BLEService service(BLE_SENSE_UUID("0000"));

BLEUnsignedIntCharacteristic versionCharacteristic(BLE_SENSE_UUID("1001"), BLERead);
BLEFloatCharacteristic gestureCharacteristic(BLE_SENSE_UUID("2001"), BLERead);

// String to calculate the local and device name
String name;

//Sensor temperature(SENSOR_ID_TEMP);

void setup()
{
  Serial.begin(115200);

  Serial.println("Start");

  nicla::begin();
  nicla::leds.begin();
  nicla::leds.setColor(green);

  //Sensors initialization
  BHY2.begin(NICLA_STANDALONE);
  //temperature.begin();


  if (!BLE.begin()){
    Serial.println("Failed to initialized BLE!");
    while (1)
      ;
  }

  String address = BLE.address();

  Serial.print("address = ");
  Serial.println(address);

  address.toUpperCase();

  name = "NiclaSenseME-";
  name += address[address.length() - 5];
  name += address[address.length() - 4];
  name += address[address.length() - 2];
  name += address[address.length() - 1];

  Serial.print("name = ");
  Serial.println(name);

  BLE.setLocalName(name.c_str());
  BLE.setDeviceName(name.c_str());
  BLE.setAdvertisedService(service);

  // Add all the previously defined Characteristics
  service.addCharacteristic(gestureCharacteristic);

  // Disconnect event handler
  BLE.setEventHandler(BLEDisconnected, blePeripheralDisconnectHandler);

  // Sensors event handlers
  gestureCharacteristic.setEventHandler(BLERead, onGestureCharacteristicRead);


  versionCharacteristic.setValue(VERSION);

  BLE.addService(service);
  BLE.advertise();
}

void loop()
{
  while (BLE.connected()){
    BHY2.update();

  }
}

void blePeripheralDisconnectHandler(BLEDevice central){
  nicla::leds.setColor(red);
}

void onGestureCharacteristicRead(BLEDevice central, BLECharacteristic characteristic){
  float gestureValue = 10;
  gestureCharacteristic.writeValue(gestureValue);
}