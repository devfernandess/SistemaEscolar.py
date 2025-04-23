from flet import *

def main1(page:Page):
    page.window_height="500"
    page.window_width="768"
    page.bgcolor="blue"



    
    

    def telalogin(page:Page):
        page.window_width="384"
        page.window_height="500"
        btncad = FilledButton(text="Mostrar Cadastro", on_click= lambda e: mostrarcad(e))
        page.bgcolor="red"
        page.update()



    def telacad(page:Page):
        page.window_width="384"
        page.window_height="500"
        btnlogin = FilledButton(text="Mostrar Login", on_click= lambda e: mostrarlogin(e))
        page.bgcolor="red"
        page.update


    def mostrarlogin(e: ControlEvent):
        page.add(telalogin)
        page.remove(telacad)
        page.update()
    
    def mostrarcad(e: ControlEvent):
        page.add(telacad)
        page.remove(telalogin)
        page.update()



    page.add(telalogin, telacad)

app(target=main1)
    






    