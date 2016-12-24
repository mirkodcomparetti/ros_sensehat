from sense_hat import SenseHat

def get_temperature(sense):
	return sense.get_temperature()

def get_humidity(sense):
	return sense.get_humidity()

def get_pressure(sense):
	return sense.get_pressure()

def get_gyroscope(sense):
	return sense.get_gyroscope()

def get_stick(sense):
	stickEvents = sense.stick.get_events()
	if (len(stickEvents) > 0):
		return stickEvents[-1]
	else:
		return None

def get_accelerometer(sense):
	return sense.get_accelerometer_raw()

def get_compass(sense):
	return sense.get_compass()

def get_gyroscope(sense):
	return sense.get_gyroscope_raw()

def get_magnetometer(sense):
	return sense.get_compass_raw()

def get_orientation(sense):
	return sense.get_orientation()

def get_orientation_radians(sense):
	return sense.get_orientation_radians()

def get_orientation_degrees(sense):
	return sense.get_orientation_degrees()
