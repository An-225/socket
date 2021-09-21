import socket


class Client:
    __ip = str()
    __port = int()
    __bufferIN = str()
    __bufferOUT = str()

    def __init__(self, IP, PORT) -> None:
        self.__ip = IP
        self.__port = PORT
        self.__conn = socket.socket(
            # Tipo de endereçamento (hostname ou IPV4 neste caso)
            socket.AF_INET,
            socket.SOCK_STREAM  # Tipo do socket (TCP neste caso)
        )
        self.__conn.connect((self.__ip, self.__port))

    def __send(self):
        self.__conn.send(self.__bufferOUT.encode("UTF-8"))

    def __recv(self):
        self.__bufferIN = self.__conn.recvfrom(1024)

    def __end(self):
        self.__conn.close()

    def mandar(self):
        self.__bufferOUT = input("Digite sua mensagem:\n")
        if self.__bufferOUT == "quit":
            self.__end()
        else:
            self.__send()

    def receber(self):
        self.__recv()
        print("Mensagem recebida:\n", self.__bufferIN)


def main():
    cliente = Client("192.168.0.105",41990)

    while True:
        cliente.mandar()
        cliente.receber()

main()