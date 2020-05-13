#! /usr/bin/python3
#Name: Dorian Mayorquin
#UCID:	31348606
#Section: CS356 003

import sys
import socket
import struct
import random

ip = sys.argv[1]
port = int(sys.argv[2])

serversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind((ip,port))

print("The server is ready to receive on port: " + str(port))

while True:

	num = int(random.random()*10)
	received, address = serversocket.recvfrom(port)
	data = struct.unpack('ii', received)
	print("Responding to ping request with sequence number " + str(data[1]))

	if num > 4:
		presponse = struct.pack('ii',2,data[1])
		serversocket.sendto(presponse,address)


