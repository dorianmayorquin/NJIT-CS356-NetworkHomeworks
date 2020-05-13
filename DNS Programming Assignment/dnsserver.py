#! usr/bin/env python3

# Name: Dorian Mayorquin
# UCID: 31348606
# Section: CS356 003

import sys
import socket
import struct
import string

ip = sys.argv[1]
port = int(sys.argv[2])

serversocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serversocket.bind((ip,port))

infile = open("dns-master.txt", "r")
rr = []
lnum = 0
for line in infile:
	lnum+=1
	if(line[0] != '#' and not line[0].isspace()):
		rr.append(line) #Stored in array [Resource Record][Types]

infile.close()
		
print("DNS Server Ready to Receive: ")

while True:

		data,address = serversocket.recvfrom(port)
		message = struct.unpack('!hhihh',data[:12])
		host = data[12:].decode()
		response = 0

		for x in rr:
			if(x.find(host) != -1):
				response = x
				newmessage = struct.pack('!hhihh',2,0,message[2],message[3],(len(response)+5)) + response.encode()#Message Type, Return Code, Message ID, QLength, ALength
				serversocket.sendto(newmessage, address)
				break

		if(response == 0):
			newmessage = struct.pack('!hhihh',2,1,message[2],message[3],0)#Message Type, Return Code, Message ID, QLength, ALength
			serversocket.sendto(newmessage,address)


		








