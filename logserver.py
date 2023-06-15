#!/bin/env python3
import socket
import sys
from datetime import datetime
import slacknotif

if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
    ip = sys.argv[1]
    port = int(sys.argv[2])
    server_address = (ip, port)
else:
    server_address = ('10.67.28.165', 31371)

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the port
s.bind(server_address)
print("Do Ctrl+c to exit the program !!")

while True:
    data, address = s.recvfrom(4096)
    curtm = datetime.now()
    print(curtm.strftime("%H:%M:%S"), " received from \'", address[0], "\': ", data.decode('utf-8'), "\n")
    slacknotif.slacknotif(curtm.strftime("%H:%M:%S"), " received from \'", address[0], "\': ", data.decode('utf-8'), "\n")


