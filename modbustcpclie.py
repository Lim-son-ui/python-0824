from pyModbusTCP.client import ModbusClient

#client = ModbusClient(host="192.168.10.200",port=502,unit_id=0x28)
# client = ModbusClient(host="172.27.10.104",port=502,unit_id=0x28)
client = ModbusClient(host="192.168.10.100",port=502,unit_id=0x01)

print(client)
client.open()
# if not client.is_open():
#     if not client.open():
#         print("unable to connect")

print(str(client.read_holding_registers(0x03e8,5)))

#print(str(client.read_holding_registers(4994,2)))
#print(str(client.read_holding_registers(0x1018,30)))

# ,type='uint16'
# client.read_holding_registers(0)
# client.read_holding_registers(0)
# client.read_holding_registers(0)



# print(client.write_single_register(1,123))
# client.write_single_register(1,124)
# client.write_multiple_registers(1,[1,2,3])

client.close()
