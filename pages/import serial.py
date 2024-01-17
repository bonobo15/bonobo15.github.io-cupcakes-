import serial
import time

def send_data_via_bluetooth(a, b):
    # Replace 'COMX' with the actual serial port where your HC-05 is connected
    bluetooth_port = '/dev/cu.HC-05-Port'  # On Windows, it might look like 'COM4'
    baud_rate = 384000  # Make sure this matches the HC-05 module's baud rate

    try:
        # Open a serial connection to the Bluetooth module
        bluetooth_serial = serial.Serial(bluetooth_port, baud_rate, timeout=1)
        print(f"Connected to {bluetooth_port} at {baud_rate} baud.")

        # Convert values to bytes and send them
        data_to_send = f"{a},{b}\n"
        bluetooth_serial.write(data_to_send.encode())
        print(f"Sent data: {data_to_send.strip()}")

        # Close the serial connection
        bluetooth_serial.close()
        print("Connection closed.")

    except serial.SerialException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example values for a and b
    a_value = 10
    b_value = 20

    send_data_via_bluetooth(a_value, b_value)
