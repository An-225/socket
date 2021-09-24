import socket
from note import Note


class Client:
    ip = str()
    port = int()

    bufferIN = str()
    bufferOUT = str()

    def __init__(self, ip: str, port: int) -> None:
        self.ip = ip
        self.port = port

    def connect(self) -> None:
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.ip, self.port))

    def disconnect(self) -> None:
        self.bufferOUT = "BYE"
        self.send()

        self.connection.close()

    def receive(self, size) -> None:
        self.bufferIN = (self.connection.recvfrom(size))[0].decode("UTF-8")
        if "BYE" in self.bufferIN:
            self.disconnect()
            print("Server closed!!!")
            exit(1)

    def send(self) -> None:
        self.connection.send(self.bufferOUT.encode("UTF-8"))

    def recvGO(self) -> None:
        self.receive(3)
        if not("GO!" in self.bufferIN):
            self.wait()

    def sendGO(self) -> None:
        self.bufferOUT = "GO!"
        self.send()

    def newNote(self) -> None:
        self.bufferOUT = "NEW"
        self.send()
        self.bufferOUT = input("Enter the name: ")
        self.send()
        self.bufferOUT = input("Enter the text: ")
        self.send()

    def allNotes(self) -> None:
        self.bufferOUT = "ALL"
        self.send()

        self.receive(8)

        self.sendGO()

        size = int(self.bufferIN)

        for i in range(size):
            self.receive(8)

            self.sendGO()

            noteSize = int(self.bufferIN)

            self.receive(noteSize)

            self.sendGO()

            tempNote = Note()
            tempNote.fromTuple(eval(self.bufferIN[1:noteSize-1]))
            tempNote.print()

    def delNote(self) -> None:
        self.bufferOUT = "DEL"
        self.send()
        self.bufferOUT = input("Enter the id: ")
        self.send()
