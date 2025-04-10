import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    
    # ele não tem cor de fundo apenas o nome e uma borda definida
    # e assim como filled button segue o tema da aplicação
    # mais utilizado quando queremos ter um botão com um estilo padrão para toda a aplicação
    btn1 = ft.OutlinedButton(
        text="ZOOM",
        icon= ft.Icons.ZOOM_IN,
        icon_color= ft.Colors.TEAL,
        style= ft.ButtonStyle(
            shape= ft.RoundedRectangleBorder(radius= 10)
        ),
        on_click= lambda _: print('Fui clicado!'),
    )
    page.add(btn1)
    
ft.app(target=main)