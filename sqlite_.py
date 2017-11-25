import sqlite3
import datetime

def cria_tabela_coleta():
    try:
        conect = sqlite3.connect('GestaoEnergia.db')
        cursor = conect.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS coleta
                         (id        INTEGER PRIMARY KEY,
                          potencia REAL, 
                          bateria   REAL,
                          tempo TIMESTAMP DEFAULT (DATETIME('now')) 
                          )''')
        conect.commit()
        conect.close()
    except Exception as e:
        print( 'except - cria_tabela_sensores', e)

def cria_tabela_media():
    try:
        conect = sqlite3.connect('GestaoEnergia.db')
        cursor = conect.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS media
                         (id        INTEGER PRIMARY KEY,
                          media REAL, 
                          bateria   REAL, 
                          tempo TIMESTAMP DEFAULT (DATETIME('now')) 
                          )''')
        conect.commit()
        conect.close()
    except Exception as e:
        print( 'except - cria_tabela_sensores', e)


def retorna_dados_coleta(quantidade=None):
    conect = sqlite3.connect('GestaoEnergia.db')
    cursor = conect.cursor()
    if not quantidade:
        cursor.execute('''SELECT * FROM coleta ORDER BY datetime(tempo) ASC''')
    else:
        cursor.execute('''SELECT * FROM coleta ORDER BY datetime(tempo) DESC LIMIT ?''', (quantidade,))
    return cursor.fetchall()

def adiciona_dado_coleta(potencia, bateria):
    try:
        conect = sqlite3.connect('GestaoEnergia.db')
        cursor = conect.cursor()
        tempo  = datetime.datetime.now()
        cursor.execute('''INSERT INTO coleta (potencia, bateria, tempo)
                          VALUES(?,?,?)''',(potencia, bateria, tempo))
        conect.commit()
        conect.close()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print( e)
        return False

def adiciona_dado_media(media, tempo):
    try:
        conect = sqlite3.connect('GestaoEnergia.db')
        cursor = conect.cursor()
        tempo  = datetime.datetime.now()
        cursor.execute('''INSERT INTO media (media, tempo)
                          VALUES(?,?)''',(media, tempo))
        conect.commit()
        conect.close()
        if cursor.rowcount > 0:
            return True
        else:
            return False
    except Exception as e:
        print( e)
        return False