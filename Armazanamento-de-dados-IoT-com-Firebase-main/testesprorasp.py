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

  curs.execute("""
    CREATE TABLE IF NOT EXISTS data (
      ID_DATA INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      END_DEVICE_NAME TEXT NOT NULL,
      DTYPE TEXT NOT NULL,
      VALUE REAL,
      DATE_CREATED DATE NOT NULL
    );
  """)

  conn.commit()
  conn.close()


def insert(device_name, dtype, valor):
  conn = sqlite3.connect('data.db')
  curs = conn.cursor()

  curs.execute("INSERT INTO data (END_DEVICE_NAME, DTYPE, VALUE, DATE_CREATED) VALUES ('" + device_name +"', '" + dtype +"', "+valor+", datetime('now'))")

  conn.commit()
  conn.close()
  ## @TODO return true ou false
  return curs.lastrowid


def consultaLastRecord(device_name):
  conn = sqlite3.connect('data.db')
  curs = conn.cursor()

  query = "SELECT END_DEVICE_NAME, DTYPE, VALUE, max(DATE_CREATED) from data WHERE END_DEVICE_NAME = '"+device_name+"' group by DTYPE"
  curs.execute(query)
  results = curs.fetchall()
  result_dict = []

  for row in results:
    row_dict = {}
    for i, col in enumerate(curs.description):
      row_dict[col[0]] = row[i]
    result_dict.append(row_dict)

  conn.commit()
  conn.close()
  return result_dict
 

create_table()
lastRecord = consultaLastRecord('PAI')


