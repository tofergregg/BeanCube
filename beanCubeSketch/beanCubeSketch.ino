// send acceleration data over a serial stream
 
void setup() {
	// initialize serial communication at 57600 bits per second:
	Serial.begin(57600);
        Serial.setTimeout(25);
}
 
void getAccel(char *buffer) {
        int16_t accelX,accelY,accelZ;
	size_t length = 6;
	
	accelX = Bean.getAccelerationX();
	accelY = Bean.getAccelerationY();
	accelZ = Bean.getAccelerationZ();
	
        // send two zeros so we know where the start of a reading is
        buffer[0] = 0;
        buffer[1] = 0;

	buffer[2] = accelX >> 8; // high order byte of X
	buffer[3] = accelX & 0xFF; // low order byte of X
	
	buffer[4] = accelY >> 8; // high order byte of Y
	buffer[5] = accelY & 0xFF; // low order byte of Y
	
	buffer[6] = accelZ >> 8; // high order byte of Z
	buffer[7] = accelZ & 0xFF; // low order byte of Z
}

// the loop routine runs over and over again forever:
void loop() {
        char accelVals[8];
	size_t length = 8;
	
        getAccel(accelVals);
  	Serial.write((uint8_t*)accelVals, length);
  	
        delay(50);
}

