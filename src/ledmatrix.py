#! /usr/bin/env python

import time
import rospy
from sense_hat import SenseHat
import ros_sensehat.ledmatrixhelper

sense = SenseHat()
#sense.set_rotation(0)
sense.clear()

rosfrequency = 500

colorarray = ros_sensehat.ledmatrixhelper.initialize_plain_color()
pixels = ros_sensehat.ledmatrixhelper.initialize_rainbow_color()

def allcolor():
	global colorarray
	global rosfrequency
	while not rospy.is_shutdown():
		#rospy.loginfo(rospy.get_caller_id() + " r is %s, g is %s, b is %s" % (colorarray[0], colorarray[1], colorarray[2]))
		sense.clear(colorarray)
		dir = sense.get_compass()
		#rospy.loginfo(rospy.get_caller_id() + " dir is %s" % dir)
		ros_sensehat.ledmatrixhelper.pix_next_color( colorarray )
		rate.sleep()

def rainbow():
	global pixels
	global rosfrequency
	while not rospy.is_shutdown():
		for pix in pixels:
			ros_sensehat.ledmatrixhelper.pix_next_color( pix )

		sense.set_pixels(pixels)
		rate.sleep()


if __name__ == '__main__':
	rospy.init_node('ros_sensehat_ledcycle', anonymous=True)
	rate = rospy.Rate(rosfrequency)
	try:
		#allcolor()
		rainbow()
		rospy.loginfo(rospy.get_caller_id() + " Quit, switch off matrix")
		sense.clear()
	except rospy.ROSInterruptException:
		sense.clear()
		pass
