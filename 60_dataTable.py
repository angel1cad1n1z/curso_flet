import flet as ft


# tabelas dinâmicas
def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100
    page.scroll = ft.ScrollMode.AUTO

    def toggle_select(e):
        e.control.selected = not e.control.selected
        print(f"Selecionando a linha do índice {e.control.data}")
        e.control.update()


    dt = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("Nome")),
            ft.DataColumn(
                label=ft.Text("Login"), tooltip="Login do usuário na plataforma"
            ),
            ft.DataColumn(
                label=ft.Text("Idade"), 
                numeric=True,
                # dispara uma função de ordenação
                on_sort= lambda e: print(f'{e.column_index}, {e.ascending}'),
            ),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        content=ft.Text("Maria"),
                        # cria um ícone de editar  
                        show_edit_icon=True,
                        # dispara uma função toda vez que clicar na célula
                        on_tap= lambda _: print("cliquei"),
                    ),
                    ft.DataCell(content=ft.Text("mary99")),
                    ft.DataCell(content=ft.Text("43")),
                ],
                # serve para dizer se a linha já deve vir selecionada ou não por padrão
                selected=True,
                # dispara uma função cada vez que a seleção da linha mudar
                on_select_changed= toggle_select,
                data = 0,
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        content=ft.Text("João"),
                        # cria um ícone de editar  
                        show_edit_icon=True,
                        # dispara uma função toda vez que clicar na célula
                        on_tap= lambda _: print("cliquei"),
                    ),
                    ft.DataCell(content=ft.Text("jhony_pedro")),
                    ft.DataCell(content=ft.Text("19")),
                ],
                # serve para dizer se a linha já deve vir selecionada ou não por padrão
                selected=False,
                # dispara uma função cada vez que a seleção da linha mudar
                on_select_changed= toggle_select,
                data = 1,
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        content=ft.Text("luiz"),
                        # cria um ícone de editar  
                        show_edit_icon=True,
                        # dispara uma função toda vez que clicar na célula
                        on_tap= lambda _: print("cliquei"),
                    ),
                    ft.DataCell(content=ft.Text("ll2002")),
                    ft.DataCell(content=ft.Text("20")),
                ],
                # serve para dizer se a linha já deve vir selecionada ou não por padrão
                selected=False,
                # dispara uma função cada vez que a seleção da linha mudar
                on_select_changed= toggle_select,
                data = 2,
            )
        ],
        # só funciona se tiver o on_select_changed ativado na roll
        show_checkbox_column=True,
        bgcolor=ft.Colors.BLUE,
        border=ft.border.all(2),
        border_radius=ft.border_radius.all(10),
        # espaçamento entre colunas
        column_spacing=40,
        data_row_max_height=50,
        data_row_min_height=10,
        # define o estilo padrão a todos os dados da tabela
        data_text_style=ft.TextStyle(italic=True),
        # espessuara dalinha que divide as linhas
        divider_thickness=2,
        # ainda que tenha o bgcolor ativado o sistema só leva em consideração as cores do gradiente
        # personaliza as cores da tabela inteira
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=[ft.Colors.CYAN, ft.Colors.TEAL],
        ),
        data_row_color={
            ft.ControlState.SELECTED: ft.Colors.ORANGE,
            ft.ControlState.DEFAULT: ft.Colors.GREEN,
        },
        # cor da linha principal
        heading_row_color=ft.Colors.WHITE,
        heading_row_height=50,
        heading_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        horizontal_lines=ft.BorderSide(width=2,color=ft.Colors.BLACK),
        vertical_lines=ft.BorderSide(width=2, color=ft.Colors.BLACK),
        horizontal_margin=30,
        show_bottom_border=True,
        sort_column_index=2,
        sort_ascending=True,
    )

    page.add(dt)


if __name__ == "__main__":
    ft.app(target=main)
