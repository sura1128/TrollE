#Orientation File

import RPi.GPIO as GPIO
import time

class Orientation:

    def __init__(self, dir):
	self.__dir = dir

    def orient(self):
        from Motor import Motor
	motor = Motor()
	motor.setup()
	dir = self.__dir

	from Imu import IMU
	imu = IMU()
	
	# direction
	# Oient to North
	if (dir > 0 and dir < 45):
	    while (dir > 2):
	        motor.orientLeft()
		dir = imu.get_heading()
	if (dir > 315 and dir < 360):
	    while (dir < 358):
		motor.orientRight()
		dir = imu.get_heading()

	#Orient to East
	if (dir > 45 and dir < 90):
	    while (dir < 88):
		motor.orientRight()
		dir = imu.get_heading()
	if (dir < 135 and dir > 90):
	    while (dir > 92):
		motor.orientLeft()
		dir = imu.get_heading()


	#Orient to West
	if (dir > 135 and dir < 180):
	    while (dir < 178):
		motor.orientRight()
		dir = imu.get_heading()
	if (dir < 225 and dir > 180):
	    while (dir > 182):
		motor.orientLeft()
		dir = imu.get_heading()

	#Orient to South
	if (dir > 225 and dir < 270):
	    while (dir < 268):
		motor.orientRight()
		dir = imu.get_heading()
	if (dir > 270 and dir < 315):
	    while (dir > 272):
		motor.orientLeft()
		dir = imu.get_heading()
 

from Imu import IMU
imu = IMU()
o = Orientation(imu.get_heading())
o.orient()


	    
	        
		
