#! /usr/bin/python
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()
time.sleep(5)
ser.write(b"6\n")
while True:
        unghi=input("Unghi rotatie: ")
        unghi=unghi+"\n"
        if unghi=="e\n":
                ser.write(b"exit\n")
                break
        ser.write(unghi.encode('utf-8'))
        line = ser.readline().decode('utf-8').rstrip()
        print("Distanta pana la senzor:" + line+"\n")
        time.sleep(1)