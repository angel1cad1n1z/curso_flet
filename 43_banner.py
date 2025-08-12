import flet as ft


def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100
    
    page.add()
    
if __name__ == "__main__":
    ft.app(target=main)