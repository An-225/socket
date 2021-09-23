import socket
from database import Database
from note import Note


class Server:
    ip = str()
    port = int()

    bufferIN = str()
    bufferOUT = str()

    path = str()

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
        self.bufferIN = ((self.connection.recv(3)).decode("UTF-8")).upper()

        if "NEW" in self.bufferIN:
            self.newNote()
        if "ALL" in self.bufferIN:
            pass
        if "DEL" in self.bufferIN:
            pass

    def newNote(self):
        temp = Note()
        
        temp.name = self.connection.recv(128).decode("UTF-8")
        temp.text = self.connection.recv(1024).decode("UTF-8")

        self.data.saveNote(temp)
