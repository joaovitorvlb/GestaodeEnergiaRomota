from machine import TouchPad
from machine import Timer
from machine import Pin
from machine import SPI
from machine import I2C
from machine import ADC
from machine import DAC 
import socket
import network
import time
import ustruct

touch0 = TouchPad(Pin(4))
touch2 = TouchPad(Pin(2))

dac0 = DAC(Pin(25))       
dac1 = DAC(Pin(26))
 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('IOT-2', 'mj110032')

i2c = I2C(scl=Pin(22), sda=Pin(21))                 #pinos I2C do esp32

spi = SPI(sck=Pin(18), mosi=Pin(23), miso=Pin(19))  #pinos SPI do esp32

cs1 = Pin(5, Pin.OUT)
cs2 = Pin(17, Pin.OUT)

led1 = Pin(13, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(14, Pin.OUT)

adc1 = ADC(Pin(36))
adc2 = ADC(Pin(39))


cs1.value(1)
cs2.value(1)

cont = 0

timer = Timer(1) 

def readl(addr):
	time = 0
	data = i2c.readfrom(addr, 2)
	value = (((data[0] << 8) + data[1]) * 1200) // 1000
	return value 


def tick1(timer):
	global cont
	if led2.value() == 1:
		led2.value(0)
	else:
		led2.value(1)
	cont = 1
		
timer.init(period=1000, mode=Timer.PERIODIC, callback=tick1)

i2c.writeto(35, bytes([0x10])) # start continuos 1 Lux readings every 120ms



def temp_th(p_cs):
	p_cs.value(1)
	p_cs.value(0)
	data = spi.read(4)
	p_cs.value(1)
	data = bytearray(4)
	p_cs.value(0)
	spi.readinto(data)
	p_cs.value(1)

	temp = data[0] << 8 | data[1]
	if temp & 0x0001:
		return float('NaN')  # Fault reading data.
	temp >>= 2
	if temp & 0x2000:
		temp -= 16384  # Sign bit set, take 2's compliment.
	return temp * 0.25



def http_get(url1):                     #Faz requisição http
	_, _, host, path = url1.split('/', 3)
	s = socket.socket()
	s.connect(("192.168.1.115", 5000))
	s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
	while True:
		data = s.recv(100)
		if data:
			print(str(data, 'utf8'), end='')
		else:
			break
	s.close()

dac0.write(128) #output 1.75V voltage
dac1.write(64)  #output 0.9V voltage

v1 = 0 
i1 = 0
p1 = 0
temp1 = 0
temp2 = 0
il = 0
setcont = 60
flag =1

while True:
	
	if cont == 1:
		led3.value(1)
		cont = 0
		va = adc1.read() / 161.0                     #Lê o ad e converte para temperatura
		ia = adc2.read() / 3.77

		v1 += va
		i1 += ia

		p1 += (va * ia) / 1000.0
		
		temp1 += temp_th(cs1) - 35
		temp2 += temp_th(cs2) - 35
		
		il += readl(35)
		flag = flag + 1
		led3.value(0)

	if flag == setcont:
		flag = 0

		bf1 = str(round((v1 / setcont),2))
		bf2 = str(round((i1 / setcont),2))
		bf3 = str(round((p1 / setcont),2))
		bf4 = str(round((temp1 / setcont),2))
		bf5 = str(round((temp2 / setcont),2))
		bf6 = str(round((il / setcont),2))
	
		url = 'http://192.168.1.115:5000/sensores1/' + bf1 + '/' + bf2 + '/' + bf3 + '/' + bf4 + '/' + bf5 + '/' + bf6     #Monta a string para enviar
		
		try:
			http_get(url)                   #Tenta disparar uma conexão
		except:                             #Se levantar exeção togla o led
			if led1.value() == 1:
				led1.value(0)
			else:
				led1.value(1)
		v1 = 0
		i1 = 0
		va = 0
		i = 0
		p1 = 0
		temp1 = 0
		temp2 = 0
		il = 0




