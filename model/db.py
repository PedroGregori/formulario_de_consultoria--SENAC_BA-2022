import sqlite3

FILE_DB ='./database/consultoria.db'

def connect():
    conn = sqlite3.connect(FILE_DB)
    return conn