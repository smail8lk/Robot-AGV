import socket

def run_modbus_client():
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432  # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("Connected to server.")

        while True:
            command = input("Enter command (read_register, write_register <address>): ")
            client_socket.sendall(command.encode())

            response = client_socket.recv(1024).decode()
            print("Response from server:", response)

def main():
    run_modbus_client()

if __name__ == "__main__":
    main()
