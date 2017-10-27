import time
from upm import pyupm_temperature as upm
from upm import pyupm_servo as servo
from wiringx86 import GPIOGalileo as GPIO
from upm import pyupm_jhd1313m1 as lcd

pino_sensor_temperatura = 0
pino_rele = 5
pino_pot = 15
pino_servo = 3

pinos = GPIO(debug=False)
pinos.pinMode(pino_rele, pinos.OUTPUT)
pinos.pinMode(pino_pot, pinos.ANALOG_INPUT)
pinos.pinMode(pino_servo, pinos.OUTPUT)
temp = upm.Temperature(pino_sensor_temperatura)
sg_servo = servo.ES08A(pino_servo)
tela = lcd.Jhd1313m1(0, 0x3E, 0x62)

def leitura_temperatura():
    return temp.value()

def leitura_pot():
    resulado = pinos.analogRead(pino_pot)
    voltagem = resulado #*5.0/1023.0
    return voltagem

def liga_rele():
    pinos.pinMode(pino_rele, pinos.OUTPUT)
    pinos.digitalWrite(pino_rele, pinos.HIGH)

def desliga_rele():
    pinos.digitalWrite(pino_rele, pinos.LOW)

def move_servo(posicao):
    sg_servo.setAngle(posicao)

def escreve_lcd(texto_linha1, texto_linha2):
    tela.clear()
    tela.setColor(255, 0, 0)
    tela.setCursor(0, 0)
    isto = str(texto_linha1)
    tela.write(isto)
    tela.setCursor(1, 0)
    isto = str(texto_linha2)
    tela.write(isto)