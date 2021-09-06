#include <Servo.h>
#include <string.h>
Servo servo1, servo2, servo3, servo4;

void setup() {
 Serial.begin(9600);
 Serial.setTimeout(1);
 servo1.attach(4);
 servo2.attach(5);
 servo3.attach(6);
 servo4.attach(7);
 int a = 0;
 servo1.write(a);
 servo2.write(a);
 servo3.write(a);
 servo4.write(a);
}

int make_num(int num) {
  return num == '1' ? 80 : 0;
}

void loop() {
  // put your main code here, to run repeatedly:
  String str;
//  int a = 180;
//   servo1.write(a);
//   servo2.write(a);
//   servo3.write(a);
//   servo4.write(a);
//char temp[100];
//  if(Serial.available()
//    byte leng = Serial.readBytesUntil(':', temp, 12);
    char ed[6][4] = {{'0','1','0','1'},{'0','0','0','1'},{'1','1','1','0'},{'1','0','1','1'},{'0','1','0','1'},{'0','1','1','0'}};
   
//    
//    Serial.print("Input data Lenght : ");
//    Serial.println(leng);
   for(int i = 0; i< 6; i++) {
      servo1.write(make_num(ed[i][0]));
      servo2.write(make_num(ed[i][1]));
      servo3.write(make_num(ed[i][2]));
      servo4.write(make_num(ed[i][3]));
      delay(400);
   }
//    if(leng == 4 && temp[0] == '1' || temp[0] == '0') {
//      servo1.write(make_num(temp[0]));
//      servo2.write(make_num(temp[1]));
//      servo3.write(make_num(temp[2]));
//      servo4.write(make_num(temp[3]));
//    }
//    Serial.println(temp);
//    for(int i = 0; i < leng; i++){
//      Serial.print(temp[i]);
//    }
//    Serial.println();
//  }    
//  while(Serial.available() > 0) {
////    for(int i = 0; i < 6; i++) {
//      char buffer[24];
//      Serial.readBytesUntil('q', buffer, 4);
//      servo1.write(make_num(buffer[0]));
//      servo2.write(make_num(buffer[1]));
//      servo3.write(make_num(buffer[2]));
//      servo4.write(make_num(buffer[3]));
//      Serial.println(buffer);
////    }
//  }
}