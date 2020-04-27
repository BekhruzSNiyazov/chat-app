import socket
import sys
import time

x = socket.socket()
h_name = input("Enter the hostname of the server: ")
port = 8080

x.connect((h_name, port))
print("Connected")

while True:
	incoming_message = x.recv(1024)
	incoming_message = incoming_message.decode()
	print(incoming_message, "<<<")
	message = input(">>>")
	message = message.encode()
	x.send(message)
	print("Sent")