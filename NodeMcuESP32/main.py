import network
import usocket as socket


nic = network.WLAN(network.STA_IF)
nic.active(True)

nic.connect('IOT-2', 'mj110032')

s = socket.socket()
addr = socket.getaddrinfo('192.168.1.120', 5000)[0][-1]
s.connect(addr)
s.send(b'GET /graficos/1 \r\n HTTP/1.1\r\n')
data = s.recv(1000)
print(data)
