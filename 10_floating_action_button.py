import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    # botão flutuante
    # fica por cima da aplicação
    # útil para uma ação rápida como adiconar algum item numa lista
    # se adicionar um texto o elemento mini não funciona
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        bgcolor=ft.Colors.BLUE,
        mini=True,
        shape= ft.CircleBorder(),
        tooltip= "Add novo item",
        on_click= lambda _: print("Fui clicado!"),
    )
    
    page.add(
        ft.Container(
            content= ft.FloatingActionButton(text='Botão flutuante'),
            bgcolor= ft.Colors.BLUE,
            height= 400,
            alignment= ft.Alignment(x=0,y=0)
            ),
        )
    
    page.update()
    
ft.app(target=main)