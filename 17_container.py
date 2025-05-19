import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    page.bgcolor="white"

    container = ft.Container(
        # height= 750,
        # width= 500,
        expand= True,
        # image=ft.DecorationImage(
            # src="https://wallpapers.com/images/hd/all-black-background-3mn1yythw6rvnlxf.jpg",
            # fit= ft.ImageFit.FILL),
        margin= ft.margin.all(10),
        # border=ft.border.all(width=5, color= ft.Colors.BLUE_200),
        # border= ft.border.only(
        #     top= ft.BorderSide(width= 5, color= ft.Colors.PINK),
        #     left= ft.BorderSide(width= 5, color= ft.Colors.ORANGE),
        #     right= ft.BorderSide(width= 5, color= ft.Colors.GREEN),
        #     bottom= ft.BorderSide(width= 5, color= ft.Colors.BLUE),
        # )
        # border=ft.border.symmetric(
        #     vertical=ft.BorderSide(width=5, color= ft.Colors.BLUE),
        #     horizontal=ft.BorderSide(width=5,color= ft.Colors.BLUE_200),
        # ),
        # border_radius=ft.border_radius.all(50), # não funciona se tiver uma cor de borda 
        # border_radius=ft.border_radius.horizontal(left=10, right=40),
        # border_radius=ft.border_radius.vertical(top=10, bottom=65),
        border_radius=ft.border_radius.only(
            top_left= 20,
            top_right= 52,
            bottom_left= 85,
            bottom_right= 45
            ),
        content= ft.Row(
            controls=[
                ft.ElevatedButton(text= "1", color=ft.Colors.BLACK, bgcolor=ft.Colors.BLUE),
                ft.ElevatedButton(text= "2", color=ft.Colors.BLACK, bgcolor=ft.Colors.BLUE),
                ft.ElevatedButton(text= "3", color=ft.Colors.BLACK, bgcolor=ft.Colors.BLUE),
                ft.ElevatedButton(text= "4", color=ft.Colors.BLACK, bgcolor=ft.Colors.BLUE),
                ft.ElevatedButton(text= "5", color=ft.Colors.BLACK, bgcolor=ft.Colors.BLUE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        # padding=ft.padding.all(15), #se tiver utilizando o alignment na row não precisa aqui, pelo que eu entendi
        shape=ft.BoxShape.RECTANGLE, # Deixa o container no farmato de um retângulo - como padrão já é retângulo entao não precisa utilizar
        # shape=ft.BoxShape.RECTANGLE, # Deixa o container no farmato de um círculo
        bgcolor=ft.Colors.BLUE_200,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.Colors.BLUE_200, ft.Colors.AMBER]
        ),
        # o shadow pode receber apenas uma borda ou uma lista delas
        shadow=[
            ft.BoxShadow(
            # spread_radius=10, #cria uma borda que se expande 10px além do tamanho do container
            blur_radius=50, # borda esfumaçada
            color=ft.Colors.BLUE_200, # cor da sombra
            # blur_style=ft.ShadowBlurStyle.INNER, # aplica a sombra dentro do componente - mas se o componente tiver uma cor de fundo não dá para vizualizar
            # blur_style=ft.ShadowBlurStyle.OUTER, # aplica a sombra apenas forado container, caso o spread_radius seja definido aparece o esfumaçado aparece após ele
            # blur_style=ft.ShadowBlurStyle.SOLID, # aplica uma cor solida na borda do container
            blur_style=ft.ShadowBlurStyle.NORMAL, # aplica a sombra tanto dentro como fora do conatiner
            offset=ft.Offset(x= 50, y=40),
        ),
            ft.BoxShadow(
            # spread_radius=10, #cria uma borda que se expande 10px além do tamanho do container
            blur_radius=0, # borda esfumaçada
            color=ft.Colors.RED_200, # cor da sombra
            # blur_style=ft.ShadowBlurStyle.INNER, # aplica a sombra dentro do componente - mas se o componente tiver uma cor de fundo não dá para vizualizar
            # blur_style=ft.ShadowBlurStyle.OUTER, # aplica a sombra apenas forado container, caso o spread_radius seja definido aparece o esfumaçado aparece após ele
            # blur_style=ft.ShadowBlurStyle.SOLID, # aplica uma cor solida na borda do container
            blur_style=ft.ShadowBlurStyle.NORMAL, # aplica a sombra tanto dentro como fora do conatiner
            offset=ft.Offset(x= -50, y=-40),
        ),
        ]
    )
    page.add(container)

ft.app(main)