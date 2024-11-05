import tkinter as tk
from tkinter import ttk
import socket

def run_modbus_client():
    HOST = '127.0.0.1'  # Server IP address
    PORT = 65432  # Server port

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            print("Connected to the server.")

            # Get number of missions from combobox
            num_missions = int(num_missions_combobox.get())

            # List to store mission data
            mission_data_list = []

            # Input details for each mission
            for i in range(num_missions):
                station = int(station_entries[i].get())
                operation = operation_entries[i].get()

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
            response_label.config(text=response)
    except Exception as e:
        print(f"An error occurred: {e}")
        response_label.config(text=str(e))

# Create Tkinter window
window = tk.Tk()
window.title("Modbus Client")

# Number of missions combobox
num_missions_label = tk.Label(window, text="Number of missions:")
num_missions_label.grid(row=0, column=0)
num_missions_combobox = ttk.Combobox(window, values=[str(i) for i in range(1, 11)])
num_missions_combobox.grid(row=0, column=1)

# Mission details entries
station_entries = []
operation_entries = []

def create_mission_entries():
    num_missions = int(num_missions_combobox.get())
    for i in range(num_missions):
        station_label = tk.Label(window, text=f"Station {i + 1}:")
        station_label.grid(row=i+1, column=0)
        station_entry = tk.Entry(window)
        station_entry.grid(row=i+1, column=1)
        station_entries.append(station_entry)

        operation_label = tk.Label(window, text="Operation (1 for loading, 0 for unloading):")
        operation_label.grid(row=i+1, column=2)
        operation_entry = tk.Entry(window)
        operation_entry.grid(row=i+1, column=3)
        operation_entries.append(operation_entry)

create_mission_entries_button = tk.Button(window, text="Create Mission Entries", command=create_mission_entries)
create_mission_entries_button.grid(row=0, column=2)

# Run Modbus client button
run_button = tk.Button(window, text="Run Modbus Client", command=run_modbus_client)
run_button.grid(row=12, column=0, columnspan=4)

# Response label
response_label = tk.Label(window, text="")
response_label.grid(row=13, column=0, columnspan=4)

window.mainloop()
