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

        print("Starting server...", end='')
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.ip, self.port))
        self.server.listen(1)
        print("OK!")
        print(f"Server online in {self.ip}:{self.port}")

        print("Waiting a client...")
        self.connection, self.clientIP = self.server.accept()
        print(f"Client {self.clientIP[0]}:{self.clientIP[1]} connected!")

    def close(self) -> None:
        self.bufferOUT = "BYE"
        self.send()

        self.server.close()
        del self.data

    def receive(self, size) -> None:
        self.bufferIN = (self.connection.recv(size)).decode("UTF-8")
        if "BYE" in self.bufferIN:
            print("Client disconnected!!!")
            print("Waiting a new client...")
            self.connection, self.clientIP = self.server.accept()
            print(f"New client {self.clientIP[0]}:{self.clientIP[1]} connected!")

    def send(self) -> None:
        self.connection.send(self.bufferOUT.encode("UTF-8"))

    def recvGO(self) -> None:
        self.receive(3)
        if not("GO!" in self.bufferIN):
            self.wait()

    def sendGO(self) -> None:
        self.bufferOUT = "GO!"
        self.send()

    def run(self) -> None:
        self.receive(3)

        if "NEW" in self.bufferIN:
            self.newNote()
        if "ALL" in self.bufferIN:
            self.allNotes()
        if "DEL" in self.bufferIN:
            self.delNote()

    def newNote(self) -> None:
        temp = Note()

        self.receive(128)
        temp.name = self.bufferIN
        self.receive(1024)
        temp.text = self.bufferIN

        self.data.saveNote(temp)

    def allNotes(self) -> None:
        notes = self.data.querryAll()

        self.bufferOUT = str(len(notes))
        self.send()

        self.recvGO()

        for note in notes:
            strNote = str(note.toTuple())
            self.bufferOUT = str(len(strNote))
            self.send()

            self.recvGO()

            self.bufferOUT = strNote
            self.send()

            self.recvGO()

    def delNote(self) -> None:
        temp = Note()

        self.receive(8)
        temp.id = int(self.bufferIN)

        self.data.deleteNote(temp)
