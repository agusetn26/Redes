import socket

def main():
    host = '127.0.0.1'
    port = 23162

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)

        print("Servidor escuchando en {}:{}".format(host, port))

        client_socket, addr = server_socket.accept()
        print("Cliente conectado desde:", addr)

        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print("Cliente:", data)
            response = input("Servidor: ")
            client_socket.sendall(response.encode())

if __name__ == "__main__":
    main()