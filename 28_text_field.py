import flet as ft


def main(page: ft.Page):
    page.title = "TextField"
    page.window.always_on_top = True
    page.bgcolor = ft.Colors.ORANGE
    page.padding = ft.padding.symmetric(vertical=100, horizontal=20)
    text = ft.Container(
        content=ft.Text(
            value="LOGIN",
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD,
            size=20,
        ),
        alignment=ft.alignment.center,
        padding=20,
    )
    tf = ft.TextField(
        label="E-mail",
        label_style=ft.TextStyle(weight=ft.FontWeight.BOLD,color=ft.Colors.WHITE),
        text_align=ft.TextAlign.JUSTIFY,
        text_size=15,
        text_style=ft.TextStyle(weight=ft.FontWeight.BOLD),
        # value='Conteúdo pré-preenchido',
        bgcolor=ft.Colors.TRANSPARENT,
        border=ft.InputBorder.OUTLINE,
        border_color=ft.Colors.WHITE,
        border_radius=ft.border_radius.all(10),
        border_width=2,
        color=ft.Colors.BLUE_200,
        content_padding=ft.padding.all(20),
        counter_text='Senha forte/ Senha Fraca',
        counter_style=ft.TextStyle(size=15, italic=True),
        cursor_color=ft.Colors.WHITE,
        cursor_height=30,
        cursor_radius=10,
        cursor_width=5,
        dense=True, #É utilizado quando temos muitos textfields na página, assim ele faz com que o componente ocupe um pouco menos de espaço na tela da app. - Por padrão vem como falso.
        # capitalization=ft.TextCapitalization.WORDS, 
            #   # words: cada palavra escrita fica com a primeira letra maisuscula - 
            # setences: a primeira letra de todo o texto fica maiuscula - 
            # characteres: todas as letras maiusculas
        # error_text='Valor inválido', #Muito utilizado em funções para destacar erros de digitação. Ex: no campo de e-mail se o usuário digitar algo diferente do que se espera.
        # error_style=ft.TextStyle(size=15),
        helper_text='Seu melhor e-mail', #aparece no mesmo lugar do error_text
        helper_style=ft.TextStyle(size=15, italic=True),
        hint_text='eu@mail.com',
        hint_style=ft.TextStyle(size=15, italic=True),
        filled=True, # se tiver utilizando um tema ao habilitar o filled as cores automaticamente se alteram para o tema da app
        focused_bgcolor=ft.Colors.TRANSPARENT,
        focused_border_color= ft.Colors.BLACK,
        focused_border_width=1,
        focused_color= ft.Colors.BLACK,
        icon=ft.Icons.EMAIL,
        # input_filter=ft.InputFilter(
        #     allow=False, # digita qualquer coisa exceto números de 0 a 9 - se tiver true digita apenas números de 0 a 9
        #     regex_string=r"[0-9]",
        #     replacement_string='-',
        # )
        # input_filter=ft.NumbersOnlyInputFilter(), #perminte apenas números
        input_filter=ft.TextOnlyInputFilter(), #permite apenas texto
        # keyboard_type=ft.KeyboardType.DATETIME, # Altera o tipo de tecaldo - usado em app mobile. Ex: campo de telefone, aparece apenas o teclado numérico. - email: aparece o teclado completo visto que tbm podem ser utilizados caracteres especiais
            # number: aparece apenas o teclado numérico
        max_length=50, #comprimento máximo que o textfield terá
        # max_lines=5, #máximo de linhas
        # min_lines=1, # mínimo de linhas - vem com 1 linha por padrão
        # multiline=True, # quando o usuário quiserpular para a linha de baixo clica no enter e a app permite que ele continue digitando na linha de baixo
        # password=True, # por padrão vem definido com false - tipo de senha, esconde o texto 
        # can_reveal_password=True, # cria um ícone de olho - por padrão vem como falso
        # prefix_text='https//',
        # prefix_icon=ft.Icons.LINK,
        # prefix_style=ft.TextStyle(size=15),
        # suffix_text='.com',
        # suffix_icon=ft.Icons.ABC,
        # suffix_style=ft.TextStyle(size=15),
        # read_only=True, # útil para campos onde os dados do usuário estão salvos no banco e não é permitido alterá-los
        on_change= lambda x: print(x.data), # geralmente usado para validações - validar email, senha, etc
    )

    page.add(text, tf)


if __name__ == "__main__":
    ft.app(target=main)
