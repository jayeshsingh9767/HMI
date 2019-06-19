import serial

#Using  pyserial Library to establish connection
#Global Variables
ser = 0

#Initialize Serial Port
def serial_connection():
    try:
        global ser
        ser = serial.Serial()
        ser.baudrate = 9600
        ser.port = '/dev/ttyUSB0' #counter for port name starts at 0

        #check to see if port is open or closed
        if (ser.isOpen() == False):
            print ('The Port %d is Open ' + ser.portstr)
            #timeout in seconds
            ser.timeout = 10
            ser.open()

        else:
            print ('The Port %d is closed')
    except Exception as er:
        print(er)


#call the serial_connection() function
# serial_connection()
# ser.write('#W03%OPRUSS%')
# response  = ser.readline()
# print(ser)
# print(response)
