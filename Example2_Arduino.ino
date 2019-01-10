#define LED 13

void setup() {
    pinMode(LED, OUTPUT);
    Serial.begin(115200);
}

void loop() {
    if (Serial.available() > 0) {
        char serialRead = Serial.read();
        
        if (serialRead == '1') {
            digitalWrite(LED, HIGH);
        }
        else if (serialRead == '0') {
            digitalWrite(LED, LOW);
        }
    }
}
