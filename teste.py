from flet import *

def main(page: Page):
    page.title = "Flet counter example"
    numero = TextField(value="0", text_align=TextAlign.RIGHT, width=100)

    def minus_click(e):
        numero.value = str(int(numero.value) - 1)
        page.update()

    def plus_click(e):
        numero.value = str(int(numero.value) + 1)
        page.update()

    page.add(
        Row(
            [
                IconButton(Icons.REMOVE, on_click=minus_click),
                numero,
                IconButton(Icons.ADD, on_click=plus_click),
            ]
            
        )
    )

app(main)