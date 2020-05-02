int switchState = 0;
int switchState_quit=0;
void setup(){
  Serial.begin(9600);
  pinMode(2,INPUT); //lecture de l'état du switch test
  pinMode(3,INPUT); //lecture switch fin test robot twitter
  pinMode(7,OUTPUT); //allumage LED
}

void loop(){
  switchState = digitalRead(2);
  switchState_quit=digitalRead(3);
  //test état du switch test
  if (switchState == HIGH){
    digitalWrite(7,HIGH);
    Serial.write("button_pressed\n");
    delay(1000);
   }
  else {
    digitalWrite(7,LOW);
  }
    
   //test switch fermeture robot twitter
   if (switchState_quit==HIGH){
     Serial.write("quit\n");
     digitalWrite(7,HIGH);
     delay(100);
     digitalWrite(7,LOW);
     delay(100);
     digitalWrite(7,HIGH);
     delay(100);
     digitalWrite(7,LOW);
     delay(1000);
    }   
}
