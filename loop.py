from threading import Thread
import sqlite_
import datetime
import time

class Loop(Thread):
	def __init__ (self):
		Thread.__init__(self)

	def run(self):
		while True:
			now = datetime.datetime.now()
			print now
			setp = now.replace(hour=8, minute=17, second=0, microsecond=0)
			print setp
			print " "
			if setp < now:
				sqlite_.cria_tabela_media()
				sqlite_.adiciona_dado_media(now.minute, now.second)
			time.sleep(1)
