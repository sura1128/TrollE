#Sensor data - RFID
# Reads data from NFC Tags.

import binascii
import sys

import Adafruit_PN532 as PN532

class NFC:

    def read_data(self): 
	
        # Configuration for a Raspberry Pi:
        CS1   = 18
        MOSI1 = 23
        MISO1 = 24
        SCLK1 = 25

        # Create an instance of the PN532 class.
        pn5321 = PN532.PN532(cs=CS1, sclk=SCLK1, mosi=MOSI1, miso=MISO1)

        # Call begin to initialize communication with the PN532.  Must be done before
        # any other calls to the PN532!
        pn5321.begin()

        # Get the firmware version from the chip and print it out.
        ic, ver, rev, support = pn5321.get_firmware_version()
        print 'Found PN532 with firmware version: {0}.{1}'.format(ver, rev)

        pn5321.SAM_configuration()
        print "Waiting for Mifare Tag..."

        dest_uid1 = ""

        while True:

            #print("Finding UID")
            uid1 = pn5321.read_passive_target()
            if uid1 is None:
                continue
            else:
		if uid1 is not None:
                	dest_uid1 = binascii.hexlify(uid1)
                	print 'Found card with UID: 0x{0}'.format(binascii.hexlify(uid1))
                break
    	return dest_uid1

#nfc = NFC()
#print nfc.read_data()
