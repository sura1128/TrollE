import time
import RPi.GPIO as GPIO


class Obstacle:

   def setup(self):
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(21, GPIO.OUT)

   def ping(self):
      count = 0
      total = 0
      
      GPIO.setup(11, GPIO.OUT)

      GPIO.output(11, 0)

      time.sleep(0.000002)

      GPIO.output(11, 1)

      time.sleep(0.000002)

      GPIO.output(11, 0)

      GPIO.setup(11, GPIO.IN)

      while GPIO.input(11)==0:
         start = time.time()

      while GPIO.input(11)==1:
         end = time.time()
	 

      duration = end - start
      distance = duration*34000/2
      if distance <= 30:
          GPIO.output(21, GPIO.HIGH)
	  time.sleep(0.05)
      GPIO.output(21, GPIO.LOW)		      

      return distance

   def get_distance(self):
      distance = self.ping()
            
      return distance

o = Obstacle()
o.setup()
#while True:
   #print "distance = ", o.get_distance()
   #time.sleep(0.05)
