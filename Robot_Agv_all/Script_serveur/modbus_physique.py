import minimalmodbus

def run_modbus_client():
    # Create a Modbus instrument instance
    instrument = minimalmodbus.Instrument('COM1', 1)  # Replace 'COM1' with your serial port name, and 1 with the device address

    # Configure communication parameters
    instrument.serial.baudrate = 9600
    instrument.serial.bytesize = 8
    instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
    instrument.serial.stopbits = 1
    instrument.serial.timeout = 1  # Timeout in seconds

    try:
        # Read a holding register
        address1 = 0
        address2=1
        address3=5
        
        value = instrument.read_register(address1, functioncode=3)
        print("Value read from simulator:", value)

        # Write to a holding register
        value_to_write = 12366
        instrument.write_register(address2, value_to_write, functioncode=16)
        print("Value written to simulator:", value_to_write)
        instrument.write_register(address3, value_to_write, functioncode=16)
        print("Value written to simulator:", value_to_write)
    except Exception as e:
        print("Error:", e)

def main():
    run_modbus_client()

if __name__ == "__main__":
    main()
