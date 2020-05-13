#! /usr/bin/python3
#Name: Dorian Mayorquin
#UCID:	31348606
#Section: CS356 003

import sys
import socket
import struct
import time
import array

ip = sys.argv[1]
port = int(sys.argv[2])

seqnumber = 0
preceived = 0

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print("Pinging " + ip + ", " + str(port) + ":\n")

tiempo = []
while seqnumber < 10:

	prequest = struct.pack('ii',1,seqnumber) #First Number message, Second Number Sequence
	now = time.time()
	clientsocket.sendto(prequest,(ip,port))
	try:
			clientsocket.settimeout(1)
			prequestEcho, address = clientsocket.recvfrom(seqnumber)
	except socket.timeout:
			print("Ping message number " + str(seqnumber) + " timed out")
			seqnumber+=1
			continue
	later = time.time()
	rtt = later - now
	tiempo.append(rtt)
	print("Ping message number " + str(seqnumber) + " RTT: " + str(rtt))
	preceived+=1
	seqnumber+=1
plost = seqnumber - preceived
percentlost = plost/seqnumber*100
print("Packets sent: " + str(seqnumber)+" Packets Received: "+str(preceived)+" Packets Lost: "+str(plost))
print("Loss %: " + str(percentlost))
average = sum(tiempo)/len(tiempo)
print("Max RTT: "+str(max(tiempo))+" Min RTT: "+str(min(tiempo))+" Avg RTT: "+str(average))



