import serial

ser = serial.Serial('/tmp/tty.LightBlue-Bean', 57600, timeout=0.25) # wait 250msec for bean

def web_socket_do_extra_handshake(request):
    pass  # Accept all requests

def web_socket_transfer_data(request):
    while True:
        line = request.ws_stream.receive_message()
        if line is None:
            return
        accelData = readAccel()
        if len(accelData) > 0:
        	request.ws_stream.send_message(	str(accelData['x'])+','+
        					str(accelData['y'])+','+
        					str(accelData['z']), binary=False)
        else:
        	request.ws_stream.send_message( "no data" )
def readBytes():
	highByte = ser.read(1)
	lowByte = ser.read(1)
	if len(highByte) > 0 and len(lowByte) > 0:
		val = bytesToUnsigned(highByte, lowByte)
		if val > 255:
			val = 255
		if val < -255:
			val = -255
		return val
	else:
		return -65535

def findZeros():
	# read bytes until we get two zeros
	ser.flushInput() # no need for old data
	# try 100 times before giving up
	count = 0
	while count < 100:
		byte = ser.read(1)
		if byte == '\x00':
			byte = ser.read(1)
			if byte=='\x00':
				return True # found two zeros in a row
		count+=1
	return False # no luck
	
def readAccel():
	accelData = {}
	
	# once we find two zeros,
	# we should get six more bytes
	if findZeros():
		accelData['x'] = readBytes()
		accelData['y'] = readBytes()
		accelData['z'] = readBytes()
	
	return accelData

def bytesToUnsigned(highByte,lowByte):
	unsignedByte = (ord(highByte)<<8) + ord(lowByte)
	if unsignedByte > (2<<14)-1:
		return unsignedByte - (2<<15)
	else:
		return unsignedByte
