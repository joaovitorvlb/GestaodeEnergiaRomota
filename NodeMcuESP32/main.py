import machine
import socket
import network
import time
import ustruct

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('IOT-2', 'mj110032')

i2c = machine.I2C(scl=machine.Pin(18), sda=machine.Pin(19))

def readI(addr,Rsh):
        i2c.writeto(addr, '\1') #select Reg1 Shunt Voltage
        data = i2c.readfrom(addr, 2)
        data = ustruct.unpack('!h', data)[0]
        return data*Rsh #100uV/0.1Ω=1mA
    
def readV(addr):
	i2c.writeto(addr, '\2') #select Reg2 Bus Voltage
	data = i2c.readfrom(addr, 2)
	data = ustruct.unpack('!h', data)[0]
	return (data>>3)*4.0 #mV


def http_get(url1):
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
	v = readV(68)
	i = readI(68,0.1)
	url = 'http://192.168.1.120:5000/oi/' + str(v) +'/' + str(i) +'/56'
	http_get(url)
	time.sleep(5)



