#define trigger     10  
#define echo        9 

long duration;
int distance;


void setup(){
pinMode(trigger, OUTPUT); 
pinMode(echo, INPUT); 
Serial.begin(9600);
delay(50);
}

void loop(){

  digitalWrite(trigger, LOW);
  delayMicroseconds(2);

  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  duration = pulseIn(echo, HIGH);

  distance = duration * 0.034 / 2;
if (distance>10){
  Serial.println("Door Open");
  delay (500);
}
if(distance<10){
  Serial.println("Door Closed");
  delay(500);
}
}