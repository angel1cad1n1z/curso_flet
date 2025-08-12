import flet as ft


def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100

    def acao(e):
        if e.control.text == "Sim":
            page.window.destroy()

        ad1.open = False
        page.update()

    ad1 = ft.AlertDialog(
        title=ft.Text(value="Atenção"), 
        content=ft.Text(value="Desejs sair do aplicativo?"),

        # espaçamento das bordas para o texto  
        content_padding=ft.padding.all(30),
        
        # espaçamento de fora (página)
        inset_padding=ft.padding.all(10), 
        
        # False fecha quando clicar fora do componente, True  não fecha.
        modal=False,
        
        # define como são as bordas. 0 = quadrado
        shape=ft.RoundedRectangleBorder(
            radius=20
        ),
        
        # função quando fecha o alerta ou clica botão.
        on_dismiss=lambda e: acao,  
        actions=[
            ft.TextButton(
                text="Não", style=ft.ButtonStyle(color=ft.Colors.RED), on_click=acao
            ),
            ft.ElevatedButton(
                text="Sim",
                style=ft.ButtonStyle(bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
                on_click=acao,
            ),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def open_ad(e):
        page.overlay.append(ad1)
        ad1.open = True
        page.update()

    btn1 = ft.ElevatedButton(
        text="Sair",
        on_click=open_ad,
    )

    page.add(btn1)


ft.app(target=main)
