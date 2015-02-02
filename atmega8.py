import time
import signal
import sys
from collections import deque
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)

bits = []

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
	GPIO.remove_event_detect(8)
        print('stopped listening.')
	
	d = deque(bits)
	for shift in range(0,8):
		d.rotate(1)
		chars = []
		for pos in range(0, len(bits) / 8):
			liste = list(d)
			b = liste[pos*8:pos*8+8]
			binarybyte = "".join(str(i) for i in b)
			chars.append(chr(int(binarybyte, 2)))
		
		print(''.join(chars))
	
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def clock_callback(channel):
	bit = GPIO.input(7)
	sys.stdout.write('1' if bit else '0')
	sys.stdout.flush()
	bits.append(bit)

GPIO.add_event_detect(8, GPIO.RISING, callback=clock_callback) 

while (True):
	time.sleep(5)

