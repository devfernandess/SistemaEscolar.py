import sqlite3 as db
from sqlite3 import *

def conectar_banco():
    try:
        conn= db.connect("sistemaescolar.db")
        return conn, "Conexão bem sucedida!"
    except Error as e:
        return None, f"Error ao conectar: {e}"
    
def inserir_nome(conn, nome_aluno):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO aluno (NOME) VALUES(?) "
        cursor.execute(query, (nome_aluno))
        conn.commit()
        return "Nome inserido com sucesso!"
    
    except Error as e:
        return f"Erro ao inserir nome: {e} "