import flet as ft

def main(page: ft.Page):
    page.window.always_on_top = True
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    dd = ft.Dropdown(
        label='Selecione uma opção',
        options=[
            ft.dropdown.Option(key="1", text="Opção 01"),
            ft.dropdown.Option(key="2", text="Opção 02"),
            ft.dropdown.Option(key="3", text="Opção 03"),
            ft.dropdown.Option(key="4", text="Opção 04"),
            ft.dropdown.Option(key="5", text="Opção 05", disabled= True),
        ],
        value="1",
        filled=True, # Coloca um background do dropdown de acordo com a cor do tema da app
        bgcolor=ft.Colors.WHITE,
        border=ft.InputBorder.UNDERLINE,
        border_color=ft.Colors.ORANGE,
        border_width=5,
        border_radius=ft.border_radius.all(10),
        expand=True,
        width= 500,
        color=ft.Colors.ORANGE,
        content_padding= 5,
        alignment=ft.alignment.center_left,
    )

    page.add(dd)


if __name__ == "__main__":
    ft.app(target=main)