import flet as ft


def main(page: ft.Page):
    page.window.always_on_top = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK

        page.update()

    st = ft.Switch(
        active_color=ft.Colors.GREEN,
        active_track_color=ft.Colors.AMBER,
        inactive_thumb_color=ft.Colors.BLACK,
        inactive_track_color=ft.Colors.WHITE,
        label="Alterar tema",
        label_position=ft.LabelPosition.LEFT,
        # disabled=True,
        thumb_color={
            ft.ControlState.HOVERED: ft.Colors.GREEN,
            ft.ControlState.FOCUSED: ft.Colors.RED,
            ft.ControlState.DEFAULT: ft.Colors.BLUE,
        },
        thumb_icon={
            ft.ControlState.SELECTED: ft.Icons.DARK_MODE,
            ft.ControlState.DISABLED: ft.Icons.CLOSE,
            ft.ControlState.DEFAULT: ft.Icons.LIGHT_MODE,
        },
        track_color={
            ft.ControlState.HOVERED: ft.Colors.RED,
            ft.ControlState.FOCUSED: ft.Colors.AMBER,
            ft.ControlState.DEFAULT: ft.Colors.WHITE,
        },
        # value=True, # se quiser que ele já inicie habilidado
        on_change= change_theme # vai ser disparada a cada clique
        )
    page.add(st)


if __name__ == "__main__":
    ft.app(target=main)