#!/usr/bin/env python

"""
A simple echo client that handles some exceptions
"""

import socket
import sys

host = 'localhost'
port = 50000
size = 1024
s = None

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
except socket.error, (value,message):
    if s:
        s.close()
    print "Could not open socket: " + message
    sys.exit(1)
s.send(' '.join([sys.argv[1], sys.argv[2]]))
data = s.recv(size)
s.close()
print 'Received:', data
