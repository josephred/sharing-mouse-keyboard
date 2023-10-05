# SERVER
import socket

def main():
    host = '0.0.0.0'  # Escucha en todas las interfaces de red
    port = 5000  # Elige un puerto que no esté en uso

    # Crea un socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((host, port))
    my_socket.listen(1)

    print("Servidor escuchando en el puerto {}".format(port))

    while True:
        conn, addr = my_socket.accept()
        print("Conexión establecida con: " + str(addr))

        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("Recibido del cliente: " + str(data))

            data = str(data).upper()
            print("Enviando: " + str(data))
            conn.send(data.encode())

        conn.close()

if __name__ == '__main__':
    main()
