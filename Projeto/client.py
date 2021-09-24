import socket

class Client:
    ip = str()
    port = int()

    bufferIN = str()
    bufferOUT = str()

    def __init__(self, ip: str, port: int, path: str) -> None:
        self.ip = ip
        self.port = port
        self.path = path

    def connect(self) -> None:
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.ip,self.port))

    def receive(self,size) -> None:
        self.bufferIN = (self.connection.recvfrom(size))[0].decode("UTF-8")

    def send(self) -> None:
        self.connection.send(self.bufferOUT.encode("UTF-8"))

    def newNote(self) -> None:
        self.bufferOUT = "NEW"
        self.send()
        self.bufferOUT = input("Enter the name: ")
        self.send()
        self.bufferOUT = input("Enter the text: ")
        self.send()


    def allNotes(self) -> None:
        self.bufferOUT = "All"
        self.receive(1024)
        print(self.bufferOUT)

    def delNote(self) -> None:
        self.bufferOUT = input("Enter the id: ")
        self.send()