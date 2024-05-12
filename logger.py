import os
import serial
import time

# see README.md for UART_PORT selection
UART_PORT = 'COM3'
BAUD_RATE = 460800
LOOP_TIME = 1

uart = serial.Serial(UART_PORT, BAUD_RATE)

log_timestamp = time.strftime('%Y%m%d-%H%M%S')
log_name = f'logs/{log_timestamp}-linkstats.log'
os.makedirs(os.path.dirname(log_name), exist_ok=True)
file = open(log_name, 'w')

try:
    while True:
        data = uart.readline().decode('utf-8').strip()
        now = time.strftime('%H:%M:%S')
        
        split_data = data.split(',')
        if len(split_data) == 10:
            c_line = f'RSSI1: {split_data[0]}    RSSI2: {split_data[1]}    LQ: {split_data[2]}'
            l_line = f'{now} {data}'
        else:
            c_line = f'Malformed data: {data}'
            l_line = f'{now} Malformed data: {data}'
        
        print(c_line)
        file.write(l_line + '\n')
        file.flush()

        time.sleep(LOOP_TIME)
        
except KeyboardInterrupt:
    print(f"\nUART stream stopped. Data saved to {log_name}")

finally:
    uart.close()
    file.close()
