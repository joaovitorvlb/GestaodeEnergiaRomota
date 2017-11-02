import time
from upm import pyupm_temperature as upm
from upm import pyupm_servo as servo
from wiringx86 import GPIOGalileoGen2 as GPIO
from upm import pyupm_jhd1313m1 as lcd

import __future__ 
from collections import OrderedDict


pino_sensor_temperatura = 0
pino_rele    = 8
pino_led1    = 3
pino_led2    = 4
pino_pot     = 15
pino_servo1  = 5
pino_servo2  = 6

pinos = GPIO(debug=False)


pinos.pinMode(pino_rele, pinos.OUTPUT)
pinos.pinMode(pino_led1, pinos.OUTPUT)
pinos.pinMode(pino_led2, pinos.OUTPUT)
pinos.pinMode(pino_pot, pinos.ANALOG_INPUT)
pinos.pinMode(pino_servo1, pinos.OUTPUT)
pinos.pinMode(pino_servo2, pinos.OUTPUT)
temp = upm.Temperature(pino_sensor_temperatura)
sg_servo1 = servo.ES08A(pino_servo1)
sg_servo2 = servo.ES08A(pino_servo2)
tela = lcd.Jhd1313m1(0, 0x3E, 0x62)

tela.setColor(0, 100, 50)

def leitura_temperatura():
    return temp.value()

def leitura_pot():
    resulado = pinos.analogRead(pino_pot)
    voltagem = resulado #*5.0/1023.0
    return voltagem

def liga_rele():
    pinos.digitalWrite(pino_rele,pinos.HIGH)

def desliga_rele():
    pinos.digitalWrite(pino_rele,pinos.LOW)

def liga_led1():
    pinos.digitalWrite(pino_led1,pinos.HIGH)

def desliga_led1():
    pinos.digitalWrite(pino_led1,pinos.LOW)

def liga_led2():
    pinos.digitalWrite(pino_led2,pinos.HIGH)

def desliga_led2():
    pinos.digitalWrite(pino_led2,pinos.LOW)

def move_servo1(posicao):
    sg_servo1.setAngle(posicao)

def move_servo2(posicao):
    sg_servo2.setAngle(posicao)

def escreve_lcd(texto_linha1, texto_linha2):
    tela.clear()
    tela.setColor(0, 50, 100)
    tela.setCursor(0, 0)
    isto = str(texto_linha1)
    tela.write(isto)
    tela.setCursor(1, 0)
    isto = str(texto_linha2)
    tela.write(isto)

def get_cpu_temp():
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as f:
        temp = float(f.read()) / 1000.0
    return temp

def meminfo():
    meminfo=OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

def partition():
    procfile = open("/proc/partitions")
    parts = [p.split() for p in procfile.readlines()[2:]]
    procfile.close()
    return parts



