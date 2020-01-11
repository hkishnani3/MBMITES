int sensorValue, AQ_sensor_pin=0;
int Refresh_time = 1000;

void setup() {
    Serial.begin(9600);
}

void loop() {
  if(Serial.available()){
    sensorValue = analogRead(AQ_sensor_pin);
    Serial.println(sensorValue);
  }
  Serial.println(sensorValue);
  
  delay(Refresh_time);
}
