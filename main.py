# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, flash, redirect, request, session, abort
from flask_sqlalchemy import SQLAlchemy
import os
import __future__ 
import socket
import requests
import threading
import netifaces
import time
import sqlite_
import sistema
import loop
import signal
import sys
import psutil

pot = 0
bat = 0
cont = 0

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)


class User(db.Model):
    """ Create user table"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(80))

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


@app.route('/', methods=['GET', 'POST'])
def home():
    """ Session control"""
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == 'POST':
            username = getname(request.form['username'])
            return render_template('index.html', data=getfollowedby(username))
        return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        passw = request.form['password']
        try:
            data = User.query.filter_by(username=name, password=passw).first()
            if data is not None:
                session['logged_in'] = True
                return redirect(url_for('home'))
            else:
                return 'Dont Login'
        except:
            return "Dont Login"

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register Form"""
    if request.method == 'POST':
        new_user = User(username=request.form['username'], password=request.form['password'], email=request.form['email'])
        db.session.add(new_user)
        db.session.commit()
        return render_template('login.html')
    return render_template('register.html')

@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))


@app.route('/graficos/<valor>')
def graficos(valor):
    valores = sqlite_.retorna_dados_coleta(valor)
    return jsonify(valores)

@app.route('/media/<valor>')
def media(valor):
    valores = sqlite_.retorna_dados_media(valor)
    return jsonify(valores)

@app.route('/update_temperatura')
def temperatura():
    return ('OK', 200)

@app.route('/update_potenciometro')
def potenciometro():
    return ('OK', 200)

@app.route('/sensores1/<vl1>/<vl2>/<vl3>/<vl4>/<vl5>/<vl6>')
def oi(vl1,vl2,vl3,vl4,vl5,vl6):
    sqlite_.cria_tabela_coleta()
    sqlite_.adiciona_dado_coleta(vl3,vl4,vl5,vl6)
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

def signal_handler(signal, frame):
    for process in psutil.process_iter():                #varre lista de processo da maquina
        if process.cmdline() == ['python', 'main.py']:   #se encontrar o processo
            print ' '
            print 'Processo: ' + str(process.pid)
            print 'Processo encerrado!'
            process.terminate()                          #pega o processo e termina

signal.signal(signal.SIGINT, signal_handler)             #gera calback por KI caso Ctrl+C

if __name__ == "__main__":
    loop = loop.Loop()
    loop.start()
    local_ip = sistema.guet_ip()                #invoca funcao para retornar o IP local 
    db.create_all()
    app.secret_key = "123"                           #inicia a thread
    app.run(host=local_ip)                      #loop dp flask


