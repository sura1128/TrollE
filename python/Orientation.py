#Orientation File

import RPi.GPIO as GPIO
import time

class Orientation:

    def __init__(self, dir):
	self.__dir = dir

    def orient(self, motor, imu):
	motor = motor
        motor.setup()
	imu = imu
	dir = imu.get_heading()
	
	
		
	#WEST += 330
	#NORTH += 97
	#EAST += 160
	#SOUTH  += 225

	#WEST-L += 275
	#WEST-R += 15

	#NORTH-L += 55
	#NORTH-R += 145

	#EAST-L += 115
	#EAST-R += 205

	#SOUTH-L += 180
	#SOUTH-R += 275 	
		

	# Oient to North
	if (dir > 15 and dir < 97):
	    print "Here"
	    while (dir < 95):
	        motor.orientRight()
		dir = imu.get_heading()
	if (dir > 97 and dir < 142):
	    while (dir > 99):
		motor.orientLeft()
		dir = imu.get_heading()

	#Orient to East
	if (dir > 115 and dir < 160):
	    while (dir < 158):
		motor.orientRight()
		dir = imu.get_heading()
	if (dir > 160 and dir < 205):
	    while (dir > 162):
		motor.orientLeft()
		dir = imu.get_heading()


	#Orient to South
	if (dir > 180 and dir < 225):
	    while (dir < 223):
		motor.orientRight()
		dir = imu.get_heading()
	if (dir > 225 and dir < 275):	    
	    while (dir > 227):
		motor.orientLeft()
		dir = imu.get_heading()

	#Orient to West
	if (dir > 275 and dir < 320):
	    while (dir < 318):
		motor.orientRight()
		dir = imu.get_heading()
	if ((dir > 320 and dir < 360) or (dir>0 and dir < 15)):
     	    if (dir > 0 and dir < 15):
	       	while(dir <= 360):
	     	    motor.orientLeft()
	     	    dir = imu.get_heading()    
	    while (dir > 322):
		motor.orientLeft()
		dir = imu.get_heading()
	     	    
	    







	    
	        
		
