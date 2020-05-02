import serial


def arduino_reading(portSerialArduino):
	"""
	Lecture infos provenant d'une carte Arduino
	"""
	
	info=''
	if (portSerialArduino.inWaiting()==0):
		info='waiting...'		
	while (portSerialArduino.inWaiting()!= 0):
		info=portSerialArduino.readline().decode('utf-8')		
	return info
	
