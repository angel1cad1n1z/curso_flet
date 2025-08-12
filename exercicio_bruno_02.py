""" 
✅ *Exercício 2*

```Crie um app que leia um número digitado 
e mostre o antecessor e o sucessor dele.```
"""
import flet as ft

def main(page: ft.Page):
    def mostrar_antecessor_sucessor(e):
        valor = campo_numero.value
        if valor and valor.isdigit():
            numero = int(valor)
            antecessor = numero - 1
            sucessor = numero + 1
            resultado.value = f"Antecessor: {antecessor}, Sucessor: {sucessor}"
            page.update()
        else:
            resultado.value = "Por favor, digite um número válido."
            page.update()

    campo_numero = ft.TextField(
        label="Número",
        keyboard_type=ft.KeyboardType.NUMBER,
    )
    # mostrar o antecessor e o sucessor
    botao = ft.ElevatedButton("Mostrar", on_click=mostrar_antecessor_sucessor)
    
    # exibir o resultado
    resultado = ft.Text()

    page.add(campo_numero, botao, resultado)

ft.app(target=main)

