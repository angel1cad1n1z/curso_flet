import flet as ft

def main(page: ft.Page):
    page.window.always_on_top = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    s1 = ft.Slider(
        active_color=ft.Colors.AMBER,
        inactive_color=ft.Colors.GREY,
        thumb_color=ft.Colors.BLACK,
        divisions=12, # coloca pontinhos e quando arrastar a bolinha vai de pontinho em pontinho
        label='{value}',
        min=0,
        max=100,
        round=2, # caso queira um número flutuante usa o round para definir quantas casas decimais serão necessárias - Caso não utilize o sistema arredonda o valor p cima
        value=10,
        on_change=lambda _: print("Selecionado", s1.value),
    )
    page.add(s1)


if __name__ == "__main__":
    ft.app(target=main)