import flet as ft
from decimal import Decimal

# lista de botões dacalculadora
botoes = [
    {"operador": "AC", "fonte": ft.Colors.BLACK, "fundo": ft.Colors.BLUE_GREY_100},
    {"operador": "±", "fonte": ft.Colors.BLACK, "fundo": ft.Colors.BLUE_GREY_100},
    {"operador": "%", "fonte": ft.Colors.BLACK, "fundo": ft.Colors.BLUE_GREY_100},
    {"operador": "/", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.ORANGE},
    {"operador": "1", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.WHITE24},
    {"operador": "2", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.WHITE24},
    {"operador": "3", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.WHITE24},
    {"operador": "*", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.ORANGE},
    {"operador": "4", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.WHITE24},
    {"operador": "5", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.WHITE24},
    {"operador": "6", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.WHITE24},
    {"operador": "-", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.ORANGE},
    {"operador": "7", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.WHITE24},
    {"operador": "8", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.WHITE24},
    {"operador": "9", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.WHITE24},
    {"operador": "+", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.ORANGE},
    {"operador": "0", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.WHITE24},
    {"operador": ".", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.WHITE24},
    {"operador": "=", "fonte": ft.Colors.WHITE, "fundo": ft.Colors.ORANGE},
]


def main(page: ft.Page):
    page.window.always_on_top = True
    page.bgcolor = "#000"
    # page.window.resizable = False - #Não permite que o usuário redimensione a tela da aplicação
    # tamanho da tela:
    page.window.width = 250
    page.window.height = 380
    # título da página:
    page.title = "Calculadora"

    # a função calculate espera dois parâmetros: o operador e o valor atual
    def calculate(operator, value_at):
        # ele vai tentar fazer a operação abaixo
        try:
            # o eval() faz o cálculo de qualquer valor que passar como parâmetro, mesmo que seja uma string - ele interpreta como uma operação aritimética 7*7
            value = eval(value_at)

            # se for % o valor vai ser igual a ele mesmo dividido por 100
            if operator == "%":
                value /= 100
            
            # se for ± vai pegar o value e inverter seu valor
            elif operator == "±":
                value = -value
        
            value = Decimal(str(value))
            
            # Se for um número inteiro, remove o ".0"
            # o to.integral() é um método da classe Decimal()e serve para retornar apenas a parte inteira do número, sem arredondar
            if value == value.to_integral():
                return str(int(value))
            else:
                # se não limita o valor para 5 casas decimais e remove zeros à direita
                # value.quantize(Decimal("1.00000")): força o número a ter no máximo 5 casas decimais.
                # normalize(): remove zeros desnecessários no final (ex: 3.50000 → 3.5).
                return format(value.quantize(Decimal("1.00000")).normalize())
        
        # se der errado vai retornar "Error"
        except:
            return "Error"

        # digits = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value)

    # a função select vai recber um evento
    """
    Resumo da função select
    
        Quando gitamos um valor na calculadora, a função vai primiero verificar se o valor é diferente de 0, se sim ele vai retornar o valor se não vai retornar uma string vazia, porque como vamos concatenar o valor atual + o valor digitado não é para aparecer 07, por exemplo, dessa forma quando digitar um valor, 7 por exemplo fica somente este. 
        Depois a função vai verificar se o valor digitado é um número, se sim ele vai concatenar o valor atual + o valor digitado. Ou seja, temos o número 7, se digitarmos um 8, ele vai concatenar e ficar 78.
        Se digitarmos AC a função vai zerar o resultado.
        Se não digitarmos nem um dígito, nem um AC, a função vai verificar se o valor digitado -1 é um dos sinais de operação "/", "*", "-", "+", "." e se quiser alterar o sinal também é possível graças ao [:-1] que significa tudo que vem da variavel anterior -1.
        exemplo:
            se tivermos um 7+ e quizermos alterar para 7* é só clicar no * para substituir o sinal anterior.
        Digitamos mais um número,agora temos 7*7 e se o próximo valor digitado for um desses sinais "=", "%", "±" a função vai chamar a função calculate para fazero cálculo da operação
    """
    def select(e):
        # vai armazenar o valor exibido na calculadora
        # se for 0 ou error ele limpa será uma string vazia para não ser concatenado com nada quando digitar uma outra vez
        value_at = result.value if result.value not in ("0", "Error") else ""
        value = e.control.content.value
            # control aqui é todo o conatainer de btn
            # control.content é o conteúdo de content
            # control.content.value é o valor que está guardado em value dentro de content

        # verifica se value é um numero
        if value.isdigit():
            # se sim soma o valor atual com o valor digitado
            value = value_at + value
        elif value == "AC":
            # se não limpa o valor, zera o resultado
            value = "0"
        else:
            # se o valor for qualquer um desses sinais
            if value_at and value_at[-1] in ("/", "*", "-", "+", "."):
                # o valor atual vai ser iguala ele mesmo menos o último elemento digitado
                value_at = value_at[:-1]

            # concatenamos novamente o valor atual mais o valor digitado
            value = value_at + value

            # se ele for um desses sinais
            if value[-1] in ("=", "%", "±"):
                # o operador vai ser o último valor digitado que será um dos operadores matemáticos e o valor atual será o valor atual que estará sendo exibido no resultado
                value = calculate(operator=value[-1], value_at=value_at)

        # 
        result.value = value
        # atualiza o result
        result.update()

    result = ft.Text(value="0", color=ft.Colors.WHITE, size=20)

    # fazemos de btn uma lista que vai iterar sobre a lista de botões para criar todos os botões que a calculadora precisa

    btn = [
        ft.Container(
            # aqui o value vai ser o operador e a cor vai ser a fonte la dalista de botões
            content=ft.Text(value=btn["operador"], color=btn["fonte"]),
            alignment=ft.alignment.center,
            width=50,
            height=50,
            # a cor do fundo tbm vai ser o fundo lá da lista de botões
            bgcolor=btn["fundo"],
            border_radius=100,
            # quando o botão for clicado vai chamar a função select
            on_click=select,
            # para cada elemento da lista de botões vamos criar um novo container
        )
        for btn in botoes
    ]

    # como não pe possível  adicionar uma lista direta para a página criamos o keyboard como uma row que vai receber  a lista de conatainers de btn
    keyboard = ft.Row(
        width=250,
        # como é uma row aqui o wrap é necessário para que os elementos quando chegarem no tamanho que definimos antes eles se alocam abaixo
        wrap=True,
        controls=btn,
        alignment=ft.MainAxisAlignment.END,
    )

    display = ft.Row(
        width=250,
        controls=[result],
        alignment=ft.MainAxisAlignment.END,
    )

    page.add(display)
    page.add(keyboard)


if __name__ == "__main__":
    ft.app(target=main)
