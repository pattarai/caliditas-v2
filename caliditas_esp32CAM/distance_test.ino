const int trigPin = 2;
const int echoPin = 13;

//define sound speed in cm/uS
#define SOUND_SPEED 0.034
#define CM_TO_INCH 0.393701
 
void setup() {
  Serial.begin(115200); // Starts the serial communication
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
}

void loop() {
  // Ultrasonic Pulse
  digitalWrite(trigPin, LOW);// Clears the trigPin
  delayMicroseconds(2); 
  digitalWrite(trigPin, HIGH); // Sets the trigPin on HIGH state for 10 micro seconds
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Reads echoPin, returns sound wave travel time in microseconds & calculate distance
  float distanceCm = pulseIn(echoPin, HIGH) * SOUND_SPEED/2;
   
  
  // Prints the distance in the Serial Monitor
  Serial.print("Distance (cm): ");
  Serial.println(distanceCm); 

  // 30 is good

  delay(1000);
}