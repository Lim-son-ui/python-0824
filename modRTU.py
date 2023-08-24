from atexit import register
from pymodbus.client import ModbusSerialClient as modbusclient
# import serial

# device = serial.Serial(port='COM6',baudrate=38400,bytesize=8,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE)
client = modbusclient(port='COM6',baudrate=38400,TimeoutError=1)
# ,TimeoutError=1,parity=None
# ,bytesize=8,parity=None,stopbits=1
#stopbits=1
# modbusclient(,)
client.connect()

# read=client.read_holding_registers(address=0x0067,count=3,id=0x01)
read=client.read_holding_registers(address=0x0067,count=3,id=0x01)
# read=client.read_holding_registers(address=0x0320,count=10,id=0x64)
# read=client.read_holding_registers(address=0x0009,count=3,id=0x01)
# read=client.read_holding_registers(address=0x0320,count=1,id=0x64)
# read=client.read_holding_registers(address=0x0320,count=20,slave=0x64)
# read = client.read_holding_registers(address=0x0000,count=2,id=0x01)

# print(read)
# print(str(read))
#print(read.decode)
print(read.__getattribute__)
print(str(read))