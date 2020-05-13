#! /user/bin/env python3

# Name: Dorian Mayorquin
# UCID: 31348606

import sys
import socket

ipaddress = sys.argv[1]
port = int(sys.argv[2])
length = int(sys.argv[3])

string = 'X'*length

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print("Client Socket Ready...\n")

print("Data is being sent to IP: " + ipaddress + " Port: " + str(port) + " Length: " + str(length) + " Content: " + string)
clientsocket.sendto(string.encode(),(ipaddress,port))

counter = 0

while counter != 3:
		try:
			clientsocket.settimeout(1)
			dataEcho, address = clientsocket.recvfrom(length)
			print("Data Received From Server IP: "+ address[0] + " Port: " + str(address[1]) + " Content " + dataEcho.decode())
			clientsocket.close()
			sys.exit()
		except socket.timeout:
			print("Message timed out")
			print("Data is being sent to IP: " + ipaddress + " Port: " + str(port) + " Length: " + str(length) + " Content: " + string)
			counter+=1
		if counter == 3:
			print("Timeout Error")
			sys.exit()







