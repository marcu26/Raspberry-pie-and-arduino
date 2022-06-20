#include <LiquidCrystal_I2C.h>
#include <Servo.h>
#include <IRremote.h>
LiquidCrystal_I2C lcd(0x20,16,2);
Servo capRobot; 

#define echoPin 2 
#define trigPin 3
#define greenLed 9
#define redLed 10
#define servoPin 5

int RECV_PIN=12; 
IRrecv irrecv(RECV_PIN); 


long duration;
int distance; 
int angle = 90;
bool way=0;
String line1;
String line2;



void setup(){
  Serial.begin(9600);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);

  digitalWrite(greenLed,HIGH);
  digitalWrite(redLed,HIGH);
  
  
  lcd.init();                      
  lcd.backlight();
  
  lcd.home();

  capRobot.attach(servoPin);
  capRobot.write(angle);


  irrecv.enableIRIn(); 
}


  
void loop()
{
  String s="Dist: ";
  int dist=getDistance();
  s=s+String(dist);
  if(dist>=100)
  {
    changeLedText(s,"");
    maiCauta();
    capRobot.write(angle);
    delay(800);
  }

  else
  {
  int distance=getDistance();
  delay(800);
  String recived="";
  if (irrecv.decode())
  {
  recived=String(irrecv.decodedIRData.decodedRawData, HEX);
  irrecv.resume(); 
  }
  
  changeLedText(s,recived);
  }
   
}




int getDistance()
{

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor
  return distance;
}

void maiCauta()
{
  if(way==true && angle <170)
  {
  angle+=20;
  return;
  }

  else if(way==true && angle==170)
  {
    way=false;
    return;
  }

  else if(way==false && angle>10)
  {
    angle-=20;
    return;
  }

    else if(way==false && angle==10)
  {
    way=true;
    return;
  }
}

void changeLedText(String text1, String text2)
{
 if(line1 != text1 || line2 != text2)
 {
  
  int xPos=8-text1.length()/2;
  if(text1.length()%2==1)
  xPos-=1;
  lcd.clear();
  lcd.setCursor(xPos,0);
  lcd.print(text1);
  line1=text1;
  
  xPos=8-text2.length()/2;
  if(text2.length()%2==1)
  xPos-=1;
  lcd.setCursor(xPos,1);
  lcd.print(text2);
  line2=text2;
 }    
   
}
