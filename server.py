import socket
import sys
import time

x = socket.socket()

h_name = socket.gethostname()
print("Server will start on host", h_name)

port = 8080

x.bind((h_name, port))
x.listen(1)
connection, address = x.accept()
print("Connected")

while True:
	display_mess = input(">>> ")
	display_mess = display_mess.encode()
	connection.send(display_mess)
	print("Sent")
	in_message = connection.recv(1024)
	in_message = in_message.decode()
	print(in_message, "<<<")