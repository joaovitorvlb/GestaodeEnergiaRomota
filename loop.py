import datetime
import time
from threading import Thread

class Loop(Thread):
	def __init__ (self):
		Thread.__init__(self)

	def run(self):
		while True:
			now = datetime.datetime.now()
			print now
			setp = now.replace(hour=12, minute=3, second=0, microsecond=0)
			print setp
			print " "
			if setp < now:
				print "passou"
			time.sleep(1)
