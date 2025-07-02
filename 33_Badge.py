import flet as ft

def main(page: ft.Page):
    page.window.always_on_top = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # é o pontinho que fica acima do ícone quando chega alguma notificação
    icon = ft.Icon(
        name=ft.Icons.NOTIFICATIONS,
        size=150,
        badge=ft.Badge(
            small_size=10, 
            bgcolor=ft.Colors.RED,
            label_visible=True,
            alignment=ft.alignment.top_right,
            text="10",
            text_color=ft.Colors.WHITE,
            text_style=ft.TextStyle(size=40, weight=ft.FontWeight.BOLD),
            padding=ft.padding.symmetric(vertical=10, horizontal=10),
            ),
    )

    page.add(icon)


if __name__ == "__main__":
    ft.app(target=main)