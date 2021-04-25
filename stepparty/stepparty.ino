

#include <ArduinoJson.hpp>
#include <ArduinoJson.h>
#include <Stepper.h>


char serialData;


const int maxRevolutions = 147; // Number of revolutions from point A to point B is 147.
const int maxRevolutionsRL = 36; // Number of revolutions from point A to point B is 36.
const int stepsPerRevolution = 200;  // 200 steps per revolution
const int stepsPerRevolution2 = 200;  // 200 steps per revolution
bool sourceToBack = true;

Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11); // initialize the stepper library on pins 8 through 11
Stepper myStepper2(stepsPerRevolution2, 7, 6, 5, 4); // initialize the stepper library on pins 7 through 4

int totalLoops = 0;

void setup() {

  myStepper.setSpeed(100);   // Max speed is 200RPM, but best speed is 100RPM:
  myStepper2.setSpeed(100);   // Max speed is 200RPM, but best speed is 100RPM:
  
  Serial.begin(9600); // initialize the serial port:
  
}

void loop() {



  deserializeObject();
  //if(Serial.available()){

    //deserializeObject();
    
        
    //}
  
  //goDown(1);    
  
  

}



void deserializeObject()
{
    String json = "{\"left\":100,\"up\":10,\"down\":30,\"right\":100,\"down\":10,\"up\":10,\"left\":50,\"down\":10,\"up\":10,\"left\":50,\"down\":40,\"up\":20,\"right\":100,\"down\":20}";
    //String json = "{\"left\":200,\"down\":200,\"right\":200,\"up\":200,\"left\":100,\"down\":100,\"right\":100,\"up\":100,\"left\":50,\"down\":50,\"right\":50,\"up\":50}";
    
    StaticJsonDocument<300> doc;
    DeserializationError error = deserializeJson(doc, json);
    if (error) { return; }
    JsonObject documentRoot = doc.as<JsonObject>();
    String key = "";
    int value = 0;

    for (JsonPair keyValue : documentRoot) {

      
    key = keyValue.key().c_str();
    value = keyValue.value().as<int>();


    if(key == "up"){
      goUp(value);
      }
    if(key == "down"){
      goDown(value);
      }
    if(key == "right"){
      goRight(value);
      }
    if(key == "left"){
      goLeft(value);
      }
    
  
  
  }

    
}





int goUp(int revs){

  int helper = 0;
  Serial.println("goUp goUp goUp...");
  while(helper <= revs){
      Serial.println(helper);
      myStepper.step(stepsPerRevolution);
      helper ++;
    }
    
  return 1;
  
  }


int goDown(int revs){

    int helper = 0;
    Serial.println("goDown goDown goDown...");
  while(helper <= revs){
        Serial.println(helper);
        myStepper.step(-stepsPerRevolution);
        helper ++;    
    }

    return 2;
  
  }







int goRight(int revs){

  int helper = 0;
  Serial.println("goRight goRight goRight...");
  while(helper <= revs){
      Serial.println(helper);
      myStepper2.step(stepsPerRevolution2);
      helper ++;
    }
    
  return 3;
  
  }


int goLeft(int revs){

    int helper = 0;
    Serial.println("goLeft goLeft goLeft...");
  while(helper <= revs){
        Serial.println(helper);
        myStepper2.step(-stepsPerRevolution2);
        helper ++;    
    }

    return 4;
  
  }


  




void findEdges(){

  
 
  
  if (totalLoops == 147){
    
    totalLoops = 0;
    if(sourceToBack == true){
          sourceToBack = false;
    }else{
          sourceToBack = true; 
    }
    

    
    }else{

      if(sourceToBack == true){
            goUp(20);
      }else{
         goDown(20);  
      }
      
      
    }


    totalLoops = totalLoops + 1;
  
  }




  
  
  
