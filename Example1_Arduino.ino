void setup() {
  Serial.begin(115200);
}

void loop() {
  Serial.write("Hello World");
  delay(1000);
}
