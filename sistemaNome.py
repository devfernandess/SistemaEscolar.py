from flet import *
from conexao import *

def main(page:Page):

    t= TextField(label= "Nome", autofocus= True)
    tfturma= TextField(label= "Turma", autofocus= True)
    b= FilledButton(text="salvar",on_click= lambda e: salvar(e))
    g= Text("",size=50)

    def salvar(e):

        nome = t.value
        turma = tfturma.value

        t.value= ""
        tfturma.value = ""

        if nome and turma:
            conn, status = conectar_banco()
            if conn:
                result = inserir_NOME(conn, nome, turma)
                g.value = result
                conn.close()
            else:
                g.value = status
        else:
            g.value = "Por favor, insira seu nome!"

    page.add(t,tfturma, b, g)

app(target = main)