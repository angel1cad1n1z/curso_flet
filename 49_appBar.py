import flet as ft
import datetime


def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100

    # adiciona um appbar na página
    # o appbar é um componente que é usado para adicionar um cabeçalho na página
    # é usado para adicionar um ícone, um titulo, um botão e um menu popup
    # fica fixo no topo da página
    page.appbar = ft.AppBar(
        # adiciona um ícone na esquerda
        # Pode utilzar esse ícone home para sempre que quiser voltar para a tela inicial
        leading=ft.Icon(ft.Icons.HOME),
        # altera a largura do ícone
        leading_width=40,
        # adiciona um titulo
        title=ft.Text("App Fit", color=ft.Colors.BLACK),
        # centraliza o titulo ou não caso esteja False
        center_title=True,
        # altera a altura da toolbar
        toolbar_height=50,
        # altera a cor dos componentes do appbar
        color=ft.Colors.ORANGE,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        # adiciona um botão na direita
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.Icons.NOTIFICATIONS),
            ft.CircleAvatar(content=ft.Text("Lika"), color=ft.Colors.GREEN),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Meud dados"),
                    ft.PopupMenuItem(text="Configurações"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        padding=ft.padding.all(0),
                        text="Sair",
                        checked=False,
                        on_click=lambda _: print("Saiu"),
                    ),
                ]
            ),
        ],
    )

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
