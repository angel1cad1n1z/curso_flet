import flet as ft


def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100
    
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Início"),
            ft.NavigationBarDestination(icon=ft.Icons.CHAT, label="Chat"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Favorites",
            ),
        ],
        selected_index= 1,
        # cor de fundo do ícone
        indicator_color=ft.Colors.BLUE,
        # formato da cor de fundo - se for 0 fica quadrado
        indicator_shape=ft.RoundedRectangleBorder(radius=14),
        on_change= lambda e: print(e.control.selected_index),
    )
    
    page.update()

if __name__ == "__main__":
    ft.app(target=main)