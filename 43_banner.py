import flet as ft


def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100

    def close_banner(e):
        page.close(bn1)
        page.update()

    def open_banner(e):
        page.open(bn1)
        page.update()

    # VERIFICAR ERRO!!!!!!!
    bn1 = ft.Banner(
        actions=[
            ft.TextButton(
                text="Cancelar",
                style=ft.ButtonStyle(color=ft.Colors.RED),
                visible=True,
                on_click=close_banner,
            ),
            ft.ElevatedButton(
                text="Tentar novamente",
                style=ft.ButtonStyle(bgcolor=ft.Colors.BLACK, color=ft.Colors.WHITE),
                visible=True,
                on_click=close_banner,
            ),
        ],
        content=ft.Text(value="Ops, parece que não conseguimos processar  sua ação."),
        content_padding=ft.padding.all(10),
        # ícone que fica ao lado do texto - antes dele.
        leading=ft.Icon(name=ft.Icons.WARNING_AMBER),
        # força para que os actions fiquem na parte inferior do banner - serve como um reforço de layout
        force_actions_below=True,
        bgcolor=ft.Colors.PINK_100,
    )

    btn1 = ft.ElevatedButton(text="Abrir Banner", on_click=open_banner)

    page.add(btn1, bn1)


if __name__ == "__main__":
    ft.app(target=main)
