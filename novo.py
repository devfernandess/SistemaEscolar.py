from flet import *

def main (page:Page):

    n = TextField(label= "Digite seu nome: ")
    btn = FilledButton(text = "Salvar", on_click=lambda e: salvar(e))
    t = Text("",size = 50)

    def salvar(e): 
       
        if n.value == "Guilherme": 
            
            t.value ="Ta certo "
            t.color = 'green'
        
        else:

            t.value = "Errado"
            t.color = colors.RED_ACCENT

        n.value = ""

        page.update()

    page.add(n, btn, t)

app(target=main)

