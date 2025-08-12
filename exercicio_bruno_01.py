""" 
Desafio Flet com 3 exercícios simples!

Crie um app simples usando o Framework Flet (Python) para treinar os seguintes conceitos:

---

✅ *Exercício 1*

Crie um app que leia o ano de nascimento do usuário 
e exiba quantos anos ele terá em 2035.
"""
import flet as ft

def main(page: ft.Page):
    def calcular_idade(e):
        valor = campo_ano.value

        if valor and valor.isdigit():
            ano_nascimento = int(valor)
            idade_em_2035 = 2035 - ano_nascimento
            resultado.value = f"Em 2035 você terá {idade_em_2035} anos."
        else:
            resultado.value = "Por favor, digite um ano válido."

        page.update()

    campo_ano = ft.TextField(
        label="Ano de nascimento",
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    
    botao = ft.ElevatedButton("Calcular", on_click=calcular_idade)
    
    resultado = ft.Text()

    page.add(campo_ano, botao, resultado)

ft.app(target=main)

