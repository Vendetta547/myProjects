
  
int speakerPin = 1;
int lightPin = 0;

void playTone(int tone) {
  for (long i = 0; i <1000L; i += tone * 2) {
    digitalWrite(speakerPin, HIGH);
    delayMicroseconds(tone);
    digitalWrite(speakerPin, LOW);
    delayMicroseconds(tone);
  }
}

void playNote(int note) {
  //char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
  int tones[] = { 1915, 1700, 1519, 1432, 1275, 1136, 1014, 956 };
  playTone(tones[note]);
}

void setup() {
  pinMode(speakerPin, OUTPUT);
}

void loop() {
  int lightLevel = analogRead(lightPin);
  lightLevel = map(lightLevel, 0, 900, 0, 255);
  lightLevel = constrain(lightLevel, 0, 255);
  
  
  if(lightLevel <= 99) {
    lightLevel = 0; 
  }
  
  else if (100 <= lightLevel && lightLevel <= 117){
    lightLevel = 1;
  }
  
  else if (118 <= lightLevel && lightLevel <= 135) {
    lightLevel = 2;
  }
  
  else if (136 <= lightLevel && lightLevel <= 153) {
    lightLevel = 3;
  }
  
  else if (154 <= lightLevel && lightLevel <= 171) {
    lightLevel = 4;
  }
  
  else if (172 <= lightLevel && lightLevel <= 189) {
    lightLevel = 5;
  }
  
  else if (190 <= lightLevel && lightLevel <= 207) {
    lightLevel = 6;
  }
  
  else 
    lightLevel = 7;
  
  playNote(lightLevel);
  
}
