import flet as ft


def main(page: ft.Page):
    page.window.always_on_top = True

    av1 = ft.CircleAvatar(
        foreground_image_src="https://picsum.photos/200/300",
        radius=50,
        tooltip="Avatar",
    )

    av2 = ft.CircleAvatar(
        # foreground_image_src="https://picsum.photos/200/300",
        radius=50,
        tooltip="Avatar_text",
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE,
        content=ft.Text(
            "A", size=70, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER
        ),
        min_radius=200,
        max_radius=100,
    )

    av3 = ft.CircleAvatar(
        foreground_image_src="https://picsum.photos/200/300",
        radius=50,
        tooltip="Avatar",
        badge=ft.Badge(
            small_size=20,
            large_size=100,
            bgcolor=ft.Colors.RED,
        ),
    )

    av4 = ft.CircleAvatar(
        foreground_image_src="images/teste.png",
        radius=50,
        tooltip="Avatar",
        background_image_src="/assets/images/teste.png",
        badge=ft.Badge(
            small_size=20,
            large_size=100,
            bgcolor=ft.Colors.RED,
        ),
    )

    page.add(av1, av2, av3, av4)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
