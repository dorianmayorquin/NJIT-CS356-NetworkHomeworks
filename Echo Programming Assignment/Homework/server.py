#! /usr/bin/env python3

# Name: Dorian Mayorquin
# UCID: 31348606

import sys
import socket

ipaddress = sys.argv[1]
port = int(sys.argv[2])

serversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind((ipaddress,port))

print ("Server is ready to receive on port: " + str(port) + "\n")

while True:
	data, address = serversocket.recvfrom(1024)
	print("Receive data from client " + address[0] + ", " + str(address[1]) + ": " + data.decode())

	serversocket.sendto(data,address)
	print("Sending data to client "+ address[0] + ", " + str(address[1]) + ": " + data.decode())