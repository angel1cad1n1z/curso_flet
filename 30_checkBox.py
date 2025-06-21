import flet as ft

def main(page: ft.Page):
    page.window.always_on_top = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    cb = ft.Checkbox(
        label="Selecione aqui:",
        label_position=ft.LabelPosition.LEFT,
        check_color=ft.Colors.AMBER,
        fill_color={
            ft.ControlState.HOVERED: ft.Colors.ORANGE,
            ft.ControlState.FOCUSED: ft.Colors.BLUE,
            ft.ControlState.DEFAULT: ft.Colors.BLACK,
        },
        # tristate=True, # pode ter três estados diferentes - sesabilitado, intermediário e habilitado
        # value=True, #se o tristate não tiver habilitado pode deixar já o checbox marcado por default
        on_change= lambda _: print("O valor é", cb.value),
    )
    page.add(cb)


if __name__ == "__main__":
    ft.app(target=main)