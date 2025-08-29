import flet as ft
import datetime


def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100

    tp = ft.TimePicker(
        cancel_text="Cancelar",
        confirm_text="Confirmar",
        error_invalid_text="Hora Inválida",
        hour_label_text="Hora",
        minute_label_text="Minutos",
        help_text="Selecione a hora",
        time_picker_entry_mode=ft.TimePickerEntryMode.DIAL,
        value=datetime.time(10, 31, 18),
        on_change=lambda _: print(tp.value),
    )

    page.overlay.append(tp)

    bt = ft.ElevatedButton("Abrir", on_click=lambda _: page.open(tp))

    page.add(bt)


if __name__ == "__main__":
    ft.app(target=main)
