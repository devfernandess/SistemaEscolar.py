
import flet as ft
import conexao as con

def main (page:ft.Page):
    page.window_center()
    page.window.width= 1200
    page.window.height= 650
    page.bgcolor= "#000000"
    page.window.maximizable = False
    page.window.resizable = False
    page.padding = 0
    #page.window_title_bar_hidden = True
   

    nomealuno= ft.TextField(label="Digite seu nome", )
    turmaaluno= ft.TextField(label="Digite sua turma", )

    dt=ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID aluno")),
                ft.DataColumn(ft.Text("Nome") ),
                ft.DataColumn(ft.Text("Turma"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
                    ],
                ),
            ],
        )
   

    btn= ft.FilledButton(text="Salvar", on_click= lambda e:salvar(e))

    def salvar(e):
        nome= nomealuno.value
        turma = turmaaluno.value

        nomealuno.valu=""
        turmaaluno=""

        if nome and turma:
            conn,status = con.conectar_banco()
            if conn:
                result= con.inserir_nome(conn,nome,turma)
                result.value = result
                conn.close()

                
        
        page.add()
  



    page.add(nomealuno, turmaaluno, dt, btn)

ft.app(target = main)