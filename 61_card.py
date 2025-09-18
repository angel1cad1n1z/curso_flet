import flet as ft

def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100
    page.scroll = ft.ScrollMode.AUTO
    
    card = ft.Card(
        content=ft.Column(
            controls=[
                ft.Text(
                    value="Título do card",
                    style=ft.TextThemeStyle.HEADLINE_MEDIUM
                ),
                ft.Text(
                    value="Conteúdo do card",
                    style=ft.TextThemeStyle.HEADLINE_SMALL
                ),
                ft.FilledButton(
                    text="Salvar",
                )
            ]
        ),
        color=ft.Colors.BLUE_100,
        # sombreamento lateral - dá a impressão de que o card está elevado
        elevation=5,
        margin=ft.margin.all(10),
        # cor da sombra
        shadow_color=ft.Colors.BLUE,
    )
    
    page.add(card)

if __name__ == "__main__":
    ft.app(target=main)