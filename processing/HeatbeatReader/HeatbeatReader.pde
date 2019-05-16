import processing.serial.*;

Serial myPort;  // Create object from Serial class
int val, screen_increment, old_x=0, old_y=0;      // Data received from the serial port
String inString;  // Input string from serial port
int lf = 10;      // ASCII linefeed 
void setup() 
{

  size(600, 600);
  String portName = Serial.list()[0];
  println(Serial.list());
  
  myPort = new Serial(this, portName, 9600);//Set up the serial port
  myPort.bufferUntil(lf);//read in data until a line feed, so the arduino must do a println
  background(255,255,255);//make the background that cool blood red
}

void draw()
{

}

void serialEvent(Serial myPort) { 

  inString = myPort.readString();
  inString = trim(inString);
  println(inString);
  val = int(inString) *10;
  strokeWeight(12);
  stroke(0,0,0);
  
  line(50, 100,100, 600-100);
  
}