import socket
from database import Database


class Server:
    ip = str()
    port = int()

    bufferIN = str()
    bufferOUT = str()

    path = str()

    # server obj
    # conn

    def __init__(self, ip: str, port: int, path: str) -> None:
        self.ip = ip
        self.port = port
        self.path = path

    def open(self):
        self.data = Database(self.path)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(1)
        self.connection, clientIP = self.server.accept()

    def receive(self):
        self.bufferIN = (self.connection.recv(1024)).upper()

        if "NEW" in self.bufferIN:
            pass
        if "ALL" in self.bufferIN:
            pass
        if "DEL" in self.bufferIN:
            pass
