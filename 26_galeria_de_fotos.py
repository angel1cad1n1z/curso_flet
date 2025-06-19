import flet as ft


def image(num: int):
    return ft.Image(
        src=f"https://picsum.photos/200/300?{num}",
        width=150,
        height=200,
        fit=ft.ImageFit.COVER,
        repeat=ft.ImageRepeat.NO_REPEAT,
        border_radius=15,
    )


def main(page: ft.Page):
    page.title = "Galeria de Fotos"
    page.window.always_on_top = True
    page.padding = 0
    page.auto_scroll = True

    def change_view(e):
        btn1.style = btn_style
        btn2.style = btn_style
        e.control.style = btn_style_selected
        # btn1.update()
        # btn2.update()
        
        if e.control.text == 'Agrupadas':
            layout.controls[0] = grid2
        else:
            layout.controls[0] = grid1
            
        layout.update()
        
        
        
    # o gridView é responsivo!
    grid1 = ft.GridView(
        controls=[
            image(num)
            for num in range(
                100
            )  # como estamos dentro de uma lista, podemos usar o range para gerar as imagens
        ],
        expand=True,  # expandir para o tamanho da tela
        # runs_count=2, # quantas elementod aparecem por linha
        max_extent=200,  # tamanho máximo da imagem em px, ignora o runs_count
        child_aspect_ratio=1.0,  # proporção da imagem
        spacing=5,
        run_spacing=5,
    )

    grid2 = ft.Column(
        expand=True,
        controls=[
            ft.Text(value="2023", size=30),
            ft.GridView(
                controls=[image(num) for num in range(1, 4)],
                # runs_count=4,
                max_extent=200,
                child_aspect_ratio=1.0,  # proporção da imagem
                spacing=5,
                run_spacing=5,
            ),
            ft.Text(value="2024", size=30),
            ft.GridView(
                controls=[image(num) for num in range(10, 15)],
                max_extent=200,
                child_aspect_ratio=1.0,  # proporção da imagem
                spacing=5,
                run_spacing=5,
            ),
            ft.Text(value="2025", size=30),
            ft.GridView(
                controls=[image(num) for num in range(16, 20)],
                max_extent=200,
                child_aspect_ratio=1.0,  # proporção da imagem
                spacing=5,
                run_spacing=5,
            ),
        ],
    )

    btn_style = ft.ButtonStyle(
        bgcolor=ft.Colors.TRANSPARENT,
        color=ft.Colors.PINK,
        elevation=0,
        overlay_color=ft.Colors.ORANGE_200,
    )
    btn_style_selected = ft.ButtonStyle(
        bgcolor=ft.Colors.PINK,
        color=ft.Colors.WHITE,
        elevation=0,
        overlay_color=ft.colors.ORANGE_200,
    )

    footer = ft.Container(
        margin=ft.margin.symmetric(vertical=5, horizontal=10),
        padding=ft.padding.all(5),
        bgcolor=ft.Colors.BLACK87,
        border_radius=20,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                btn1 := ft.ElevatedButton(text="Todas as Fotos", style=btn_style_selected, on_click=change_view),
                btn2 := ft.ElevatedButton(text="Agrupadas", style=btn_style, on_click=change_view),
            ],
            tight=True,
        ),
    )

    layout = ft.Column(
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            grid1,
            footer,
        ],
    )
    page.add(layout)

    page.update()


if __name__ == "__main__":
    ft.app(target=main)
