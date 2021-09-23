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

    def open(self) -> None:
        self.data = Database(self.path)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(1)
        self.connection, clientIP = self.server.accept()

    def receive(self) -> None:
        self.bufferIN = ((self.connection.recv(3)).decode("UTF-8")).upper()

        if "NEW" in self.bufferIN:
            self.newNote()
        if "ALL" in self.bufferIN:
            self.allNotes()
        if "DEL" in self.bufferIN:
            self.delNote()

    def send(self) -> None:
        self.connection.send(self.bufferOUT.encode("UTF-8"))

    def newNote(self) -> None:
        temp = Note()
        
        temp.name = self.connection.recv(128).decode("UTF-8")
        temp.text = self.connection.recv(1024).decode("UTF-8")

        self.data.saveNote(temp)

    def allNotes(self) -> None:
        notes = self.data.querryAll()

        self.bufferOUT = str(notes).encode("UTF-8")
        self.send()

    def delNote(self) -> None:
        temp = Note()

        temp.id = int(self.connection.recv(8).decode("UTF-8"))

        self.data.deleteNote(temp)