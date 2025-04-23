import sqlite3 as db
from sqlite3 import *

def conectar_banco():
    try:
        conn= db.connect("banconovo.db")
        return conn, "Conexão bem sucedida!"
    except Error as e:
        return None, f"Error ao conectar: {e}"
    
def inserir_NOME(conn, nome, turma ):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO aluno (nome, turma) VALUES(?,?)"
        cursor.execute(query, (nome, turma,))
        conn.commit()
        return "Nome inserido com sucesso!"
    
    except Error as e:
        return f"Erro ao inserir nome: {e} "
