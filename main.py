
from flask import Flask, render_template, jsonify
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
    return render_template('principal.html')

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
    #valor = int(valor)
    print valor
    if valor == '1':
        sensores.liga_rele()
    elif valor == '0':
        sensores.desliga_rele()
    else:
        return ('valor desconhecido', 200)
    return ('OK', 200)

@app.route('/led/<valor>')
def led(valor):
    #valor = int(valor)
    print valor
    if valor == '1':
        sensores.liga_led()
    elif valor == '0':
        sensores.desliga_led()
    else:
        return ('valor desconhecido', 200)
    return ('OK', 200)

@app.route('/lcd/<texto>')
def lcd(texto):
    texto_linha1, texto_linha2 = texto.split(',')
    sensores.escreve_lcd(texto_linha1, texto_linha2)
    return ('OK', 200)

@app.route('/servo/<valor>')
def servo(valor):
    valor = int(valor)
    sensores.move_servo(valor)
    return ('OK', 200)

@app.route('/update_temperatura')
def temperatura():
    t = sensores.leitura_temperatura()
    return jsonify(t)

@app.route('/update_potenciometro')
def potenciometro():
    p = sensores.leitura_pot()
    return jsonify(p)

def cria_tabela_sensores():
    try:
        conect = sqlite3.connect('site.db')
        cursor = conect.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS sensores
                         (id        INTEGER PRIMARY KEY,
                          corrente1 REAL, 
                          corrente2 REAL, 
                          corrente3 REAL,
                          corrente4 REAL,
                          tempo TIMESTAMP DEFAULT (DATETIME('now')) 
                          )''')
        conect.commit()
        conect.close()
    except Exception as e:
        print 'except - cria_tabela_sensores', e

def retorna_dados_sensores(quantidade=None):
    conect = sqlite3.connect('site.db')
    cursor = conect.cursor()
    if not quantidade:
        cursor.execute('''SELECT * FROM sensores ORDER BY datetime(tempo) ASC''')
    else:
        cursor.execute('''SELECT * FROM sensores ORDER BY datetime(tempo) DESC LIMIT ?''', (quantidade,))
    return cursor.fetchall()

def adiciona_dado_sensores(corrente1, corrente2, corrente3, corrente4):
    try:
        conect     = sqlite3.connect('site.db')
        cursor = conect.cursor()
        #dat  = time.strftime('%d/%m/%Y')
        #hora = time.strftime('%H:%M:%S')
        tempo = datetime.datetime.now()
        cursor.execute('''INSERT INTO sensores (tempo, corrente1, corrente2, corrente3, corrente4)
                          VALUES(?,?,?,?,?)''',(tempo, corrente1, corrente2, corrente3, corrente4))
        conect.commit()
        conect.close()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print e
        return False

class ThreadSock(threading.Thread):
    def __init__(self, ip_host, port_host):
        threading.Thread.__init__(self)
        self.ip_host = ip_host
        self.port_host = port_host

    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.ip_host, self.port_host))
        print 'ok'
        server.listen(5)
        while True:
            client, add = server.accept()                                #fica aguardando alguem conectar
            data = client.recv(1024)                                     #cloloca todo o buffer em data
            if data:
                print 'Received from ', add[0], ' >> ', data
                data = data.strip()                                      #retira as quebras de linha 
                tag_pct, i_00, i_01, i_02, i_03 = data.split(':')        #separa a string com lilmitador :

                if tag_pct == 'ESP01-IIII':
                    print 'Processing package'
                    print 'Package tag   ', tag_pct
                    print 'Load device 1 ', i_00, ' mA'
                    print 'Load device 2 ', i_01, ' mA'
                    print 'Load device 3 ', i_02, ' mA'
                    print 'Load device 4 ', i_03, ' mA'
                    cria_tabela_sensores()
                    adiciona_dado_sensores(i_00, i_01, i_02, i_03)

def guet_ip():
    gateways = netifaces.gateways()
    try:
        ifnet = gateways['default'][netifaces.AF_INET][1]
        return netifaces.ifaddresses(ifnet)[netifaces.AF_INET][0]['addr']
    except (KeyError, IndexError):
        return


if __name__ == "__main__":
    local_ip = guet_ip()                       #invoca funcao para retornar o IP local
    sock_1 = ThreadSock(local_ip,500)          #cria objeto de socket dentro de uma thread
    sock_1.start()                             #inicia a thread
    app.run(host=local_ip)                     #loop dp flask
