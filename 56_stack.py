import flet as ft


# serve para empilhar vários elementos do flet um acima do outro
# o primeiro elemento é o que estará ao fundo
def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100

    # assim como o container não tem largura, altura nem cor
    st = ft.Stack(
        controls=[
            # ft.Image(src="assets/images/img2.jpg"),
            ft.Container(
                image=ft.DecorationImage(
                    # o cover ocupa todo o espaço disponível no container
                    src="https://ciclovivo.com.br/wp-content/uploads/2018/10/iStock-536613027.jpg", fit= ft.ImageFit.COVER)
            ),
            # esse segundo container age como um filtro da imagem que está por traz
            ft.Container(
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=[ft.Colors.BLUE_GREY_100, ft.Colors.BLUE]
                ),
                opacity=0.8,
            ),
            ft.Text(value='Texto Sobreposto', style=ft.TextThemeStyle.HEADLINE_LARGE),
            # os elementos dentro dacolumn ainda estão na frente do elemento text só que na aplicação é mostrada abaixo por termos definido o top como 200
            ft.Column(
                # esses quatro so funcionar se o componente estiver dentro de uma stack
                top=200,
                left=50,
                right=0,
                bottom=0,
                controls=[
                    ft.Text(value='Curso de Jardinagem', style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    ft.Text(value='Aprenda como plantar flores lindas', style=ft.TextThemeStyle.HEADLINE_SMALL),
                    ft.FilledButton(text='Saiba mais')
                ]
            )
        ],
        # expand=True,
        # define o aspecto dessa stack - só funciona sem o expand - aqui a altura da stack deve ter no máximo 60% da app
        aspect_ratio=0.6,
    )

    page.add(st)


if __name__ == "__main__":
    ft.app(target=main)
