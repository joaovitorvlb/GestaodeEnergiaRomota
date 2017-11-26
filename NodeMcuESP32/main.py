import machine
import socket
import network
import time
import ustruct

from machine import SPI
from machine import Pin

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('IOT-2', 'mj110032')

i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))

led = machine.Pin(13, machine.Pin.OUT)

adc = machine.ADC(machine.Pin(36))

spi = SPI(baudrate=2000000, polarity=0, phase=0, firstbit=SPI.MSB,sck=Pin(18), mosi=Pin(23), miso=Pin(19)) #pinos SPI do esp32
cs = machine.Pin(5, machine.Pin.OUT)

def readI(addr,Rsh):                      #faz a leitura da corrente com base no shunt no ina219
	i2c.writeto(addr, '\1')
	data = i2c.readfrom(addr, 2)
	data = ustruct.unpack('!h', data)[0]
	return data*Rsh #100uV/0.1Ω=1mASS
    
def readV(addr):                         #Mede a tensão no barramento do ina219
	i2c.writeto(addr, '\2')
	data = i2c.readfrom(addr, 2)
	data = ustruct.unpack('!h', data)[0]
	return (((data>>3)*4.0) / 1000.0)

def temp_c():
	cs.value(1)
	cs.value(0)
	data = spi.read(4)
	cs.value(1)
	data = bytearray(4)
	cs.value(0)
	spi.readinto(data)
	cs.value(1)

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
	s.connect(("192.168.1.120", 5000))
	s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
	while True:
		data = s.recv(100)
		if data:
			print(str(data, 'utf8'), end='')
		else:
			break
	s.close()

while True:
	
	i = readI(64,0.1)
	v = readV(64)
	p = v * i                          #Faz o calculo da potencia
	t = adc.read()                     #Lê o ad e converte para temperatura
	rgtemp = temp_c()
	url = 'http://192.168.1.120:5000/sensores1/' + str(p) + '/' + str(rgtemp)     #Monta a string para enviar
	try:
		http_get(url)                   #Tenta disparar uma conexão
	except:                             #Se levantar exeção togla o led
		if led.value() == 1:
			led.value(0)
		else:
			led.value(1)
	time.sleep(5)



