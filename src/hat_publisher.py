#! /usr/bin/env python

import time
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import String
from geometry_msgs.msg import Vector3
from sense_hat import SenseHat
import ros_sensehat.sensorhelper
import ros_sensehat.ledmatrixhelper

def sensorsDataToVector3(data):
	return Vector3(data['x'], data['y'], data['z'])

if __name__ == '__main__':
	sense = SenseHat()
	rosFrequency = 100
	rosNodeName="ros_sensehat_datapublisher"
	rospy.init_node(rosNodeName, anonymous=True)
	rospy.loginfo(rospy.get_caller_id() + " Initializing node with frequency %s Hz", rosFrequency)
	rate = rospy.Rate(rosFrequency)
	pub_humidity = rospy.Publisher('sensehat/humidity', Float64, queue_size=10)
	pub_temperature = rospy.Publisher('sensehat/temperature', Float64, queue_size=10)
	pub_pressure = rospy.Publisher('sensehat/pressure', Float64, queue_size=10)
	pub_accelerometer = rospy.Publisher('sensehat/accelerometer', Vector3, queue_size=10)
	pub_gyroscope = rospy.Publisher('sensehat/gyroscope', Vector3, queue_size=10)
	pub_magnetometer = rospy.Publisher('sensehat/magnetometer', Vector3, queue_size=10)
	pub_compass = rospy.Publisher('sensehat/compass', Float64, queue_size=10)
	pub_stick = rospy.Publisher('sensehat/stick', String, queue_size=10)
	try:
		rospy.loginfo(rospy.get_caller_id() + " Starting")
		while not rospy.is_shutdown():
			pub_humidity.publish(ros_sensehat.sensorhelper.get_humidity(sense))
			pub_temperature.publish(ros_sensehat.sensorhelper.get_temperature(sense))
			pub_pressure.publish(ros_sensehat.sensorhelper.get_pressure(sense))
			
			pub_accelerometer.publish(sensorsDataToVector3(ros_sensehat.sensorhelper.get_accelerometer(sense)))
			pub_gyroscope.publish(sensorsDataToVector3(ros_sensehat.sensorhelper.get_gyroscope(sense)))
			pub_magnetometer.publish(sensorsDataToVector3(ros_sensehat.sensorhelper.get_magnetometer(sense)))
			pub_compass.publish(ros_sensehat.sensorhelper.get_compass(sense))
			
			stickEvent = ros_sensehat.sensorhelper.get_stick(sense)
			if (stickEvent is not None):
				pub_stick.publish(stickEvent.direction)
			
			rate.sleep()
		
		rospy.loginfo(rospy.get_caller_id() + " Quit")
	except rospy.ROSInterruptException:
		pass
