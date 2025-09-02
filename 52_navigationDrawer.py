import flet as ft


# util para telas menores
# aparece por cima da aplicação
def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100

    drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Item 01",
                icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
            ),
            ft.NavigationDrawerDestination(
                label="Item 02",
                icon=ft.Icons.HOME,
                selected_icon=ft.Icon(ft.Icons.HOME),
            ),
            ft.NavigationDrawerDestination(
                label="Item 03",
                icon=ft.Icons.CHAT_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.CHAT),
            ),
            ft.ElevatedButton(
                text="oi",
                icon=ft.Icons.FACE,
            )
        ],
        bgcolor=ft.Colors.BLUE,
        indicator_color=ft.Colors.WHITE,
        indicator_shape=ft.RoundedRectangleBorder(20),
        selected_index=0,
        # espaçamento entre os navigation destinations
        tile_padding=ft.padding.all(5),
        on_change= lambda e: print(e.control.selected_index),
        
    )

    def show_drawer(e):
        page.open(drawer)
        drawer.update()

    btn = ft.IconButton(icon=ft.Icons.MENU, on_click=show_drawer)
    page.add(btn)

if __name__ == "__main__":
    ft.app(target=main)
