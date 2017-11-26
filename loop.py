# -*- coding: utf-8 -*-

from threading import Thread
import sqlite_
import datetime
import time

class Loop(Thread):
	def __init__ (self):
		Thread.__init__(self)

	def run(self):
		flag = 1
		while True:
			now = datetime.datetime.now()
			print now
			setp = now.replace(second=50, microsecond=0)
			print " "
			print setp
			print " "
			print main.ist
			if setp > now:                           #Indica quando chega um novo dia
				flag = 1	                         #flag para selar atá a proxima condição

			if setp < now:                           #Checa se a data atual ja é a mesma doset point 
				if flag == 1:                        #flag indica se o dia atual na teve media apurada
					flag = 0                         #flag para selar atá a proxima condição
					print "Fim do minuto!"
					sqlite_.cria_tabela_media()
					sqlite_.adiciona_dado_media(now.minute, now.second)
			time.sleep(1)
