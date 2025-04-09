import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    page.spacing = 50
    btn1 = ft.ElevatedButton(text = "Clique aqui")
    btn2 = ft.ElevatedButton(text = "Botão Inativo", disabled= True)
    btn3 = ft.ElevatedButton(text = "Botão com ícone", icon= ft.Icons.FAVORITE) # Por padrão o ícone sempre vem antes do texto
    btn4 = ft.ElevatedButton(
        text = "Demais propriedades",
        bgcolor = ft.Colors.BLUE,
        color =  ft.Colors.RED,
        icon = ft.Icons.FAVORITE,
        icon_color = ft.Colors.WHITE,
        tooltip="demais propriedades",
        url="https://www.google.com/",
        )
    
    style = ft.ButtonStyle(
        color = {
            ft.ControlState.HOVERED: ft.Colors.WHITE,
            ft.ControlState.DISABLED: ft.Colors.GREEN,
            ft.ControlState.DEFAULT: ft.Colors.BLACK,
        },
        bgcolor = {
            ft.ControlState.HOVERED: ft.Colors.PINK,
            ft.ControlState.DISABLED: ft.Colors.BLACK,
            ft.ControlState.DEFAULT: ft.Colors.RED,
        },
        padding={
            ft.ControlState.HOVERED: 20,
            ft.ControlState.DEFAULT: 15,
        },
        animation_duration= 1000,
        side = {
            ft.ControlState.HOVERED: ft.BorderSide(width=3, color=ft.Colors.BLACK),
            ft.ControlState.DEFAULT: ft.BorderSide(width=3, color=ft.Colors.ORANGE),
        },
        shape = {
            ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=15),
            ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=10),
            
        }
    )

    btn5 = ft.ElevatedButton(text = "Botão com estilo personalizado", style= style, disabled= True)
    
    page.add(btn1, btn2, btn3, btn4, btn5)
    
    def button_cliked(e):
        # control = controle que ativa o evento do botão
        e.control.data += 1
        text1.value = f'botão acionado { e.control.data} vezes'
        text1.update()
        e.control.update()
        
    btn = ft.ElevatedButton(
        text = "+",
        on_click= button_cliked,
        data = 0,
    )
    
    text1 = ft.Text()
    page.add(btn, text1)
    
    def button_cliked1(e):
        # control = controle que ativa o evento do botão
        e.control.data -= 1
        text2.value = f'botão minimizado { e.control.data} vezes'
        text2.update()
        e.control.update()
        
    btn2 = ft.ElevatedButton(
        text = "-",
        on_click= button_cliked1,
        data = 10,
    )
    
    text2 = ft.Text()
    page.add(btn2, text2)
    
ft.app(target= main)

"""
legenda
    tooltip:  tipo de texto que aparece sempre que passamos o mouse encima do botão
    controlState houvered: quando passa o mouse em cima do botão o texto vai ficar de uma determinada cor
    controlState default: define uma cor para o texto padrão
    controlState focused: quando apertamos tab e estamos navegando entre os elementos da tela
    shape: formato que o botão vai ter, redondo, oval, quadrado
    borderside: ajusta cor e tamanho da borda do botão
    padding: ajusta o tamanho do botão
    animation-duration: ajusta a animação para mudar de um moda para outro 
    ft.ControlState.DEFAULT: ft.StadiumBorder() - é a borda padrão
    ft.ControlState.DEFAULT: ft.CircleBorder() - vira um círculo mesmo - apropriado quando tiver usando um ícone
    ft.ControlState.DEFAULT: ft.BeveledRectangleBorder(radius = 4) - ele faz um corte nas bordas
    ft.ControlState.DEFAULT: ft.ContinuiusRectangleBorder(radius=5)
"""