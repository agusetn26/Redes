import socket

def main():
    host = '127.0.0.1'
    port = 23162

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        while True:
            message = input("Cliente: ")
            client_socket.sendall(message.encode())

            response = client_socket.recv(1024).decode()
            print("Servidor:", response)

if __name__ == "__main__":
    main()
