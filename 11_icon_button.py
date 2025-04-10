import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    
    # exclusivo para botões que tem apenas ícones
    btn1 = ft.IconButton(
        icon= ft.Icons.DELETE_FOREVER_ROUNDED,
        icon_color= ft.Colors.PINK,
        icon_size= 100,
        tooltip= "deletar"
        )
    
    def play_pause(e):
        # aqui basta reverter a lógica como selected está como false ao clicar no botão ele vai ser true e assim sucessivamente
        # ela simplesmente troca o valor do selected que colocamos la na btn2
        e.control.selected = not e.control.selected
        e.control.update()

    # temos um botão que vai servir como play e pause
    # ele inicia como play
    # no selected_icon colocamos o ícone de pause
    # iniciamos o selected como false para que ele mostre primeiro o play
    # e no onclick chamamos a função que vai pegar o evento de clique e mudar o ícone
    btn2 = ft.IconButton(
        icon= ft.Icons.PLAY_CIRCLE,
        selected_icon= ft.Icons.PAUSE_CIRCLE,
        selected= False,
        icon_size= 150,
        on_click=play_pause,
        style = ft.ButtonStyle(
            color= {
                ft.ControlState.SELECTED: ft.Colors.PINK,
                ft.ControlState.DEFAULT: ft.Colors.BLUE,
            }
        )
    )
    page.add(btn1, btn2)
    
ft.app(target=main)