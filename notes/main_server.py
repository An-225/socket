from server import Server

temp = Server("192.168.122.89", 41990, "data-test.db")

temp.open()

while True:
    try:
        temp.run()
    except:
        temp.close()
