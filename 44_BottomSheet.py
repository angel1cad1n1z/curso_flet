import flet as ft


def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100

    def show_bs(e):
        bs.open = True
        page.update()

    def hide_bs(e):
        bs.open = False
        page.update()

    bs = ft.BottomSheet(
        content=ft.Container(
            ft.Column(
                controls=[
                    ft.Text(value="Título", style=ft.TextThemeStyle.HEADLINE_LARGE),
                    ft.Text(
                        value="Conteúdo do BottomSheet",
                        style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                    ),
                    ft.FilledButton(text="Fechar", on_click=hide_bs),
                ]
            ),
            padding=20,
        ),
        # se for definido como false não consegue mais fechar a janela e para fechar precisa de um botão para realizar essa ação.
        dismissible=False,
        # possibilita clicar e arrastar o bottomsheet na vertical - podendo expandir ou minimizar
        enable_drag=True,
        # indica se está ou não sendo controlado pelo scroll
        is_scroll_controlled=False,
        # adiciona um espaçamento inferior para não afetar os botões do celular
        maintain_bottom_view_insets_padding=True,
        # tracinho na parte superior que indica ao usuário que pode manusear o bottomSheet
        show_drag_handle=True,
    )

    page.overlay.append(bs)

    btn1 = ft.ElevatedButton(text="Abrir BottomSheet", on_click=show_bs)
    page.add(btn1, bs)


if __name__ == "__main__":
    ft.app(target=main)
