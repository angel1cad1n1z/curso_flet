import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    # é um botão disparador
    # quando clicamos ele dispara uma ação como exibir um menu suspenso na tela
    # ele tem um parâmetro - item - que é uma lista e cada elemento dessa lista é um item que vai ser exibido no app
    
    def checked_item_clicked(e):
        e.control.checked= not e.control.checked
        e.control.update()
    
    pb = ft.PopupMenuButton(
        icon= ft.Icons.MENU,
        items= [
            ft.PopupMenuItem(
                text="Item I",
            ),
            ft.PopupMenuItem(
                text="Item I",
                icon=ft.Icons.HELP
            ),
            ft.PopupMenuItem(
                content= ft.Row(
                    controls=[
                        ft.Icon(ft.Icons.NOTIFICATION_IMPORTANT),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    value="Dalton gostaria de enviar uma mensagem",
                                    theme_style= ft.TextThemeStyle.BODY_LARGE,
                                    max_lines=1,
                                    overflow=ft.TextOverflow.ELLIPSIS
                                ),
                                ft.Text(
                                    value="Olá, tudo bem? Você está curtindo aprender flet conosco? Deixe sua opnião no nosso forúm",
                                    theme_style= ft.TextThemeStyle.BODY_LARGE,
                                    max_lines=2,
                                    overflow=ft.TextOverflow.ELLIPSIS
                                    ),
                            ],
                            width= 200,
                        ),
                    ],
                ),
                on_click= lambda e: print("fui clicado!"),
            ),
            ft.PopupMenuItem(),
            ft.PopupMenuItem(
                text="Item III",
                checked= False,
                on_click= checked_item_clicked,
            ),
        ],
    )
    page.add(pb)
    
ft.app(target=main)