import socket

ip = "192.168.0.105"
port = 41990

# Tipo de endereçamento (hostname ou IPV4 neste caso)
# Tipo do socket (TCP neste caso)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(1)

print(f"Servidor disponivel em {ip}:{port}")
conn, source = server.accept()
print(f"Conectado em: {source}")

while True:
    # Recebendo
    print("Esperando mensagem...")
    bufferIN = conn.recv(1024)
    if bufferIN.decode("UTF-8") == "quit":
        print("Cliente encerrou a conexao!")
        print("Aguardando um novo cliente...")
        conn, source = server.accept()
        print(f"Conectado em: {source}")
    else:
        print("Mensagem recebida:\n", bufferIN.decode("UTF-8"))

    # Mandando
    bufferOUT = input("Digite sua mensagem:\n")
    if bufferOUT == "quit":
        print("Fechando conexao e servidor!")
        conn.send(bufferOUT.encode("UTF-8"))
        conn.close()
        server.close()
        break
    else:
        conn.send(bufferOUT.encode("UTF-8"))
