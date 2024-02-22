import serial
import json
from datetime import datetime

# Establish serial connection (change port and baudrate accordingly)
# knee angle, thigh girth, knee girth
ser = serial.Serial('/dev/cu.usbmodem1101', 9600)  # Replace 'COM3' with your XIAO's port

file_name = "received_data_meichen_squat" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".json"
data_list = []

try:
    while True:
        line = ser.readline().decode('utf-8').rstrip()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{current_time}: {line}")
        data_list.append({
            "timestamp": current_time,
            "data": line
        })

except KeyboardInterrupt:
    with open(file_name, 'w') as outfile:
        json.dump(data_list, outfile)

    ser.close()
