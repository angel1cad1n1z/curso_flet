import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.RED
        # opções:
            # "white"
            # ft.Colors.white (aqui tem as cores já pré-definidas) 
    
    page.update()
    
    
ft.app(target= main)