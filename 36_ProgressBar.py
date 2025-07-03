import flet as ft
import time

# cria barra de progresso
# estado padrão: rolagem infinita


def main(page: ft.Page):
    page.window.always_on_top = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    pg1 = ft.ProgressBar(
        value=0.3,
        bar_height=50,
        bgcolor=ft.Colors.GREY_200,
        color=ft.Colors.GREEN,
        tooltip="Progresso",
    )

    pg2 = ft.ProgressBar(
        bar_height=50,
    )

    page.add(pg1, pg2)

    for i in range(10):
        if pg1.value is not None:
            pg1.value += 0.1
            time.sleep(1)  # incrementa de 1 em 1 segundo
            page.update(pg1)
        else:
            pg1.value = 0.1
            time.sleep(1)  # incrementa de 1 em 1 segundo
            page.update(pg1)


if __name__ == "__main__":
    ft.app(target=main)
