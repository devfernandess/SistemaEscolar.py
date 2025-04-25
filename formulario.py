from flet import *

def main (page:Page):
    page.window.center()
    page.window_width  = 768
    page.window.height = 500
    page.bgcolor = "white"
    page.padding = 0

    #Tela de login
    titulolog = Text("Login", color="black", size=40, weight= FontWeight.W_900 )
    emaillog = TextField(label="Digite seu usuário", prefix_icon= icons.EMAIL, password= True )
    senhalog = TextField(label="Digite sua senha", prefix_icon= icons.PASSWORD, password= True)
    btnlog = FilledButton(text="Entrar",)

    #Botao de mudar para tela de cadastro
    txtcad = Text("Ainda nao possui uma conta? Faça seu cadastro", size = 15)
    mudarpracad = FilledButton(text="Faça seu cadastro", on_click= lambda e: mudarpracad(e))

    #.............................................................................................

    #Tela de cadastro
    titulocad = Text("Cadastro", color="black", size = 30, weight= FontWeight.W_900)
    emailcad = TextField(label="Digite seu email", prefix_icon= icons.EMAIL)
    senhacad = TextField(label="Crie uma senha", prefix_icon= icons.PASSWORD, password= True)
    confirmesenha = TextField(label="Confirme a senha", prefix_icon= icons.PASSWORD, password= True )
    btncad = FilledButton(text="Cadastrar")

    #Botao de mudar para login
    txt = Text("Ja possui uma conta? Faça login", size = 15)
    mudarpralog = FilledButton(text="Login", on_click= lambda e: mudarpralog(e) )

    cadastro = Row([

        Container( height=500, width=334, bgcolor="blue", border_radius = border_radius.only(top_right=100, bottom_right=100), padding = 30,
            content= Column([
                
                        txt, mudarpralog

            ], alignment = MainAxisAlignment.CENTER, horizontal_alignment= CrossAxisAlignment.CENTER),
            
         ),

        Container( height=500, width=404, padding = 30,
            content= Column([
                titulocad, emailcad, senhacad, confirmesenha, btncad
            ], alignment = MainAxisAlignment.CENTER, horizontal_alignment= CrossAxisAlignment.CENTER)
        )

    ])


    login = Row([
       

        Container(
            height=500,width=404,padding =30,
            content= Column([
                titulolog, emaillog, senhalog, btnlog
            ], alignment = MainAxisAlignment.CENTER, horizontal_alignment= CrossAxisAlignment.CENTER)
        ),

         Container(
            height=500, width=364, bgcolor="blue", border_radius = border_radius.only(top_left=100, bottom_left=100), padding =30,
           
            content= Column([
                txtcad, mudarpracad
            ], alignment = MainAxisAlignment.CENTER, horizontal_alignment= CrossAxisAlignment.CENTER)
        )

    ])


    def mudarpracad(e):
        page.clean()
        page.add(cadastro)

    def mudarpralog(e):
        page.clean()
        page.add(login)


    page.add(login)

app(target=main)














