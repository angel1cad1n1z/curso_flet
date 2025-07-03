import flet as ft
import time


def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = 0
    page.title = "Markdown Editor"

    def update_view(e):
        view.value = editor.value
        view.update()

    editor = ft.TextField(
        multiline=True,
        min_lines=30,
        max_lines=30,   
        content_padding=ft.padding.all(10),
        border=ft.InputBorder.NONE,
        bgcolor=ft.Colors.BLUE_GREY,
        on_change=update_view,
    )

    how_to = ft.Container(
        expand=True,
        content=ft.Column(
            scroll=ft.ScrollMode.ALWAYS,
            controls=[
                ft.Text(
                    value="Para criar títulos em diferentes tamanhos",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK,
                ),
                ft.Text(value="# H1", color=ft.Colors.GREY_700),
                ft.Text(value="## H2", color=ft.Colors.GREY_700),
                ft.Text(value="### H3", color=ft.Colors.GREY_700),
                ft.Divider(color=ft.Colors.GREY, height=40),
                ft.Text(
                    value="Para formatar o estilo do texto",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK,
                ),
                ft.Text(value="**Texto em negrito**", color=ft.Colors.GREY_700),
                ft.Text(value="*Texto em itálico*", color=ft.Colors.GREY_700),
                ft.Text(value="~Texto tachado~", color=ft.Colors.GREY_700),
                ft.Divider(color=ft.Colors.GREY, height=40),
                ft.Text(
                    value="Para criar listas",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK,
                ),
                ft.Text(value="1. Ordenada", color=ft.Colors.GREY_700),
                ft.Text(value="- Não ordenada", color=ft.Colors.GREY_700),
                ft.Divider(color=ft.Colors.GREY, height=40),
                ft.Text(
                    value="Para inserir links e imagens",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK,
                ),
                ft.Text(
                    value="[texto do link](https://google.com.br)",
                    color=ft.Colors.GREY_700,
                ),
                ft.Text(value="[Label da imagem](https://picsum.photos/200/300)", color=ft.Colors.GREY_700),
                ft.Divider(color=ft.Colors.GREY, height=40),
                ft.Text(
                    value="Para inserir código",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK,
                ),
                ft.Text(
                    value="`print('Olá mundo!')`",
                    color=ft.Colors.GREY_700,
                ),
                ft.Text(value="```print('Olá mundo!') - código com várias linhas```", color=ft.Colors.GREY_700),
                ft.Divider(color=ft.Colors.GREY, height=40),
            ],
        ),
        bgcolor=ft.Colors.GREY_200,
        padding=ft.padding.all(10),
        alignment=ft.alignment.center,
    )

    view = ft.Markdown(
        value=editor.value,
        selectable=True,
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        code_theme=ft.MarkdownCodeTheme.GITHUB,
        on_tap_link=lambda e: page.launch_url(e.data) if e.data else None,
    )

    layout = ft.Row(
        expand=True,
        spacing=0,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[
            ft.Container(
                expand=True,
                bgcolor=ft.Colors.WHITE,
                content=ft.Column(
                    controls=[
                        editor,
                        how_to,
                    ]
                ),
            ),
            ft.Container(
                expand=True,
                bgcolor=ft.Colors.GREY,
                padding=ft.padding.all(10),
                content=view,
            ),
        ],
    )

    page.add(layout)


if __name__ == "__main__":
    ft.app(target=main)
