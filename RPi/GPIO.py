BCM = 'BCM'
OUT = 'OUT'

def setmode(mode):
  print 'GPIO-mock setmode ' + mode

def setup(pins, io):
  print 'GPIO-mock setup'

def output(pin, io):
  print 'GPIO-mock output'

def input(pin):
  print 'GPIO-mock input'
  return 17
