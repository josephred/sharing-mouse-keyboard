# CLIENTE
import socket

def main():
    host = '192.168.x.x'  # La dirección IP del servidor
    port = 5000  # El mismo puerto que el servidor

    # Crea un socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((host, port))

    message = input(" -> ")

    while message != 'q':
        my_socket.send(message.encode())
        data = my_socket.recv(1024).decode()

        print('Recibido del servidor: ' + data)

        message = input(" -> ")

    my_socket.close()

if __name__ == '__main__':
    main()
