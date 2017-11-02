
from flask import Flask, render_template, jsonify
import __future__ 
import socket
import requests
import sqlite3
import threading
import netifaces
import datetime
import time
import sensores


app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/sensores')
def sensores_rota():
    return render_template('sensores.html')

@app.route('/atuadores')
def atuadores():
    return render_template('atuadores.html')

@app.route('/graficos/<valor>')
def graficos(valor):
    valores = retorna_dados_sensores(valor)
    return render_template('graficos.html', valores=valores)

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

@app.route('/oi/<vl1>/<vl2>/<vl3>')
def oi(vl1,vl2,vl3):
    cria_tabela_sensores()
    adiciona_dado_sensores(vl1,vl2,vl3)
    return ('OK', 200)

@app.route('/t_cpu')
def t_cpu():
    i = sensores.get_cpu_temp()
    return jsonify(i)

@app.route('/p_mem')
def p_mem():
    meminfo = sensores.meminfo()
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
    disc = sensores.partition()
    part_t = long(disc[0][2])
    part_1 = long(disc[1][2])
    part_2 = long(disc[2][2])
    part = part_t / (part_1 + part_2)
    return jsonify(part)


def cria_tabela_sensores():
    try:
        conect = sqlite3.connect('site.db')
        cursor = conect.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS sensores
                         (id        INTEGER PRIMARY KEY,
                          corrente REAL, 
                          tensao   REAL, 
                          potencia REAL,
                          tempo TIMESTAMP DEFAULT (DATETIME('now')) 
                          )''')
        conect.commit()
        conect.close()
    except Exception as e:
        print( 'except - cria_tabela_sensores', e)

def retorna_dados_sensores(quantidade=None):
    conect = sqlite3.connect('site.db')
    cursor = conect.cursor()
    if not quantidade:
        cursor.execute('''SELECT * FROM sensores ORDER BY datetime(tempo) ASC''')
    else:
        cursor.execute('''SELECT * FROM sensores ORDER BY datetime(tempo) DESC LIMIT ?''', (quantidade,))
    return cursor.fetchall()

def adiciona_dado_sensores(corrente, tensao, potencia):
    try:
        conect = sqlite3.connect('site.db')
        cursor = conect.cursor()
        tempo  = datetime.datetime.now()
        cursor.execute('''INSERT INTO sensores (tempo, corrente, tensao, potencia)
                          VALUES(?,?,?,?)''',(tempo, corrente, tensao, potencia))
        conect.commit()
        conect.close()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print( e)
        return False

def guet_ip():
    gateways = netifaces.gateways()
    try:
        ifnet = gateways['default'][netifaces.AF_INET][1]
        return netifaces.ifaddresses(ifnet)[netifaces.AF_INET][0]['addr']
    except (KeyError, IndexError):
        return


if __name__ == "__main__":
    local_ip = guet_ip()                       #invoca funcao para retornar o IP local                             #inicia a thread
    app.run(host=local_ip)                     #loop dp flask
