import serial


rid = serial.Serial(port='COM6',baudrate=38400,parity=serial.PARITY_NONE
                     ,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,
                     timeout=1)

get = rid.read_all()


data = str(get)

print(data)