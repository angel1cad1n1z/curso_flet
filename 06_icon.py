import flet as ft

# CONSEGUIMOS MAIS OPÇOES DE ICONES NO SITE GO FLET/GALERIA
def main(page: ft.Page):
    page.window.always_on_top= True
    icon1 = ft.Icon(name= ft.Icons.FAVORITE, color= ft.Colors.BLUE, size= 30)
    icon2 = ft.Icon(name= ft.Icons.SEARCH, color= ft.Colors.RED, size= 30)
    icon3 = ft.Icon(name= 'settings', color= ft.Colors.AMBER, size= 30)
    icon4 = ft.Icon(name= ft.Icons.BEACH_ACCESS, color= ft.Colors.GREEN, size= 30)
    
    page.add(icon1, icon2, icon3, icon4)
    
ft.app(target= main)