import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

path = resource_path("logo.png")



import serial

ser = serial.Serial(
    port="COM9",
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )

command = "0x2E 0x09 \n"
ser.write(serial.to_bytes(command.encode()))
ser.close()