import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    
    btn1 = ft.TextButton(
        text="Editar",
        icon= ft.Icons.EDIT,
        icon_color= ft.colors.GREEN,
        tooltip= "Clique aqui para editar o texto",
        on_click= lambda e: print("Editando o texto..."),
        url= "https://www.google.com",
        style= ft.ButtonStyle(
            color= ft.colors.GREEN,
            overlay_color= ft.colors.BLACK,
        )
    )
    
    page.add(btn1)

ft.app(target= main)