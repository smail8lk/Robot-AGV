import socket

def run_modbus_client():
    HOST = '127.0.0.1'  # Server IP address
    PORT = 65432  # Server port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("Connected to the server.")

        # Number of missions
        num_missions = int(input("Enter the number of missions: "))

        # List to store mission data
        mission_data_list = []

        # Input details for each mission
        for i in range(num_missions):
            print(f"\nMission {i + 1}:")
            station = int(input("Enter the station number: "))
            operation = input("Enter the operation (1 for loading, 0 for unloading): ")

            # Validate station number and operation
            if 0 <= station <= 255 and operation in ['0', '1']:
                # Append mission data to the list
                mission_data_list.extend([station, int(operation)])
            else:
                print("Invalid input. Please enter a valid station number and operation.")
                return

        # Send the number of missions to the server
        client_socket.sendall(f"write_register {num_missions}".encode())

        # Convert mission data to bytes and send to the server
        mission_data_bytes = bytes(mission_data_list)
        client_socket.sendall(mission_data_bytes)

        # Receive response from the server
        response = client_socket.recv(1024).decode()
        print("Server response:", response)

if __name__ == "__main__":
    run_modbus_client()
