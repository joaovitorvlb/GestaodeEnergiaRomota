
from flask import Flask, render_template, jsonify
import __future__ 
import socket
import requests
import threading
import netifaces
import time
import sensores
import sqlite_
import sistema
import loop

pot = 0
bat = 0
cont = 0

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/graficos/<valor>')
def graficos(valor):
    valores = sqlite_.retorna_dados_coleta(valor)
    return jsonify(valores)

@app.route('/media/<valor>')
def media(valor):
    valores = sqlite_.retorna_dados_media(valor)
    return jsonify(valores)

@app.route('/rele/<valor>')
def rele(valor):
    if valor == '1':
        sensores.liga_rele()
    elif valor == '0':
        sensores.desliga_rele()
    else:
        return ('valor desconhecido', 200)
    return ('OK', 200)

@app.route('/led1/<valor>')
def led1(valor):
    if valor == '1':
        sensores.liga_led1()
    elif valor == '0':
        sensores.desliga_led1()
    else:
        return ('valor desconhecido', 200)
    return ('OK', 200)

@app.route('/led2/<valor>')
def led2(valor):
    if valor == '1':
        sensores.liga_led2()
    elif valor == '0':
        sensores.desliga_led2()
    else:
        return ('valor desconhecido', 200)
    return ('OK', 200)

@app.route('/lcd/<texto>')
def lcd(texto):
    texto_linha1, texto_linha2 = texto.split(',')
    sensores.escreve_lcd(texto_linha1, texto_linha2)
    return ('OK', 200)

@app.route('/servo1/<valor>')
def servo1(valor):
    valor = int(valor)
    sensores.move_servo1(valor)
    return ('OK', 200)

@app.route('/servo2/<valor>')
def servo2(valor):
    valor = int(valor)
    sensores.move_servo2(valor)
    return ('OK', 200)


@app.route('/update_temperatura')
def temperatura():
    t = sensores.leitura_temperatura()
    return jsonify(t)

@app.route('/update_potenciometro')
def potenciometro():
    p = sensores.leitura_pot()
    return jsonify(p)

@app.route('/sensores1/<vl1>/<vl2>')
def oi(vl1,vl2):
    sqlite_.cria_tabela_coleta()
    sqlite_.adiciona_dado_coleta(vl1,vl2)
    return ('OK', 200)

@app.route('/t_cpu')
def t_cpu():
    i = sistema.get_cpu_temp()
    return jsonify(i)

@app.route('/p_mem')
def p_mem():
    meminfo = sistema.meminfo()
    est1 = ('{}'.format(meminfo['MemTotal']))
    est1 = (est1.strip('kB'))
    est1 = long(est1)
    est2 = ('{}'.format(meminfo['MemFree']))
    est2 = (est2.strip('kB'))
    est2 = long(est2)
    uso = ((est2 *100) / est1)
    return jsonify(uso)


@app.route('/p_disc')
def partirion():
    disc = sistema.partition()
    part_t = long(disc[0][2])
    part_1 = long(disc[1][2])
    part_2 = long(disc[2][2])
    part = part_t / (part_1 + part_2)
    return jsonify(part)


if __name__ == "__main__":
    loop = loop.Loop()
    loop.start()
    local_ip = sistema.guet_ip()                #invoca funcao para retornar o IP local                             #inicia a thread
    app.run(host=local_ip)                     #loop dp flask
