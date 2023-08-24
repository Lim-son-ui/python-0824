from pyModbusTCP.client import ModbusClient
import time

host1 = "192.168.10.200"
port1 = 502

c1 = ModbusClient()

c1.host(host1)
c1.port(port1)
c1.unit_id(0x28)

while True:

    if not c1.is_open():
        if not c1.open():
            print("unable to connect to" +host1)

    if c1.is_open:
         regs = c1.read_holding_registers(0,32)

    #time.sleep(2)


# ModbusClient.read_holding_registers(,)

# ModbusClient('192.168.27.44',502)
# read_input_registers(start_addr,count,unit=sid)
# read_holding_registers(start_addr,count,unit=sid)
# write_registers(start_addr,value_array,unit=sid)
# read_discrete_inputs(start_addr,bit count,unit=sid)



# async def _handle_holding_registers(client):
#     """Read/write holding registers."""
#     _logger.info("### write holding register and read holding registers")
#     _check_call(await client.write_register(1, 10, slave=SLAVE))
#     rr = _check_call(await client.read_holding_registers(1, 1, slave=SLAVE))
#     assert rr.registers[0] == 10

#     _check_call(await client.write_registers(1, [10] * 8, slave=SLAVE))
#     rr = _check_call(await client.read_holding_registers(1, 8, slave=SLAVE))
#     assert rr.registers == [10] * 8

#     _logger.info("### write read holding registers, using **kwargs")
#     arguments = {
#         "read_address": 1,
#         "read_count": 8,
#         "write_address": 1,
#         "write_registers": [256, 128, 100, 50, 25, 10, 5, 1],
#     }
#     _check_call(await client.readwrite_registers(slave=SLAVE, **arguments))
#     rr = _check_call(await client.read_holding_registers(1, 8, slave=SLAVE))
#     assert rr.registers == arguments["write_registers"]

