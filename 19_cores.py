import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    
    containers = [
        ft.Container(height= 150, width= 150, bgcolor= ft.Colors.AMBER),
        ft.Container(height= 150, width= 150, bgcolor= 'deeporange'),
        ft.Container(height= 150, width= 150, bgcolor= '#FC6954'),
        ft.Container(height= 150, width= 150, bgcolor= ft.Colors.with_opacity(0.5, '#FC76')), # O VALOR DA OPACIDADE VAI DE 0 ATÉ 1
        ft.Container(height= 150, width= 150, bgcolor= ft.Colors.with_opacity(1, '#FC7896')),
        ft.Container(height= 150, width= 150, bgcolor= ft.Colors.with_opacity(0.25, '#CF78')),
    ]
    page.add(*containers)

ft.app(main)