import flet as ft

def main(page: ft.Page):
    page.window.always_on_top= True
    page.spacing = 80
    
    theme = ft.Theme(
        color_scheme= ft.ColorScheme(
            primary= ft.Colors.PINK,
        ),
        text_theme= ft.TextTheme(
            title_large= ft.TextStyle(
                size= 50,
                weight= ft.FontWeight.W_500
            ),
        )
    )
    page.add(
        ft.Container(
            height= 100,
            width= 200,
            padding= 10,
            content= ft.Column(
                controls= [
                    ft.Text(
                        value="Título",
                        style= ft.TextThemeStyle.TITLE_LARGE,
                    ),
                    ft.ElevatedButton(
                        text= "Botão", color= ft.Colors.AMBER,
                    ),
                    ft.FilledButton(
                        text='Botão Primário'
                    )
                ]
            ),
            bgcolor= ft.Colors.PRIMARY,
            theme= theme,
        ),
        ft.Container(
            height= 90,
            width= 200,
            padding= 10,
            content= ft.Column(
                controls= [
                    ft.Text(
                        value="Título",
                        style= ft.TextThemeStyle.TITLE_LARGE,
                    ),
                    ft.ElevatedButton(
                        text= "Botão", color= ft.Colors.AMBER,
                    ),
                    ft.FilledButton(
                        text='Botão Primário'
                    )
                ]
            ),
            bgcolor= ft.Colors.PRIMARY,
            theme= theme,
        )
    )

    page.theme_mode = ft.ThemeMode.LIGHT # deixa a aplicação sempre no modo ligth ainda que no sistema esteja configurado como dark
    
    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
    
    
        page.update()
    
    page.floating_action_button = ft.FloatingActionButton(
        icon= ft.icons.CHANGE_CIRCLE,
        on_click= change_theme
    )
    
    page.update()

ft.app(main)