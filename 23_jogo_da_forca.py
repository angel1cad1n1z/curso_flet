import flet as ft
import string
import random


# cria e retorna um Container que representa uma letra da palavra oculta no jogo
# seja um sublinhado ("_") no início ou uma letra revelada após o acerto.
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

    # Palavras disponíveis
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
    # Palavra sorteada
    choiced = random.choice(avaible_words).upper()

    # Contador de erros
    errors = 0

    # Diálogo de derrota
    dialog = ft.AlertDialog(title=ft.Text("Que pena! Você perdeu!"), open=False)
    page.overlay.append(dialog)

    # Função para validar a letra inserida pelo usuário
    def validate_letter(e):
        nonlocal errors
        guessed_letter = e.control.content.value
        # 'e' é o evento de clique;
        # 'e.control' é o botão clicado
        # 'e.control.content.value' é a letra visível nele
        if guessed_letter in choiced:
            # Verifica se a letra escolhida está **na palavra sorteada** (ex: "MARIO").
            for pos, letter in enumerate(choiced):
                # Percorre a palavra (choiced), letra por letra.
                if letter == guessed_letter:
                    word.controls[pos] = letter_to_guess(letter)
            word.update()
        else:
            # se errar aumenta o contador de erros
            errors += 1

            if errors >= 6:
                # se passar de 6 erros aparece o 'você perdeu!' na tela
                dialog.open = True
                page.update()
            else:
                # se ainda tiver chances troca a imagem do boneco da forca para mostrar a próxima parte do corpo
                victim.src = f"images/hangman_{errors}.png"
                victim.update()

    # Imagem inicial do boneco da forca
    victim = ft.Image(
        # data=0,
        src="images/hangman_0.png",
        repeat=ft.ImageRepeat.NO_REPEAT,
        height=300,
    )

    # Palavra oculta - vai conter as letras da palavra da forca
    word = ft.Row(
        # Cria uma lista de caixinhas com '_' para cada letra da palavra sorteada
        controls=[letter_to_guess("_") for _ in choiced]
    )

    # Montagem da área do jogo
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

    # Teclado virtual
    keyboard = ft.Container(
        col={"xs": 12, "lg": 6},
        image=ft.DecorationImage(
            src="images/keyboard.png",
            repeat=ft.ImageRepeat.NO_REPEAT,
            fit=ft.ImageFit.FILL,
        ),
        padding=ft.padding.only(top=150, left=80, right=80, bottom=50),
        content=ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    height=50,
                    width=50,
                    border_radius=ft.border_radius.all(5),
                    content=ft.Text(
                        value=letter,
                        color=ft.Colors.WHITE,
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                    ),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.Colors.AMBER, ft.Colors.DEEP_ORANGE],
                    ),
                    on_click=validate_letter,
                )
                for letter in string.ascii_uppercase
            ],
        ),
    )

    # Imagem de fundo da cena
    scene = ft.Image(col=12, src="images/scene.png")

    # Layout final responsivo
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            scene,
            game,
            keyboard,
            scene,
        ],
    )

    # Adiciona o layout à página
    page.add(layout)
    page.update()


# Executa o app informando a pasta "assets"
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
