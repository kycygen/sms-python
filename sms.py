import serial
import os, time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
port = serial.Serial(“/dev/ttyS0”, baudrate=9600, timeout=1)

port.write(b’AT\r’)
rcv = port.read(10)
print(rcv)
time.sleep(1)

port.write(b”ATE0\r”)
rcv = port.read(10)
print(rcv)
time.sleep(1)

port.write(b’AT+CNMI=1,1,0,0,0\r’)
rcv = port.read(30)
print(rcv)
time.sleep(1)

port.write(b’AT+CPMS=”SM”,”SM”,”SM”\r’)
rcv = port.read(30)
print(rcv)
time.sleep(1)

port.write(b’AT+CSAS\r’)
rcv = port.read(30)
print(rcv)
time.sleep(10)

port.write(b’AT+CMGDA=”DEL ALL”\r’)
rcv = port.read(30)
print(rcv)
time.sleep(1)

port.write(b’AT+CPMS=”SM”,”SM”,”SM”\r’)
rcv = port.read(30)
print(rcv)
time.sleep(1)

port.write(b’AT\r’)
rcv = port.read(10)
print(rcv)
time.sleep(1)

port.write(b”AT+CMGF=1\r”)
print(“Text Mode Enabled…”)
time.sleep(3)
port.write(b’AT+CMGS=”9166873301″\r’)
msg = “test message from SIM900A…”
print(“sending message….”)
time.sleep(3)
port.reset_output_buffer()
time.sleep(1)
port.write(str.encode(msg+chr(26)))
time.sleep(3)
print(“message sent…”)
