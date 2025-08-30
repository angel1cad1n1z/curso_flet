import flet as ft
import datetime


def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100

    t = ft.Tabs(
        tabs=[
            ft.Tab(
                text="Tab 01",
                content=ft.Container(
                    padding=ft.padding.all(10),
                    content=ft.Text("Conteúdo Tab 01"),
                ),
            ),
            ft.Tab(
                icon=ft.Icons.SETTINGS,
                content=ft.Text("Conteúdo Tab 02"),
            ),
            ft.Tab(
                tab_content=ft.Container(
                    content=ft.CircleAvatar(
                        foreground_image_src="https://images.vexels.com/media/users/3/147101/isolated/preview/b4a49d4b864c74bb73de63f080ad7930-botao-de-perfil-do-instagram.png",
                        tooltip="Programador Aventureiro",
                        badge=ft.Badge(bgcolor=ft.Colors.GREEN, small_size=10),
                    )
                )
            ),
        ],
        # qual índice será selecionado por padrão - inicia do 0
        selected_index=1,
        animation_duration=300,
        # cor da linha que divide o conteudo da tela dos títulos de tab na parte superior
        divider_color=ft.Colors.AMBER,
        # altera a cor da linhazinha que fica abaixo da tag selecionada
        indicator_color=ft.Colors.BLUE,
        indicator_border_radius=ft.border_radius.all(10),
        indicator_padding=ft.padding.all(5),
        # se for true ocupa todoo espaço do nome ou ícone da tab
        indicator_tab_size=True,
        # cor do texto ou do ícone das tabs quando estiver selecionado
        label_color=ft.Colors.BLACK,
        # cor para quando não tiver selecionado
        unselected_label_color=ft.Colors.ORANGE,
        overlay_color={
            # quando passar o mouse pelas tabs fica com o fundo rosa
            ft.ControlState.HOVERED: ft.Colors.PINK,
        },
        scrollable=False,
    )

    page.add(t)


if __name__ == "__main__":
    ft.app(target=main)
