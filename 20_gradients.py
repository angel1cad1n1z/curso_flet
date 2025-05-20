import flet as ft
import math

def main(page: ft.Page):
    page.window.always_on_top= True
    
    containers = [
        ft.Container(
            expand = True,
            # por padrão ele aplica o linear horizontalmente
            # podemos escolher 2 ou mais opções de cores
            gradient = ft.LinearGradient(
                begin= ft.alignment.top_center, # vai da margem central esquerda
                # begin= ft.alignment.top_left, # margem central esquerda
                end= ft.alignment.bottom_center, # margem central direita
                # end= ft.alignment.bottom_right, #margem inferior direita
                colors= [ft.Colors.BLUE, ft.Colors.AMBER_300, ft.Colors.PURPLE,],
                stops= [0, 0.5, 1], # vai de 0 a 1
                rotation= math.radians(70) # consegue rotacionar a posição do gradient e  podemos usar  o math.radians para ajustar essa rotação
                ),
        ),
        ft.Container(
            expand = True,
            # por padrão ele começa a cor pelo centro e vai seguindo para as bordas
            #  o centro é 0 e as laterais são o 1
            gradient = ft.RadialGradient(
                # begin= ft.alignment.top_center, # vai da margem central esquerda
                # # begin= ft.alignment.top_left, # margem central esquerda
                # end= ft.alignment.bottom_center, # margem central direita
                # # end= ft.alignment.bottom_right, #margem inferior direita
                colors= [ft.Colors.BLUE, ft.Colors.AMBER_200, ft.Colors.PURPLE,],
                stops= [0, 0.5, 1], # vai de 0 a 1
                center= ft.Alignment( x=0.5, y=-0.5,), # 0 a 1 / 0 a -1
                radius= 1.5, # por padrão é 0.5
                ),
        ),
        ft.Container(
            expand = True,
            # por padrão ele começa a cor pelo centro e vai seguindo para as bordas
            #  o centro é 0 e as laterais são o 1
            gradient = ft.SweepGradient(
                colors= [ft.Colors.RED, ft.Colors.BLACK, ft.Colors.PINK],
                stops= [0, 0.5, 1], # vai de 0 a 1
                center= ft.Alignment( x=0, y=1), # 0 a 1 / 0 a -1
                rotation= math.radians(30)
            )
        ),
    ]
    page.add(*containers)

ft.app(main)