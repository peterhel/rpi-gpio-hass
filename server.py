#!/usr/bin/env python

"""
A simple echo server that handles exceptions
"""

import socket

def handleData(data):
   print data
   return data

host = ''
port = 50000
backlog = 5
size = 1024
s = None
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(backlog)
except socket.error, (value,message):
    if s:
        s.close()
    print "Could not open socket: " + message
    sys.exit(1)
while 1:
    client = None
    try:
      client, address = s.accept()
      data = client.recv(size)
      if data:
          client.send(handleData(data))
      client.close()
    finally:
      client.close()
