import minimalmodbus
import socket

def handle_client(client_socket, instrument):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        command = data.decode().strip()

        # Execute the command received from the client
        if command.startswith("write_register"):
            parts = command.split(" ")
            if len(parts) >= 2:
                num_missions = int(parts[1])
                mission_data = client_socket.recv(1024)  # Receive mission data
                try:
                    # Convert mission data bytes to a list of integers
                    mission_data_list = list(mission_data)
                    # Write the mission data to the registers
                    instrument.write_registers(20, mission_data_list)
                    response = f"{num_missions} mission(s) written to registers."
                except Exception as e:
                    response = f"Error writing missions to registers: {str(e)}"
            else:
                response = "Invalid command format"
        else:
            response = "Invalid command"

        client_socket.sendall(response.encode())

def run_modbus_server():
    # Create a Modbus instrument instance
    instrument = minimalmodbus.Instrument('COM1', 1)  # Replace 'COM1' with your serial port name, and 1 with the device address

    # Configure communication parameters
    instrument.serial.baudrate = 9600
    instrument.serial.bytesize = 8
    instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
    instrument.serial.stopbits = 1
    instrument.serial.timeout = 1  # Timeout in seconds

    # Set up TCP/IP server to listen for commands from another client
    HOST = '127.0.0.1'  # localhost
    PORT = 65432  # Arbitrary non-privileged port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print("Waiting for connection...")
        client_socket, client_address = server_socket.accept()
        print("Connected to:", client_address)

        with client_socket:
            handle_client(client_socket, instrument)

def main():
    run_modbus_server()

if __name__ == "__main__":
    main()
