
from flask import Flask, render_template
import socket
import requests
import sqlite3
import threading
import netifaces
import datetime
import time


app = Flask(__name__)

@app.route("/sensores")
def sensores():
    valores = retorna_dados_sensores()
    return render_template("sensores.html", valores=valores)

def cria_tabela_sensores():
    try:
        conect = sqlite3.connect('site.db')
        cursor = conect.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS sensores
                         (id INTEGER PRIMARY KEY,
                          corrente1 REAL, 
                          corrente2 REAL, 
                          corrente3 REAL,
                          corrente4 REAL,
                          tempo TIMESTAMP DEFAULT (DATETIME('now')))''')
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
        cursor.execute('''SELECT * FROM sensores ORDER BY datetime(tempo) DESC LIMIT ?''',
                       (quantidade,))
    return cursor.fetchall()

def adiciona_dado_sensores(corrente1, corrente2, corrente3, corrente4):
    try:
        conect     = sqlite3.connect('site.db')
        cursor = conect.cursor()
        tempo  = datetime.datetime.now()
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
            client, add = server.accept()
            data = client.recv(1024)  # Wait for some data and print
            if data:
                print 'Received from ', add[0], ' >> ', data
                data = data.strip()
                tag_pct, i_00, i_01, i_02, i_03 = data.split(':')

                if tag_pct == 'ESP01-IIII':
                    print 'Processing package'
                    print 'Package tag   ', tag_pct
                    print 'Load device 1 ', i_00, ' mA'
                    print 'Load device 2 ', i_01, ' mA'
                    print 'Load device 3 ', i_02, ' mA'
                    print 'Load device 4 ', i_03, ' mA'
                    cria_tabela_sensores()
                    adiciona_dado_sensores(i_00, i_01, i_02, i_03)
                if tag_pct == 'ESP02-VVVV':
                    print 'Processing package'
                    print 'Package tag       ', tag_pct
                    print 'Device 01 voltage ', i_00, ' V'
                    print 'Device 02 voltage ', i_01, ' V'
                    print 'Device 03 voltage ', i_02, ' V'
                    print 'Devide 04 voltage ', i_03, ' V' 


def guet_ip():
    gateways = netifaces.gateways()
    try:
        ifnet = gateways['default'][netifaces.AF_INET][1]
        return netifaces.ifaddresses(ifnet)[netifaces.AF_INET][0]['addr']
    except (KeyError, IndexError):
        return


if __name__ == "__main__":
    local_ip = guet_ip()
    sock_1 = ThreadSock(local_ip,500)
    sock_1.start()
    app.run(host=local_ip)
