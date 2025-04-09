import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    btn1 = ft.FilledTonalButton(text= "Clique aqui")
    
    page.add(btn1)
    page.add(
        ft.FilledTonalButton(
            text="Botão desabilitado",
            disabled= True),
        ft.FilledTonalButton(
            text="Botão com ícone",
            icon= ft.Icons.ADD),
        ft.FilledTonalButton(
            text="Botão com ícone de outra cor",
            icon= ft.Icons.ADD,
            icon_color= ft.Colors.AMBER),
        ft.FilledTonalButton(
            text="Botão com tooltip",
            tooltip="Ação não permitada",
            disabled= True),
        ft.FilledTonalButton(
            text="Botão com estilo",
            style= ft.ButtonStyle(
                shape= ft.RoundedRectangleBorder(radius=0)
            )
        ),
    )

ft.app(target=main)