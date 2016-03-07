#navigate

class Navigate:

    def __init__(self,motor,imu):
        self.__motor = motor
        self.__imu = imu
        
    def get_direc(self, imu):
        direc = imu.get_heading()
        if (direc <= 198.5):
            direc = "S"
        elif (direc == 315):
            direc = "N"
        elif (direc == 135):
            direc = "E"
        elif (direc >= 251.565 and direc <= 251.6):
            direc = "W"
        return direc
    
  

    def navigate(self,x,y):

        direc = self.get_direc(self.__imu)
        print "Direction = ", direc
        
        if (x == 0 and y == 1):
            if (direc == "N"):
                self.turnLeft();                
            elif (direc == "S"):
                self.turnRight()
            elif (direc == "E"):
                self.turnLeft()
                self.turnLeft()

	    self.__direc = "W"
                
            self.move(4)
            self.turnRight()
            self.__direc = "N"
	    self.move(4)   
            

        elif (x == 0 and y == 2):
            if (direc == "N"):
                self.turnLeft()                
            elif (direc == "S"):
                self.turnRight()
            elif (direc == "E"):
                self.turnLeft()
                self.turnLeft()    
            
            self.__direc = "W"		    
            self.move(2)
            self.turnRight()
            self.__direc = "N"
	    self.move(4)
	 

        elif (x == 0 and y == 3):
            if (direc == "E"):
                self.turnLeft()                
            elif (direc == "W"):
                self.turnRight()
            elif (direc == "S"):
                self.turnLeft()
                self.turnLeft()    
            
            self.__direc = "N"    
            self.move(4)
            
        elif (x == 0 and y == 4):
            if (direc == "E"):
                self.turnLeft()                
            elif (direc == "W"):
                self.turnRight()
            elif (direc == "S"):
                self.turnLeft()
                self.turnLeft()    
             
	    self.__direc = "N"   
            self.move(4)
            self.turnRight()
            self.__direc = "E"
            self.move(1)
         

        elif (x == 0 and y == 5):
            if (direc == "S"):
                self.turnLeft()                
            elif (direc == "N"):
                self.turnRight()
            elif (direc == "W"):
                self.turnLeft()
                self.turnLeft()    
            
	    self.__direc = "E"    
            self.move(3)
            self.turnLeft()
	    self.__direc = "N"
            self.move(4)
	   	

        elif (x == 1 and y == 0):
            if (direc == "W"):
                self.turnLeft()                
            elif (direc == "E"):
                self.turnRight()
            elif (direc == "N"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "S"    
            self.move(4)
            self.turnLeft()
            self.__direc = "W"
            self.move(4)
	   
        
        elif ((x == 1 and y == 2) or (x==2 and y==3) or (x==4 and y==5) or (x==10 and y==9) or (x==9 and y==11) or (x==11 and y==7)):
            if (direc == "S"):
                self.turnLeft()                
            elif (direc == "N"):
                self.turnRight()
            elif (direc == "W"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "E"    
            self.move(2)
            
        elif ((x == 2 and y == 1) or (x==3 and y==2) or (x==5 and y==4) or (x==9 and y==10) or (x==11 and y==9) or (x==7 and y==11)):
            if (direc == "N"):
                self.turnLeft()                
            elif (direc == "S"):
                self.turnRight()
            elif (direc == "E"):
                self.turnLeft()
                self.turnLeft()
            self.__direc = "W"    
            self.move(2)

        elif ((x == 2 and y == 9) or (x==1 and y==10) or (x==5 and y==6)):
            if (direc == "E"):
                self.turnLeft()                
            elif (direc == "W"):
                self.turnRight()
            elif (direc == "S"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "N"    
            self.move(3)


        elif (x == 2 and y == 0):
            if (direc == "W"):
                self.turnLeft()                
            elif (direc == "E"):
                self.turnRight()
            elif (direc == "N"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "S"    
            self.move(4)
            self.turnLeft()
            self.__direc = "E"
            self.move(2)
	   	

        elif (x == 3 and y == 0):
            if (direc == "W"):
                self.turnLeft()                
            elif (direc == "E"):
                self.turnRight()
            elif (direc == "N"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "S"    
            self.move(4)


        elif ((x == 3 and y == 4) or (x==7 and y==6)):
            if (direc == "S"):
                self.turnLeft()                
            elif (direc == "N"):
                self.turnRight()
            elif (direc == "W"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "E"    
            self.move(1)

        elif (x == 3 and y == 8):
            if (direc == "E"):
                self.turnLeft()                
            elif (direc == "W"):
                self.turnRight()
            elif (direc == "S"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "N"    
            self.move(2)

        elif ((x == 4 and y == 3) or (x == 6 and y == 7)):
            if (direc == "N"):
                self.turnLeft()                
            elif (direc == "S"):
                self.turnRight()
            elif (direc == "E"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "W"    
            self.move(1)

        elif (x == 4 and y == 7):
            if (direc == "S"):
                self.turnLeft()                
            elif (direc == "N"):
                self.turnRight()
            elif (direc == "W"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "E"     
            self.move(2)
            self.turnLeft()
            self.__direc = "N"
            self.move(3)
	    

        elif (x == 4 and y == 0):
            if (direc == "W"):
                self.turnLeft()                
            elif (direc == "E"):
                self.turnRight()
            elif (direc == "N"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "S"    
            self.move(4)
            self.turnRight()
            self.__direc = "W"
            self.move(1)
	    


        elif (x == 5 and y == 0):
            if (direc == "W"):
                self.turnLeft()                
            elif (direc == "E"):
                self.turnRight()
            elif (direc == "N"):
                self.turnLeft()
                self.turnLeft()    
            
            self.__direc = "S"    
            self.move(4)
            self.turnRight()
            self.__direc = "W"
            self.move(3)
	    

        elif ((x == 6 and y == 5) or (x==9 and y==2) or (x==10 and y==1)):
            if (direc == "W"):
                self.turnLeft()                
            elif (direc == "E"):
                self.turnRight()
            elif (direc == "N"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "S"    
            self.move(3)


        elif (x == 7 and y == 4):
            if (direc == "W"):
                self.turnLeft()                
            elif (direc == "E"):
                self.turnRight()
            elif (direc == "N"):
                self.turnLeft()
                self.turnLeft()    
            
            self.__direc = "S"    
            self.move(3)
            self.turnRight()
	    self.__direc = "W"
            self.move(1)


        elif (x == 8 and y == 3):
            if (direc == "W"):
                self.turnLeft()                
            elif (direc == "E"):
                self.turnRight()
            elif (direc == "N"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "S"    
            self.move(2)

        elif (x == 8 and y == 11):
            if (direc == "E"):
                self.turnLeft()                
            elif (direc == "W"):
                self.turnRight()
            elif (direc == "S"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "N"    
            self.move(1)


        elif (x == 11 and y == 8):
            if (direc == "W"):
                self.turnLeft()                
            elif (direc == "E"):
                self.turnRight()
            elif (direc == "N"):
                self.turnLeft()
                self.turnLeft()    
            self.__direc = "S"    
            self.move(1)


    def turnRight(self):
        #turn 90
        #self.__motor.turnRight()
        print "turn right"

    def turnLeft(self):
        #turn 90
        #self.__motor.turnLeft()
        print "turn left"

    def move(self,steps):
        #self.move forward
        #self.__motor.move(steps)
        print "moving by ", steps, "steps"


