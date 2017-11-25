import sqlite3

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