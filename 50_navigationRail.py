import flet as ft


def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100

    rail = ft.NavigationRail(
        # pode ser qualquer elemento que fica no início do navigation
        leading=ft.CircleAvatar(ft.Text('Lika')),
        # pode ser qualquer elemento para ficar no final do navigation
        trailing=ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text='Cadastrar novo'),
                ft.PopupMenuItem(text='Enviar em massa')]),
        bgcolor=ft.Colors.TRANSPARENT,
        # índice do elemento que vai ficar selecionado
        selected_index=0,
        # aumenta  o espaço do navigation e altera a disposição dos ícones e dos nomes
        extended=False,
        label_type=ft.NavigationRailLabelType.SELECTED,
        # vai ocupar no mínimo a quantidade de pixels que for definida
        min_width=60,
        min_extended_width=150,
        group_alignment=-0.9,
        on_change=lambda e: print(e.control.selected_index),
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.HOME,
                label="Home",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Itens salvos",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.SEARCH),
                selected_icon=ft.Icon(ft.Icons.SEARCH_ROUNDED),
                label="Pesquisar",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS,
                label="Settings",
            ),
        ],
    )

    row = ft.Row(
        controls=[
            rail,
            ft.VerticalDivider(width=1),
        ],
        expand=True,
    )

    page.add(row)


if __name__ == "__main__":
    ft.app(target=main)
