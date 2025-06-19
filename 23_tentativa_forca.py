import flet as ft
import string
import random

def letter_to_guess(letter):
    return ft.Container(
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.AMBER,
        height=50,
        width=50,
        border_radius=ft.border_radius.all(5),
        content=ft.Text(
            value=letter,
            color=ft.Colors.WHITE,
            size=30,
            text_align=ft.TextAlign.CENTER,  # Centraliza o texto na horizontal
            weight=ft.FontWeight.BOLD,  # Deixa o texto em negrito
        ),
    )
    
def main(page: ft.Page):
    page.title = "Jogo da Forca"
    page.window.always_on_top = True
    page.bgcolor = ft.Colors.WHITE
    
    avaible_words = [
        "Cogumelo",
        "Flor",
        "Estrela",
        "Luigi",
        "Peach",
        "Bowser",
        "Toad",
        "Mario",
        "Princesa",
    ]
    
    choiced = random.choice(avaible_words).upper()

    scene = ft.Image(col=12, src="assets/images/scene.png")

    victim = ft.Image(
        src="images/hangman_0.png",
        repeat=ft.ImageRepeat.NO_REPEAT,
        height=300,
    )
    word = ft.Row(
        controls=[letter_to_guess("_") for _ in choiced]
    )

    game = ft.Container(
        col={"xs": 12, "lg": 6},
        padding=ft.padding.all(50),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                victim,
                word,
            ],
        ),
    )

    keyboard = ft.Container()

    layout = ft.ResponsiveRow(controls=[scene, game, keyboard, scene])
    page.add(layout)
    # page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
