#include <Arduino.h>

const int relayPin = 23; // Pin connected to the relay module

void setup() {
  Serial.begin(115200); // Initialize Serial communication at 115200 baud
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW); // Start with the relay OFF
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the incoming character

    if (command == 'H') {
      digitalWrite(relayPin, HIGH); // Turn Relay ON
      Serial.println("Relay ON");
    } 
    else if (command == 'L') {
      digitalWrite(relayPin, LOW);  // Turn Relay OFF
      Serial.println("Relay OFF");
    }
  }
}
