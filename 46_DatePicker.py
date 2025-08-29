import flet as ft
import datetime

def main(page: ft.Page):
    page.window.always_on_top = True
    page.padding = ft.padding.all(10)
    page.bgcolor = ft.Colors.BLUE_GREY_100

        
    dp = ft.DatePicker(
                    cancel_text='Cancelar',
                    confirm_text='Confirmar',
                    error_format_text='Data inválida',
                    field_hint_text='MM/DD/YYYY',
                    field_label_text= 'Digite uma data',
                    help_text='Selecione uma data no calendário',      
                    first_date=datetime.datetime(year=2000, month=10, day=1),
                    last_date=datetime.datetime(year=2025, month=12, day=10),
                    switch_to_calendar_icon=ft.Icons.CALENDAR_MONTH,
                    switch_to_input_icon=ft.Icons.EDIT,
                    date_picker_mode=ft.DatePickerMode.DAY,
                        # year - ao invesde aparecer o calendário com os dias aparece com os anos
                    date_picker_entry_mode=ft.DatePickerEntryMode.CALENDAR,
                    value= datetime.date(2025,1,5),
                    error_invalid_text='Data fora do lmite',
                    on_change=lambda _: print(dp.value),
                    # para dispositivos móveis - usa na parte onde edita a data 
                    keyboard_type=ft.KeyboardType.DATETIME,
                )
    
    
    btn = ft.ElevatedButton(
            "Pick date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(dp),
    
        )
    
    page.overlay.append(dp)
    page.add(btn)

if __name__ == "__main__":
    ft.app(target=main)