#! usr/bin/env python3

# Name: Dorian Mayorquin
# UCID: 31348606
# Section: CS356 003

import sys
import socket
import struct
import random

ip = sys.argv[1]
port = int(sys.argv[2])
hostname = sys.argv[3]

messageID = int(random.randrange(1,100))

message = struct.pack('!hhihh',1,0,messageID,3,0) + hostname.encode() #Message Type, Return Code, Message ID, QLength, ALength


clientsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientsocket.sendto(message, (ip,port))

print("Sending Request to " + ip + ", " + str(port))
print("Message ID: " + str(messageID))
print("Question Length: " + str(len(hostname)+5) + " bytes")
print("Answer Length: 0 bytes")
print("Question: " + str(hostname) + " A IN")

print(" ")

seqnumber = 1

while seqnumber < 4:
	try:
		clientsocket.settimeout(1)
		data, address = clientsocket.recvfrom(port)
		received = struct.unpack('!hhihh',data[:12])
		response = data[12:].decode()
		break
	except socket.timeout:
		if(seqnumber == 3):
			print("Request timed out ... Exiting Program.")
			sys.exit()
		print("Request timed out ...")
		print("Sending Request to " + ip + ", " + str(port))
		seqnumber+=1
		continue


print("Received Response from " + ip + ", " + str(port))
if(received[1] == 0):
	print("Return Code: " + str(received[1]) + " (No errors)")
else:
	print("Return Code: " + str(received[1]) + " (Name does not exist)")
print("Message ID: " + str(received[2]))
print("Question Length: " + str(len(hostname)+5) + " bytes")
print("Answer Length: " + str(received[4]) + " bytes")
print("Question: " + str(hostname) + " A IN")
if(received[1] != 1):
	print("Answer: " + response)