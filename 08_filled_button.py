import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    # não pode alterar a cor do texto nem a cor do fundo
    # o filled button utiliza as cores padrão do tema
    # precisa fazer a personalização do tema para que o botão possa ser alterado automaticamente
    btn1 = ft.FilledButton(text= 'Botão primário')
    btn2 = ft.FilledButton(
        text="Botão com ícone",
        icon= ft.Icons.FAVORITE,
        icon_color= ft.Colors.RED)
    
    style = ft.ButtonStyle(
        padding= 50,
        animation_duration= 350,
        side= {
            ft.ControlState.DEFAULT: ft.BorderSide(2, ft.Colors.AMBER),
            ft.ControlState.HOVERED: ft.BorderSide(10, ft.Colors.RED),
        },
        shape= {
            ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=15),
            ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=20),
        }
    )
    btn3 = ft.FilledButton(text= 'Botão personalizado', style= style )
    btn4 = ft.FilledButton(
        text="Botão com link",
        url="https://www.google.com/",
        tooltip= "Clique aqui para ir para o Google",
        )
    
    
    page.add(btn1, btn2, btn3, btn4)

ft.app(target= main)