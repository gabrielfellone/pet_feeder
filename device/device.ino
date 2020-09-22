#include <Servo.h>

#define PIR D0
#define SERVO D1
#define INTERVAL 1000

Servo servo;

int pos;
unsigned long previousMillis = 0;

void abre() {
  delay(1000);
  for (pos = 180; pos >= 0; pos--) {
    servo.write(pos);
    delay(15);
  }

  delay(300);
  fecha();
}

void fecha() {
  for (pos = 0; pos < 180; pos++) {
    servo.write(pos);
    delay(15);
  }
}

boolean feedTime() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= INTERVAL) {
    previousMillis = currentMillis;
    return true;
  }
  else {
    return false;
  }
}

void setup() {
  Serial.begin(9600);
  pinMode(PIR, INPUT);
  servo.attach(SERVO);
  servo.write(180);
}

void loop() {
  if (Serial.available() > 0) {
    if (Serial.readString() == "open") {
      abre();
    }
  }

  if (digitalRead(PIR) && feedTime()) {
    Serial.println(1);
  }
  else {
    Serial.println(0);
  }

  delay(1000);
}
