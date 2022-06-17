#include <Servo.h>

Servo myservo;

#define greenLed 11
#define redLed 12
#define yellowLed 10

void setup()
{
   pinMode(greenLed, OUTPUT);
   pinMode(redLed, OUTPUT);
   pinMode(13,OUTPUT);
   pinMode(yellowLed,OUTPUT);
   digitalWrite(13,LOW);
   
   digitalWrite(redLed,HIGH);
   myservo.attach(9);
}

void loop() 
{ 

 openDoor();
 
}

void openDoor()
{
   delay(3000);
    myservo.attach(9);
    myservo.write(90);
    digitalWrite(redLed,LOW);
    digitalWrite(greenLed,HIGH);
    
   myservo.write(180);
    delay(110);
     myservo.write(90);
     delay(4500);
     digitalWrite(greenLed,LOW);
     digitalWrite(yellowLed,HIGH);
     delay(2000);
     myservo.write(0);
      delay(80);
    myservo.detach();
    
    delay(100);
     digitalWrite(yellowLed,LOW);
     digitalWrite(redLed, HIGH);
}
