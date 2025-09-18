import flet as ft


# criar espaçamentos verticais personalizados
def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    # page.bgcolor = ft.Colors.BLUE_GREY_100
    # page.scroll = ft.ScrollMode.AUTO
    
    page.add(ft.Row(
        expand=True,
        spacing=0,
        controls=[
                ft.Container(
                    bgcolor=ft.Colors.AMBER,
                    expand=True,
                ),
                ft.VerticalDivider(),
                ft.Container(
                    bgcolor=ft.Colors.BLUE,
                    expand=True,
                ),
                ft.VerticalDivider(
                    # espessura
                    width=5
                ),
                ft.Container(
                    bgcolor=ft.Colors.DEEP_PURPLE,
                    expand=True,
                ),
                ft.VerticalDivider(
                    # altura do divider
                    width=50,
                    # aumenta a espessura da linha
                    thickness=10,
                    color=ft.Colors.BLUE,
                ),
                ft.Container(
                    bgcolor=ft.Colors.RED,
                    expand=True,
                ),
            ],
    ))
    
if __name__ == "__main__":
    ft.app(target=main)