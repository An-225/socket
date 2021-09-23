import socket
from database import Database

class Server:
    IP = str()
    port = int()
    #server obj
    #conn

    def __init__(self,ip:str, port:int,path:str) -> None:
        data = Database(path)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((ip, port))
        self.server.listen(1)
        self.connection, clientIP = self.server.accept()

