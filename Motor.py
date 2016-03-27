import RPi.GPIO as GPIO
import time
import threading

class Motor(threading.Thread):

      
    def __init__(self, obstacle):
	self.__obstacle = obstacle

    
    def setup(self):
        
        GPIO.setmode(GPIO.BCM)
        print "Setting up Motor Pins"

        #common pins - EN, MS1,MS2,MS3
        GPIO.setup(14, GPIO.OUT)
        GPIO.output(14, GPIO.LOW)

        #DIR Pins - Motor 1 = 7, Motor 2 = 8
        GPIO.setup(7, GPIO.OUT)
        GPIO.output(7, GPIO.LOW)
        GPIO.setup(8, GPIO.OUT)
        GPIO.output(8, GPIO.LOW)
        
        #Motor STP Pins: Motor 1 = 15, Motor 2 = 12
        GPIO.setup(15, GPIO.OUT)
        GPIO.output(15, GPIO.LOW)
        GPIO.setup(12, GPIO.OUT)
        GPIO.output(12, GPIO.LOW)
   	#LED Pins
	GPIO.setup(21, GPIO.OUT)
	GPIO.output(21, GPIO.LOW)      
            
    def move(self,num):
        
        steps =0               
	
	#Forward Direction 
        GPIO.output(7, GPIO.HIGH) #Setting directions Right
        GPIO.output(8, GPIO.LOW) #Left
	count = 0

        from Imu import IMU #Get direction
	imu = IMU()
	print imu.get_heading()
        
	while(steps != num*255):
            ##int( "Step ", steps) #255	    
	    count = count + 1
	    if (count%20==0):
	       	if (self.__obstacle.get_distance() < 30):
		    GPIO.output(21, GPIO.HIGH)
		    time.sleep(5)		
	   
            #print "Motor 15: ", steps    	     
            GPIO.output(15, GPIO.HIGH)	    
	    #print "Motor 12L ", steps
            GPIO.output(12, GPIO.HIGH)	    		
            time.sleep(0.010)	    
            GPIO.output(15,GPIO.LOW)
            GPIO.output(12,GPIO.LOW)	    
            time.sleep(0.010)
            steps = steps +1
        
        GPIO.output(7, GPIO.LOW)
        GPIO.output(8, GPIO.LOW)
##       # GPIO.cleanup()
    
    def turnLeft(self):
        steps = 0
        
        GPIO.output(7, GPIO.LOW) #Setting directions
        GPIO.output(8, GPIO.LOW)
        print "Moving the wheels turning right"
        while(steps != 110):
##            print( "Step ", steps)
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(12, GPIO.HIGH)
            time.sleep(0.005)
            GPIO.output(15,GPIO.LOW)
            GPIO.output(12,GPIO.LOW)
            time.sleep(0.005)
            steps = steps +1
            
        GPIO.output(7, GPIO.LOW)
        GPIO.output(8, GPIO.LOW)
##        GPIO.cleanup()

    def turnRight(self):
        steps = 0

        GPIO.output(7, GPIO.HIGH) #Setting directions
        GPIO.output(8, GPIO.HIGH)
        print "Moving the wheels turning left"
        while(steps != 110):
##            print( "Step ", steps)
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(12, GPIO.HIGH)
            time.sleep(0.005)
            GPIO.output(15,GPIO.LOW)
            GPIO.output(12,GPIO.LOW)
            time.sleep(0.005)
            steps = steps +1
            
        GPIO.output(7, GPIO.LOW)
        GPIO.output(8, GPIO.LOW)
##        GPIO.cleanup()  

    def orientRight(self):
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(8, GPIO.HIGH)
	
	count = 0
	while (count < 3):
	    GPIO.output(15, GPIO.HIGH)
	    GPIO.output(12, GPIO.HIGH)
	    time.sleep(0.005)
	    GPIO.output(15, GPIO.LOW)
	    GPIO.output(12, GPIO.LOW)
	    time.sleep(0.005)
	    count = count + 1

    def orientLeft(self):
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.LOW)
	
	count = 0
	while (count < 3):
	    GPIO.output(15, GPIO.HIGH)
	    GPIO.output(12, GPIO.HIGH)
	    time.sleep(0.005)
	    GPIO.output(15, GPIO.LOW)
	    GPIO.output(12, GPIO.LOW)
	    time.sleep(0.005)
            count = count + 1

#from Imu import IMU
#imu = IMU()
from obstacle import Obstacle
o = Obstacle()
motor = Motor(o)
motor.setup()

#motor.turnLeft()

#for x in range(0,4):
    #print imu.get_heading()
    #motor.turnRight()


motor.move(5)
motor.turnRight()
motor.move(3)
motor.turnLeft()
motor.move(7)
