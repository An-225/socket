import socket

ip = "192.168.0.105"
port = 41990

# Tipo de endereçamento (hostname ou IPV4 neste caso)
# Tipo do socket (TCP neste caso)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"Conectando em {ip}:{port}...")
client.connect((ip, port))
print("Conectado!")

while True:
    # Mandando
    bufferOUT = input("Digite sua mensagem:\n")
    if bufferOUT == "quit":
        client.send(bufferOUT.encode("UTF-8"))
        print("Fechando conexao!")
        client.close()
        break
    else:
        client.send(bufferOUT.encode("UTF-8"))

    # Recebendo
    print("Esperando mensagem...")
    bufferIN = client.recvfrom(1024)
    if bufferIN[0].decode("UTF-8") == "quit":
        print("Servidor fechou conexao!!")
        break
    else:
        print("Mensagem recebida:\n", bufferIN[0].decode("UTF-8"))
