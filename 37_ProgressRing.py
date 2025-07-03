import flet as ft
import time

def main(page: ft.Page):
    page.window.always_on_top = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    pg1 = ft.ProgressRing(
        value=0.2,
        bgcolor=ft.Colors.GREY_200,
        color=ft.Colors.GREEN,
        stroke_width=5,
        tooltip="Carregando...",
    )
    
    pg2 = ft.ProgressRing()

    page.add(pg1, pg2)
    
    for i in range(100):
        if pg1.value is not None:
            pg1.value += 0.01
            time.sleep(0.2)
            page.update(pg1)

if __name__ == "__main__":
    ft.app(target=main)
