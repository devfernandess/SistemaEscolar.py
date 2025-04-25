from flet import *
#from conection import *

def main (page:Page):
    page.window.center()
    page.window_width  = 768
    page.window.height = 500
    page.bgcolor = "white"
    page.padding = 0

    #Tela de login
    titulolog = Text("Login", color="black", size=30, weight= FontWeight.W_900 )
    emaillog = TextField(label="Digite seu usuário", prefix_icon= icons.EMAIL, password= True, border_radius=15)
    senhalog = TextField(label="Digite sua senha", prefix_icon= icons.PASSWORD, password= True, border_radius=15)
    btnlog = FilledButton(text="Entrar", style = ButtonStyle(bgcolor="#1534c0", color="#ffffff"), width=250, height=50)
    #Botao de mudar para tela de cadastro
    txtcad = Text("Ainda nao possui uma conta? Faça seu cadastro", size = 15, color="#ffffff", font_family="bold")
    mudarpracad = FilledButton(text="Faça seu cadastro", on_click= lambda e: mudarpracad(e), style = ButtonStyle(bgcolor="#ffffff", color="black"), width=250, height=50)

    #.............................................................................................

    #Tela de cadastro
    titulocad = Text("Cadastro", color="black", size = 30, weight= FontWeight.W_900)
    emailcad = TextField(label="Digite seu email", prefix_icon= icons.EMAIL, border_radius=15)
    senhacad = TextField(label="Crie uma senha", prefix_icon= icons.PASSWORD, password= True, border_radius=15)
    confirmesenha = TextField(label="Confirme a senha", prefix_icon= icons.PASSWORD, password= True, border_radius=15 )
    btncad = FilledButton(text="Cadastrar", on_click= True, style = ButtonStyle(bgcolor="#1534c0", color="#ffffff"), width=250, height=50)
    g = Text("")

    #Botao de mudar para login
    txt = Text("Ja possui uma conta? Faça login", size = 15, color="#ffffff", font_family="bold")
    mudarpralog = FilledButton(text="Login", on_click= lambda e: mudarpralog(e), style = ButtonStyle(bgcolor="#ffffff", color="black"), width=250, height=50 )

    cadastro = Row([

        Container( height=500, width=334, bgcolor="#1534c0", border_radius = border_radius.only(top_right=100, bottom_right=100), padding = 30,
            content= Column([
                
                        txt, mudarpralog

            ], alignment = MainAxisAlignment.CENTER, horizontal_alignment= CrossAxisAlignment.CENTER)
            
         ),

        Container( height=500, width=404, padding = 30,
            content= Column([
                titulocad, emailcad, senhacad, confirmesenha, btncad, g
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
            height=500, width=364, bgcolor="#1534c0", border_radius = border_radius.only(top_left=100, bottom_left=100), padding =30,
           
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


    # def salvar(e):

    #     email = emailcad.value
    #     senha = senhacad.value
    #     msg = g.value

    #     email.value= ""
    #     senha.value = ""

    #     if email and senha:
    #         conn, status = conectar_banco()
    #         if conn:
    #             result = inserir_dados(conn, email, senha)
    #             msg.value = result
    #             conn.close()
    #         else:
    #             msg.value = status
    #     else:
    #         msg.value = "Por favor, insira seu nome!"
    #     page.update()

    page.add(login)

app(target=main)














