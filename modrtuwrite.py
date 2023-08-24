from pymodbus.client import ModbusSerialClient as modbusclient

client = modbusclient(port='COM8',baudrate=38400,TimeoutError=1,stopbits=1,parity='N')
# modbusclient(,)
client.connect()

fvalue = 30
fvalue *= 10

# read=client.read_holding_registers(address=0x0000,count=3,id=0x01)
#目前在抓id要怎麼寫還不確定



# write = client.write_register(0X034e,65280,slave=0X64)

# write = client.write_register(0X012d,2730,slave=0X11)

# write = client.write_register(0X0065,65280,slave=0X01)

# write = client.write_register(0X0067,65506,slave=0X01)
# write = client.write_register(0X0067,30,slave=0X01)

write = client.write_register(0X0067,0,slave=0X01)
# client.write_registers()


print(str(write))