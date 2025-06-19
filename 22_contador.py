import flet as ft
import math

def main(page: ft.Page):
    page.title = "Contador"
    page.window.always_on_top = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    text_number = ft.Text(
        value="0", 
        text_align=ft.TextAlign.CENTER, 
        size=200)
    
    def minus_click(e, text):
        print(text)
        text_number.value = str(int(text_number.value or "0") - 1)
        text_number.update()
        
    def plus_click(e):
        text_number.value = str(int(text_number.value or "0") + 1)
        text_number.update()
    
    page.add(
            ft.Container(
                content=ft.Column(
                    horizontal_alignment= ft.CrossAxisAlignment.STRETCH,
                    controls=[
                        ft.Row(
                            expand= True,
                            controls=[
                                text_number,
                            ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                ft.IconButton(ft.Icons.REMOVE, on_click= lambda e: minus_click(e, 'teste'), icon_size=50, icon_color=ft.colors.BLACK),
                                ft.IconButton(ft.Icons.ADD, on_click=plus_click, icon_size=50, icon_color= ft.Colors.BLACK),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                expand = True,
                gradient= ft.LinearGradient(
                    begin= ft.alignment.top_center,
                    end= ft.alignment.bottom_center,
                    colors= [ft.Colors.BLUE_200, ft.Colors.AMBER_300, ft.Colors.PURPLE_200,],
                    stops= [0, 0.5, 1], # vai de 0 a 1
                    rotation= math.radians(70)
                ),
            )
                )

    page.update()
    
ft.app(target=main)