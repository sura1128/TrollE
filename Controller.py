#Controller File

class Controller:

    
    def __init__(self, prodMap):
        self.__prodMap = prodMap

    def setup(self):
        from ProductList import ProductList
        prodList = ProductList()
        prodList.set_prod_map({})

        with open("products.txt") as f:            
            lines = f.readlines()
        f.closed

        for x in range(0,len(lines)-1):
            words = lines[x].rstrip().split(',')
            from Product import Product
            prod = Product(words[0], words[1], words[2],x)
            prodList.populate_map(words[0], prod)
        
        self.__prodMap = prodList.get_product_map()

    def get_product_map(self):        
        return self.__prodMap

    def get_uid_from_map(self, choice):
        return self.__prodMap[choice].get_uid()

    def get_index_from_uid(self, uid):
        for key,value in self.__prodMap.iteritems():
            if (value.get_uid() == uid):
                index = value.get_index()
        return index
        
    def get_current(self):
        #NFC Reading
        from NFC import NFC
        nfc = NFC()
        return nfc.read_data()

    def get_route(self, destination):
        destination = self.get_uid_from_map(destination)
        current_pos = self.get_current();
        
        dest_id = self.get_index_from_uid(destination)
        curr_id = self.get_index_from_uid(current_pos)
        print "dest id = ", dest_id 
        print "curr id = ", curr_id
       

        from Route import Route
        route = Route(curr_id, dest_id, [], [], [])
        path = route.findRoute()

        from Imu import IMU
	imu = IMU()
	print "imu reading = ", imu.get_heading()

        print "setting up motors..."
        from Motor import Motor
        motor = Motor()
	motor.setup()       

        print "setting up navigation..."
	from navigate import Navigate
        navigator = Navigate(motor,imu)       
    
        
        for x in range(0,len(path)-1):
            #print (path[x],path[x+1])
            navigator.navigate(path[x], path[x+1])
        

