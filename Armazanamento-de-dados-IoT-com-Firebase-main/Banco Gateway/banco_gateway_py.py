# -*- coding: utf-8 -*-
"""Banco_Gateway.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16u_8qLxiFoQcxrHlTukYnGPZqMzKm09v
"""

# -*- coding: utf-8 -*-
"""TestesProRasp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Ler3oLvMvdm0P6EBDFUyTQaDPRR8LB9
"""

import sqlite3
import time

'''
  @TODO 
    - verificar se dtype é válido
'''

def create_table():
  conn = sqlite3.connect('data.db')
  curs = conn.cursor()
  
  try:
    curs.execute("BEGIN") #COMEÇO DO TRANSACIONAL 
    curs.execute("""
      CREATE TABLE IF NOT EXISTS data (
      ID_DATA INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      END_DEVICE_NAME TEXT NOT NULL,
      DTYPE TEXT NOT NULL,
      VALUE REAL,
      DATE_CREATED DATE NOT NULL,
      FIREBASE_SYNC BOOLEAN NOT NULL
      );
    """)
    curs.execute("""
      CREATE INDEX IF NOT EXISTS idx_busca_sync on data (END_DEVICE_NAME, FIREBASE_SYNC);
    """)
    conn.commit()
  except Exception as e:
    curs.rollback()
  finally:
    conn.close()
  

def dropa_table():
  conn = sqlite3.connect('data.db')
  curs = conn.cursor()
  try:
    curs.execute("BEGIN") #COMEÇO DO TRANSACIONAL 
    curs.execute("""
      DROP TABLE if not exists data;
    """)
    conn.commit()
  except Exception as e:
    curs.rollback()
  finally:
    conn.close()  


def insert(device_name, dtype, valor):
  conn = sqlite3.connect('data.db')
  curs = conn.cursor()

  try: 
   curs.execute(f"INSERT INTO data (END_DEVICE_NAME, DTYPE, VALUE, DATE_CREATED,FIREBASE_SYNC) VALUES ('{device_name}', '{dtype}', {valor}, datetime('now'), FALSE)" )  
  except Exception as e:
    conn.rollback()
  finally:
    conn.commit()
    conn.close()
  ## @TODO return true ou false
  return curs.lastrowid


def consultaLastRecord(device_name):
  conn = sqlite3.connect('data.db')
  curs = conn.cursor()
  result_dict = []

  try:
    query = f"SELECT END_DEVICE_NAME, DTYPE, VALUE, max(DATE_CREATED) from data WHERE END_DEVICE_NAME = '{device_name}' group by DTYPE"
    curs.execute(query)
    results = curs.fetchall()
    for row in results:
      row_dict = {}
      for i, col in enumerate(curs.description):
        row_dict[col[0]] = row[i]
      result_dict.append(row_dict)
  except Exception as e:
    conn.commit()
    return []
  finally:
    conn.close()
 
  return result_dict

def returnDadosNotSYNC():
  conn = sqlite3.connect('data.db')
  curs = conn.cursor()
  result_dict = []

  try:
    query = f"SELECT * FROM data WHERE FIREBASE_SYNC = FALSE"
    curs.execute(query)

    results = curs.fetchall()

    for row in results:
      row_dict = {}
      for i, col in enumerate(curs.description):
        row_dict[col[0]] = row[i]
      result_dict.append(row_dict)
  except Exception as e:
    conn.commit()
    return []
  finally:
    conn.close()
 
  return result_dict

'''
  Função para atualizar dado sincronizado com o Firebase.
  Para isso, atualizamos o campo FIREBASE_SYNC para true no banco
  @params:
   - ID_DATA
'''
def atualizaTrue(id_data): 

  conn = sqlite3.connect('data.db')
  curs = conn.cursor()

  try:
    query = f"UPDATE DATA SET FIREBASE_SYNC = TRUE WHERE id_data = {id_data}"
    curs.execute(query)
  except Exception as e:
    conn.rollback()
    return -1 ## erro de excecao
  finally:
    conn.commit()
    conn.close()
  return curs.rowcount

'''
  Pega tudo do banco
'''
def selectAll():
  conn = sqlite3.connect('data.db')
  curs = conn.cursor()
  result_dict = []

  try:
    query = f"SELECT ID_DATA, END_DEVICE_NAME, FIREBASE_SYNC FROM data"
    curs.execute(query)

    results = curs.fetchall()

    for row in results:
      row_dict = {}
      for i, col in enumerate(curs.description):
        row_dict[col[0]] = row[i]
      result_dict.append(row_dict)
  except Exception as e:
    conn.commit()
    return []
  finally:
    conn.close()
 
  return result_dict


'''
  ## FUNCOES USADAS PRA TESTE
from threading import Thread
def insere_algo():
  conn = sqlite3.connect('data.db')
  curs = conn.cursor()
  device_name = 'LALA'
  dtype = 'pH'
  valor = 1

  try: 
   curs.execute(f"INSERT INTO data (END_DEVICE_NAME, DTYPE, VALUE, DATE_CREATED,FIREBASE_SYNC) VALUES ('{device_name}', '{dtype}', {valor}, datetime('now'), FALSE)" )  
  except Exception as e:
    conn.rollback()
  finally:
    conn.commit()
    conn.close()
  ## @TODO return true ou false
  return curs.lastrowid

def update_algo():
  conn = sqlite3.connect('data.db')
  curs = conn.cursor()

  try: 
   curs.execute(f"UPDATE data set FIREBASE_SYNC = true where ID_DATA = 19" )  
  except Exception as e:
    conn.rollback()
  finally:
    conn.commit()
    conn.close()
  ## @TODO return true ou false
  return True

def teste():
  insert_t = Thread(target=insere_algo)
  update_t = Thread(target=update_algo)
  insert_t.start()
  update_t.start()
'''

#dropa_table()
create_table()
insert('PAI', 'pH', 10.0)
time.sleep(1)
insert('PAI', 'Conduct', 5.0)
time.sleep(1)
insert('PAI', 'pH', 11.0)
time.sleep(1)
insert('PAI', 'pH', 25.0)
insert('PAI', 'Conduct', 42.0)
insert('PAI', 'Temperature', 12.0)

naoSincronizados = returnDadosNotSYNC()
print(naoSincronizados)
print(len(naoSincronizados)) ## vai retornar 22

ans = atualizaTrue(1)
print('primeira atualizacao linhas: ', ans)
ans = atualizaTrue(2)
print('segunda atualizacao linhas: ',ans)
ans = atualizaTrue(10000)
print('terceira atualizacao linhas: ',ans)

### 1
### 1
### 0

## Vejo tudo
ans = selectAll()
for row in ans:
  print('Linha: ', row)

print('-----------------------------------')

#teste()
## Vejo tudo de novo
ans = selectAll()
for row in ans:
  print('Linha: ', row)



lastRecord = consultaLastRecord('PAI')

for v in lastRecord:
  print('Dtype: ', v['DTYPE'], ' e valor: ', v['VALUE'])

