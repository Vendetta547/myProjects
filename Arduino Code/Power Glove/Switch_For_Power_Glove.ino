/*The word switch is used as a substitute for "force sensitive resistor." Therefore, every time terminology
like "switch flip" or something similar occurs, it is synonymous to the resistor being pressed. It serves the function
of a pressable switch. It is also used for the sake of brevity and simplicity of code comments*/


int sensePin = 0; //variable to read resistor input
int mousePower = 8; //pin to supply circuit board with power
int ledPin = 9;

void setup()
{
  Serial.begin(9600);
  pinMode(mousePower, OUTPUT); //have mousePower output voltage to the arduino
  pinMode(sensePin, INPUT); //have sensePin read input
  pinMode(ledPin, OUTPUT); //have ledPin output voltage to a light
}
                                                                                            
void loop() //while the arduino has power                                                                                                 
{                                                                                                                                         
  int threshold = 500; // value that must be exceeded to flip the switch                                                                    
  int value = analogRead(sensePin); //read in the current pressure on the resistor                                                        
  static int flipcount = 0; //counts number of switch flips                                                                               
  bool was_flipped = false; //logically in each loop, the switch has not been flipped                                                     
                                                                                                                                          
                                                                                                                                          
  while (value > threshold) //when the switch is flipped ("while" loop is used because of dealing with analog input)                   
  {
      was_flipped = true; //let the arduino know the switch was flipped
      value = analogRead(sensePin); //continue to read pressure on resistor
  }

  if (was_flipped) //if the switch was flipped
  {
    flipcount++; //increase flipcount by one
    
    if (flipcount % 2 == 1) //if the switch has been flipped an odd number of times
    {
      digitalWrite(mousePower, HIGH); //then it should be in the on position
      digitalWrite(ledPin, HIGH); //and the light comes on to indicate so
    }

    else if (flipcount % 2 == 0) //if the switch has been flipped an even number of times
    {
      digitalWrite(mousePower, LOW); //then it should be in the off position
      digitalWrite(ledPin, LOW); //and the light turns off to indicate so
    }
  }

  Serial.println(value); //allows analog value checking within the serial monitor
}
