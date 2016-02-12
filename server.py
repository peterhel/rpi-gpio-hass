#!/usr/bin/env python

"""
A simple echo server that handles exceptions
"""

import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup([2, 3], GPIO.OUT)

def handleData(data):
  print data
  dataString = data.split( )
  pin = int(dataString[1])
  acn = str(dataString[0])

  if acn == 'state':
    print GPIO.input(pin)
    return str(0 if GPIO.input(pin) == 1 else 1)
  elif acn == 'on':
    GPIO.output(pin, True)
    print 'Turned on'
    return str(0)
  elif acn == 'off':
    GPIO.output(pin, False)
    print 'Turned off'
    return str(1)

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
