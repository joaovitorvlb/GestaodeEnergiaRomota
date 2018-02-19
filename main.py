# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, flash, redirect, request, session, abort, url_for
from flask_sqlalchemy import SQLAlchemy
from array import array
from threading import Thread
import datetime
import os
import __future__ 
import socket
import requests
import threading
import netifaces
import time
import sqlite_
import sistema
import signal
import sys
import psutil
import mpu6050
import smbus
import pca9685
import pcduino

ad = pcduino.Adc(3)

name = ""

api = "B245K8ZFSW1YI54O"

i2c = smbus.SMBus(2)

pwm = pca9685.Pca9685(i2c=i2c, freq=50)

pwm0 = 75
pwm1 = 90

pwm.write_servo(0,pwm0)
pwm.write_servo(1,pwm1)

mpu = mpu6050.Mpu6050(i2c=i2c,adr=0x68)

pot = []
bat = []
il = []
tmp = []
flag = 1

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)

class User(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password



@app.route('/', methods=['GET', 'POST'])
def home():                                      #Função que é chamada para fazer o conrole de seção com 1 id para cada seção
    if not session.get('logged_in'):             #verifica se for true inicia seção senao finaliza
        return render_template('login.html')
    else:
        return render_template('inicio.html', usuario=session['username'])
        print get_online_users()


@app.route('/login', methods=['GET', 'POST'])
def login():
    global name
    if request.method == 'GET':                  #Verifica se é requisição GET
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        try:
            data = User.query.filter_by(username=name, password=passw).first()  #verifica n banco de dados se existe usuário
            if data is not None:
                session['username'] = name
                session['logged_in'] = True            #Flag da seção se torna true para autenticado geralmente inicia none
                return redirect(url_for('home'))       #se tiver usuario cadastrado chama home e verifica flag de login
            else:
                return render_template('login.html')   # se o usuaruio não exixtir retorna pagina login

        except:        
            return render_template('login.html')        # Se alguma exceção for levantada nao finaliza e retorna para login

@app.route('/registro', methods=['GET', 'POST'])
def register():
    """Register Form"""
    if request.method == 'POST':        #verifica se o formulario fez ação POST
        new_user = User(username=request.form['username'], password=request.form['password'])  #pega valores e prepara para injetar no bd
        db.session.add(new_user)               #Adiciona na fina de inserção
        db.session.commit()                    #Dispara a inserção de dados no bd
        return render_template('login.html')   #E retorna login para lgar no usuário cadastrado
    return render_template('register.html')    # se o if não encontrar POST retorna pagina de registro

@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False      #se logout for chamado pega a flag e atribui false
    return redirect(url_for('home'))  #Chama nome que vai verificar que a seção foi encerrada

@app.route("/controle")
def controle():
    return render_template('controle.html', usuario=session['username'])

@app.route("/energia")
def energia():
    return render_template('energia.html', usuario=session['username'])

@app.route("/orientacao")
def orientacao():
    return render_template('orientacao.html', usuario=session['username'])

@app.route("/index")
def index():
    return redirect(url_for('home'))



@app.route('/update')
def update():
    buf = array('f')
    buf.append(mpu.read_gyro_x())
    buf.append(mpu.read_gyro_y())
    buf.append(mpu.read_gyro_z())
    buf.append(round(psutil.cpu_percent(), 2))
    buf.append(round(psutil.virtual_memory()[2], 2))
    buf.append(round(psutil.disk_usage('/')[3], 2))
    buf.append(round(mpu.read_accel_x(), 2))
    buf.append(round(mpu.read_accel_y(), 2))
    buf.append(round(mpu.read_accel_z(), 2))
    buf.append(mpu.get_x_rotation(buf[6], buf[7], buf[8]))
    buf.append(mpu.get_y_rotation(buf[6], buf[7], buf[8]))
    buf.append(ad.read() / 329.3)
    buff = buf.tolist()
    return jsonify(buff)

@app.route('/graficos/<valor>')
def graficos(valor):
    valores = sqlite_.retorna_dados_coleta(valor)
    return jsonify(valores)

@app.route('/media/<valor>')
def media(valor):
    valores = sqlite_.retorna_dados_media(valor)
    return jsonify(valores)

@app.route('/servo/<valor>')
def servo(valor):
    global pwm0
    global pwm1

    if valor == 'a1':
        pwm0 = pwm0 + 2
        pwm.write_servo(0, pwm0)

    if valor == 'a2':
        pwm0 = pwm0 - 2
        pwm.write_servo(0, pwm0)

    if valor == 'a3':
        pwm1 = pwm1 + 2
        pwm.write_servo(1, pwm1)

    if valor == 'a4':
        pwm1 = pwm1 - 2
        pwm.write_servo(1, pwm1)

    return "OK"


@app.route('/sensores1/<vl1>/<vl2>/<vl3>/<vl4>/<vl5>/<vl6>')
def oi(vl1,vl2,vl3,vl4,vl5,vl6):
    pot.append(float(vl3))
    tmp.append(float(vl4))
    il.append(float(vl6))
    bat.append(float(vl1))

    sqlite_.cria_tabela_coleta()
    sqlite_.adiciona_dado_coleta(vl3,vl1,vl4,vl6)

    return ('OK', 200)

class Loop(Thread):
    def __init__ (self):
        Thread.__init__(self)

    def run(self):

        flag = 1
        global api
        global bat
        global pot

        while True:
            now = datetime.datetime.now()
            setp = now.replace(minute=59,second=0, microsecond=0) 
            
            if now < setp:                           #Indica quando chega um novo dia
                flag = 1                             #flag para selar atá a proxima condição

            if now > setp:                           #Checa se a data atual ja é a mesma doset point 
                if flag == 1:                        #flag indica se o dia atual na ja teve media apurada
                    flag = 0  
                    print "oi"                       #flag para selar atá a proxima condição
                    if bat and pot:

                        mbat = sum(bat) / len(bat)
                        mpot = sum(pot) / len(pot)
                        mtmp = sum(tmp) / len(tmp)
                        mil = sum(il) / len(il)

                        payload = {'api_key': api, 'field1' : str(mpot), 'field2' : str(mtmp), 'field3' : str(mil), 'field4' : str(mbat)}
                        requests.post("https://api.thingspeak.com/update",params=payload)

                
                        sqlite_.cria_tabela_media()
                        sqlite_.adiciona_dado_media(mbat, mpot)
                        while len(bat) > 0 : bat.pop()  #limpa a lista para novo ciclo
                        while len(pot) > 0 : pot.pop()  #limpa a lista para novo ciclo
                        while len(tmp) > 0 : tmp.pop()  #limpa a lista para novo ciclo
                        while len(il) > 0 : il.pop()  #limpa a lista para novo ciclo
            time.sleep(1)
        

def signal_handler(signal, frame):
    for process in psutil.process_iter():                #varre lista de processo da maquina
        if process.cmdline() == ['python', 'main.py']:   #se encontrar o processo
            print ' '
            print 'Processo: ' + str(process.pid)
            print 'Processo encerrado!'
            process.terminate()                          #pega o processo e termina

signal.signal(signal.SIGINT, signal_handler)             #gera calback por KI caso Ctrl+C

if __name__ == "__main__":
    loop = Loop()
    loop.start()
    local_ip = sistema.guet_ip()                #invoca funcao para retornar o IP local 
    db.create_all()                             #verifica o modelo de tabela e cria o bd
    app.secret_key = "123"                      
    app.run(host=local_ip)                      #loop dp flask


