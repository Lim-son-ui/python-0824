from pyModbusTCP.server import ModbusServer,DataBank

server = ModbusServer("172.29.3.251",502,no_block=True)

try:
    print("start server..")
    server.start()
    print("server is online")
    while True:
        # DataBank.set_words(0,[int(uniform(0,100))])
        if state != DataBank.get_words(1):
            state = DataBank.get_words(1)
            print("value of register 1 has changed to " + str(state))
            # time.sleep(0.5)
        continue
except:
    print("shutdown server...")
    server.stop()
    print("server is offline")