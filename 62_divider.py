import flet as ft


# criar espaçamentos personalizados
def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    # page.bgcolor = ft.Colors.BLUE_GREY_100
    # page.scroll = ft.ScrollMode.AUTO

    page.add(
        ft.Column(
            spacing=0,
            expand=True,
            controls=[
                ft.Container(
                    bgcolor=ft.Colors.AMBER,
                    expand=True,
                ),
                ft.Divider(),
                ft.Container(
                    bgcolor=ft.Colors.BLUE,
                    expand=True,
                ),
                ft.Divider(
                    # espessura
                    height=5
                ),
                ft.Container(
                    bgcolor=ft.Colors.DEEP_PURPLE,
                    expand=True,
                ),
                ft.Divider(
                    # altura do divider
                    height=50,
                    # aumenta a espessura da linha
                    thickness=10,
                    color=ft.Colors.BLUE,
                ),
                ft.Container(
                    bgcolor=ft.Colors.RED,
                    expand=True,
                ),
            ],
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
