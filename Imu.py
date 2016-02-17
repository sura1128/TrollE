import time, math

class IMU:

    def __init__(self):
        print "IMU is initialized."
    
    def twos_comp_combine(self, msb, lsb):
        twos_comp = 256*msb + lsb
        if twos_comp >= 32768:
            return twos_comp - 65536
        else:
            return twos_comp

    def get_heading(self):
        from smbus import SMBus
        busNum = 1
        b = SMBus(busNum)


        LSM = 0x1d

        LSM_WHOAMI_ADDRESS = 0x0F
        LSM_WHOAMI_CONTENTS = 0b1001001

        LSM_CTRL_0 = 0x1F
        LSM_CTRL_1 = 0x20
        LSM_CTRL_2 = 0x21
        LSM_CTRL_3 = 0x22
        LSM_CTRL_4 = 0x23
        LSM_CTRL_5 = 0x24
        LSM_CTRL_6 = 0x25
        LSM_CTRL_7 = 0x26

        LSM_MAG_X_LSB = 0x08
        LSM_MAG_X_MSB = 0x09
        LSM_MAG_Y_LSB = 0x0A
        LSM_MAG_Y_MSB = 0x0B
        LSM_MAG_Z_LSB = 0x0C
        LSM_MAG_Z_MSB = 0x0D


        if (b.read_byte_data(LSM, LSM_WHOAMI_ADDRESS) == LSM_WHOAMI_CONTENTS):
            print ("LSM303D detected successfully on I2C bus ")
        else:
            print ("No LSM303D detected on I2C Bus ")

        b.write_byte_data(LSM, LSM_CTRL_1, 0b1010111)
        b.write_byte_data(LSM, LSM_CTRL_2, 0x00)
        b.write_byte_data(LSM, LSM_CTRL_5, 0b01100100)
        b.write_byte_data(LSM, LSM_CTRL_6, 0b00100000)
        b.write_byte_data(LSM, LSM_CTRL_7, 0x00)

        count = 0;
        total = 0;
        
        
        time.sleep(0.5)
            
        magx = self.twos_comp_combine(b.read_byte_data(LSM, LSM_MAG_X_MSB), b.read_byte_data(LSM, LSM_MAG_X_LSB))
        magy = self.twos_comp_combine(b.read_byte_data(LSM, LSM_MAG_Y_MSB), b.read_byte_data(LSM, LSM_MAG_Y_LSB))
        magz = self.twos_comp_combine(b.read_byte_data(LSM, LSM_MAG_Z_MSB), b.read_byte_data(LSM, LSM_MAG_Z_LSB))

        magdata = (magx, -magy, magz)

        heading = 180* math.atan2(magdata[1], magdata[0])/3.14159265359
        if (heading < 0):
            heading = heading + 360
	#print "Heading ", heading
	return heading
